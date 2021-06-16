
import os
import json
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mongoengine import MongoEngine
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/")
@app.route("/get_cars")
def get_cars():
    cars = list(mongo.db.cars.find())
    return render_template("cars.html", cars=cars)


@app.route("/about")
def about():
    data = []
    with open("data/cars.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", cars=data)


@app.route("/cars")
def cars():
    return render_template("cars.html")


@app.route("/about/<car_name>")
def about_car(car_name):
    car = {}
    with open("data/cars.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == car_name:
                car = obj
    return render_template("about.html", car=car)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome Back, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))
    

@app.route("/add_car", methods=["GET", "POST"])
def add_car():
    if request.method == "POST":
        car = {
            "category_name": request.form.get("category_name"),
            "car_model": request.form.get("car_model"),
            "car_color": request.form.get("car_color"),
            "car_year": request.form.get("car_year"),
            "car_origen": request.form.get("car_origen"),
            "car_description": request.form.get("car_description"),
            "car_extras": request.form.get("car_extras"),
            "post_date": request.form.get("post_date"),
            "car_image": request.form.get("car_image"),
            "created_by": session["user"]
        }
        mongo.db.cars.insert_one(car)
        flash("Car Successfully Added")
        return redirect(url_for("get_cars"))
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_car.html", categories=categories)


@app.route("/edit_car/<car_id>", methods=["GET", "POST"])
def edit_car(car_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "car_model": request.form.get("car_model"),
            "car_color": request.form.get("car_color"),
            "car_year": request.form.get("car_year"),
            "car_origen": request.form.get("car_origen"),
            "car_description": request.form.get("car_description"),
            "car_extras": request.form.get("car_extras"),
            "post_date": request.form.get("post_date"),
            "car_image": request.form.get("car_image"),
            "created_by": session["user"]
        }
        mongo.db.cars.update({"_id": ObjectId(car_id)}, submit)
        flash("Car Successfully Updated")

    car = mongo.db.cars.find_one({"_id": ObjectId(car_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_car.html", car=car, categories=categories)


@app.route("/delete_car/<car_id>")
def delete_car(car_id):
    mongo.db.cars.remove({"_id": ObjectId(car_id)})
    flash("Car Successfully Deleted")
    return redirect(url_for("get_cars"))


@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT")),
        debug=True) #change to false before submit