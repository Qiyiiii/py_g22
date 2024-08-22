# Intro

use this: ./matchapp/database/script.sh
or python3 matchapp/app/app.py if you got the database ready

Welcome to the **tinder-like matchapp** designed and developed by **Group 22** 
It is a very simple program that allows user to 
- register their information in database as an user
- login to see their profile with their unique userid that is automatically generated 
- change/delete their profile information (after deletion, their information will be removed from database)
- add favorite movie genres in both register page and in profile page as "Interest".
- match people that based on their preference weights of the information.
- like/dislike people that were matched and see the records of who they liked/disliked
- view a list of people they have liked who have also liked them back, showing mutual interest between both parties.

# matchapp_demo 
### [click here to redirect](https://github.com/Qiyiiii/py_g22/tree/main/matchapp_demo)
- the version of the porject that was demoed in the presentation on Aug 16,2024.
- satisfied all the basic demands of the project
- can depoly on the local host
- limited freedom on users' choices of matching 
- long matching time
- very limited imput validation and error handling
- user can only add favorite movie genres in the profile page

# matchapp
### [click here to redirect](https://github.com/Qiyiiii/py_g22/tree/main/matchapp)
Update:
- user can add favorite movie genres in the register page as well
- prevetion of under-aged population

# Architecture:
## Four **entity class** are stored in the database
### User:
basic information: 
- name: name of the user
- email: email of the user.   **Notice**: unique for all users, which is, one email address can only registered once to create user
- gender: gender of the user.   **Notice**: only limited to male and female
- location: postal code (USA only) of the user
- age: age of the user. **Notice**: must be larger than or equal to 18
- sim_weight: how user determine the importance of similar favorite movie genres in the matching algorithm
- loc_weight: how user determine the importance of distance in the matching algorithm
- age_weight: how user determine the importance of difference of age in the matching algorithm
### Interest
Favorite movie genres of a user in the format (userid, interest)
- userid reference the User instance with uid
- if the user with userid is deleted (delete profile), all interests related to the user with this userid will be automatically removed
### Actions
- actions between two users in the format (userid1, userid2, action)
- userid1 is the id of the user who does the action, and userid2 is the id of the user who get the action
### Coordinates
coordinate of the user location, stored automatically when user register or change their postal code
- uid: user id of the user
- latitude: latitude of the user location
- longitude: longitude of the user location
### Encapsulation & clean architecture:
- information are stored under database.db with schema.sql and some preloaded information in data.sql
- only dataManager.py (as use case classes for data management in SQLite) can access database.db and do CRUD operations on it
- match.py and profile.py under controller directory can access functions in dataManager.py, and they represent two main functions that our program can do
- Lastly, Flask can serve frontend content and use functions from match.py as well as profile.py to do the update
<img src="https://raw.githubusercontent.com/Qiyiiii/py_g22/0a0637e2f47acc0d9fb2b0edb6552501fee9d6a5/imgs/clean.png" alt="Clean Architecture Diagram" width="600" height="400">

## [Frontend content](https://github.com/Qiyiiii/py_g22/tree/main/matchapp/app)
### html files are stored in [here](https://github.com/Qiyiiii/py_g22/tree/main/matchapp/app/templates) under template directory
- index.html is the start page after running the program
### css and other static files are stored in [here](https://github.com/Qiyiiii/py_g22/tree/main/matchapp/app/templates)

# Requirements
[here to view required package for this project to be deployed in the local](https://github.com/Qiyiiii/py_g22/blob/main/matchapp/requirements.txt)
# How to start this project:
1. **Remotely**:
   - [click here to see our project that is hosted in the Azure cloud](qiyizhang71.com)
   - this project is remotely depolyed on qiyizhang71.com and chill-btgvfufugfdkgpbj.canadacentral-01.azurewebsites.net
2. **Locally**
   - Firstly, download required packages that can be found [here](https://github.com/Qiyiiii/py_g22/blob/main/matchapp/requirements.txt)
   - in the terminal, in the root page, enter: "./matchapp/database/script.sh", it will automatically load the example data and run the project
   - or run the commands line by line from the script.sh file that can be found [here](https://github.com/Qiyiiii/py_g22/blob/main/matchapp/database/script.sh)



  

