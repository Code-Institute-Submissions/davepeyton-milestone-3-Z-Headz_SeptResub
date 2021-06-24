![ipad](https://user-images.githubusercontent.com/76107271/123308265-5ad9f980-d51b-11eb-81a6-c5fd9a8c597e.jpg)

# UX
## Contents

---

- [UX](#ux)
  - [User Stories](#user-stories)
  - [Site Owner Goals](#goals)
  - [User Requirements and Expectations](#user-requirements)
  - [Design Choices](#design-choices)
    - Fonts
    - Icons
    - Colours
- [Database Model](#database-model)
- [Wireframes](#wireframes)
- [Features](#features)
- [Technologies](#technologies)
- [Testing](#testing)
- [Bugs](#bugs)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

## <a name="ux">UX</a>

---

### <a name="user-stories">User Stories</a>

#### All Users
1. As a user I want to be able to understand what the site is about.
2. I want to be able to easily navigate through the site.
3. I want to be able to search for list of Z's and learn about th esellect model.
4. I want to be able to find a car by model so that I can learn about that type of car.
5. I want to be able to recieve and send emails containing information about the cars.

#### Unregistered Users
1. As an unregistered user I want to be able to easily sign up to the website with ease.
2. I want to nagigate through the site with ease.

#### Registered Users
1. As a registered user I would like to be able to add my own cars to the collection and display on the website so that I can share my knowledge of that car.
2. I would like to be able to view any car that I have added easily and locate them in the same place.
3. I want to edit all my posts.


### <a name="goals">Site Owner Goals</a>

1. I want to inspire people to work on their own profiles.
2. Provide people with clear instructions on how to add, delete , edit content.
3. Increase the volume of people that visit this website over time.
4. The end goal is  to provide a visually appealing site.



## <a name="user-requirements">User Requirements and Expectations</a>

---

- The user is presented with a visually appealing website.
- The user is able to clearly navigate through the website on their first visit.
- The user will learn about the BMW Z range.
- The will be able to search for a specific Z and filter through by model.
- The user will be able to register for the website.
- The user will be able to add, edit and delete content. 
- The user will NOT be able to view the features that are reserved unless they are registered.


## <a name="design-choices">Design Choices</a>

---

### Fonts
- I used [Roboto](https://fonts.google.com/specimen/Roboto) for the body and after some deliberation and feeedback from some friends that tested the website I decided to use [Roboto Mono](https://fonts.google.com/specimen/Roboto+Mono) for all the headings and navbar items.


### Colours
 


### Icons
- The icons that I used in this project were provided by [Font Awesome](https://fontawesome.com/). I decided to use icons as they offer a pleasant visual aide to the site, also users tend to know that icons usually work as buttons.

## <a name="database-model">Database Model</a>
I used MongoDB's non-relational database for this website,

#### Seeds collection

|**Key**|**Type**|
|:-----|:-----|
|car_name|string|
|model_name|string|
|car_description|string|
|car_image|string|


#### Categories collection

|**Key**|**Type**|
|:-----|:-----|
|_id|ObjectId|string|
|category_name|string|


#### Users collection

|**Key**|**Type**|
|:-----|:-----|
|_id|ObjectId|string|
|username|string|
|password|string|


## <a name="wireframes">Wireframes</a>

---

The wireframes for this website can be found at the following links:
- []()
- []()
- []()
- []()



#### Changes to Wireframes
- Footer:
     - 
     - 
- 
     - 
- 
     - 
     - 

## <a name="features">Features</a>

---
**The main features of this website are:**
- an attractive design.
- a navigation bar that the user understands how to use even on their first visit to the website and that brings them to the appropriate part of the website.
- 
- 
- 
- an add car page so that users can add their own information on the cars.
- a profile page that allows users to edit or delete info that they have posted.
- registration, log in and log out pages.
- links to social network platforms and a way to sign up for a newsletter.

**Features that will be added in the future are:**
- an option to add car videos.
- a comment section so people can provide some extra tips on how to fix any Z issues.

## <a name="technologies">Technologies</a>

---

### Languages

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS3)
- [JavaScript](https://en.wikipedia.org/wiki/javascript)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Other

1. [Tiny PNG]()
   - Was used to compress the size of the hero image and the default card image.
2. [Font Awesome](https://fontawesome.com/)
   - The icons used were found at Font Awesome.
3. [Ucraft](https://www.ucraft.com/free-logo-maker)
   - Ucraft was used to make the logo for the favicon.
4. [Materialize](https://materializecss.com/)
   - Materialize was used throughout this website, in 
   particular for the navbar, form, modal, styling and for the responsiveness.
5. [jQuery](https://jquery.com/)
   - jQuery was used for initializing the Materialize features.
6. [Flask](https://flask.palletsprojects.com/en/1.1.x/)
   - Flask was used throughout the building of this website.
7. [Google Fonts](https://fonts.google.com/)
   - The fonts used for this website were found at Google Fonts.
8. [Balsamiq](https://balsamiq.com/)
   - The wireframes were made using Balsamiq.
9. [Github](https://github.com/)
   - This project was stored on Github.
10. [Gitpod](https://www.gitpod.io/)
    - Gitpod was used to write the code used for this website.
11. [Git](https://en.wikipedia.org/wiki/Git)
    - The version control system used for this project was Git.
12. [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools)
    - Chrome DevTools was used throughout the building of this website.
13. [WebFormatter](https://webformatter.com/html) 
    - WebFormatter was used to format the html and css files.
14. [Am I Responsive](http://ami.responsivedesign.is/) 
    - Am I Responsive was used to see how the website looked on different devices.
16. [Unsplash](https://unsplash.com/)
    - Unsplash was used to get images to use for the website.
17. [Pexels](https://www.pexels.com/)
    - Pexels was used to get images to use for the website.
18. [Emailjs](https://www.emailjs.com/)
    - Emailjs was used so that the user can sign up for the newsletter.
19. [Sweetalert2](https://sweetalert2.github.io/)
    - Sweetalert2 was used to display a message to the user when they sign up for the newsletter.
20. [JSHint](https://jshint.com/)
    - JSHint was used to test the JavaScript code.
21. [Python Tester](https://extendsclass.com/python-tester.html)
    - Used to test python code.
22. [Heroku](https://id.heroku.com/login)
    - Heroku was used to deploy this website


### Resources
The following websites were used as learning resources throughout the building of this project:
- [Code Institute](https://codeinstitute.net/)
- [Slack - Code Institutes Community](https://slack.com/intl/en-ie/)
- [w3schools](https://www.w3schools.com/)
- [Stack Overflow](https://stackoverflow.com/)
- [YouTube](https://www.youtube.com/)
- [CSS-Tricks](https://css-tricks.com/)
- [Markdown](https://commonmark.org/help/)

## <a name="testing">Testing</a>

---
The details of testing can be found [here]().

## <a name="deployment">Deployment</a>

---
## Deployment

The master branch of this repository is the most up to date version and has been used for the deployed version of the site.


### How to clone the project

To clone this project from its [GitHub repository]():

1. From the repository, click "Code"
2. In the "Clone >> HTTPS" section, copy the clone URL for the repository
3. Type `git clone` into your teminal and paste the URL you copied.

```
git clone <paste url>.
```

```
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "SECRET KEY")
os.environ.setdefault("MONGO_URI", "MONGO URI")
os.environ.setdefault("MONGO_DBNAME", "MONGO DBNAME")

```
8. **List env.py in your .gitignore file so that your variables are not pushed publicly.**
9. The app can now be run locally using
```
python3 run.py
```


### How to deploy to Heroku

To deploy the app to Heroku from its [GitHub repository](), I took the following steps:

1. Create "requirements.txt" and "Procfile" using the following commands:

```
pip3 freeze --local > requirements.txt
echo web: python app.py > Procfile
```

2. "Push" these files to GitHub.
3. "Log In" to [Heroku](https://id.heroku.com/login).
4. Select "Create new app" from the dropdown in the Heroku dashboard.
5. Choose a unique name ('zheadz') for the app pick whatever location is closest to you.
6. Click the "Deploy" tab and under "Deployment method" pick GitHub.
7. In "Connect to GitHub" enter your GitHub repository details and click "Connect".
8. Go to the "Settings" tab and under "Config Vars" select "Reveal Config Vars".
9. Enter the following keys and values, these must match the keys and values in your env.py file:

|**Key**|**Value**|
|:-----|:-----|
|IP|`0.0.0.0`|
|PORT|`5000`|
|SECRET_KEY|`Secret Key`|
|MONGO_URI|`Mongo URI`|
|MONGO_DBNAME|`Database Name`|

10. Go to the "Deploy" tab again and under "Automatic deploys" select "Enable Automatic Deploys".
11. Under "Manual deploy", select "master" and click "Deploy Branch".
12. On the top right of the page click "Open app".



## <a name="credits">Credits</a>

---

### Credits for Fonts

- [Google Fonts](https://fonts.google.com)
- [Font Pair](https://fontpair.co/)

### Media

- All images used on this website were found on [Unsplash](https://unsplash.com/) and [Pexels](https://www.pexels.com/).

### Code 

1. The code for the carousel is from Materialize and can be found [here](https://materializecss.com/carousel.html).
2. The code for the autoplay function for the carousel was found on [here](https://www.youtube.com/watch?v=I-roimeoeXM).
3. The code for the alerts shown to the user after signing up for the newletter was found on [sweetalert2](https://sweetalert2.github.io/).
4. Code was used from [Materialize](https://materializecss.com/) throughout this site, in particular for some buttons, colours, forms, reponsiveness and the modal.


### Content

- The content for zheadz can be found on []() and []().
## <a name="acknowledgements">Acknowledgements</a>


