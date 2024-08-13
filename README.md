# Intro
Welcome to the **tinder-like matchapp** designed and developed by **Group 22** 
It is a very simple program that allows user to 
- register their information in database as an user
- login to see their profile with their unique userid that is automatically generated 
- change/delete their profile information (after deletion, their information will be removed from database)
- match people that based on their information
- like/unlike people that were matched
- find people they liked/unliked and people also liked them back (users that are mutually liked with the login user)

# demo (low-level prototype)
### [click here to redirect](https://github.com/Qiyiiii/py_g22/tree/main/demo).
- very simple program with data preloaded into different lists (Users, Interests, Actions) each time when the program starts
- user will be directly loged in and can only interact with users that were preloaded
- user can match with other user based on the number of interests that are shared
- user can view users he liked/unliked
- user can view his profile
- user can view people he liked and also liked him

# matchapp (web application)
### [click here to redirect](https://github.com/Qiyiiii/py_g22/tree/main/matchapp)
- still a very simple program but with sqllite embeded and more encapsulated design and use **Flask** to serve frontend content 
- users now can do whatever that is decribed in the [**Intro**](#intro)
- can be deployed on the website

# Architecture:
## Three **entity class** are stored in the database
### User:
basic information: 
- name: name of the user
- email: email of the user.   **Notice**: unique for all users, which is, one email address can only registered once to create user
- gender: gender of the user.   **Notice**: only limited to male and female
- location: location or address of the user
- age: age of the user

### Interest
interest of a user in the format (userid, interest)
- userid reference the User instance with uid
- if the user with userid is deleted (delete profile), all interests related to the user with this userid will be automatically removed
### Actions
- actions between two users in the format (userid1, userid2, action)
- userid1 is the id of the user who does the action, and userid2 is the id of the user who get the action

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

# How to set up virtualenv and downloaded required package:
- **Warning**: my original venv file only support for macos users, could cause some problems if you are using other os
- [click here for the tutorial](https://virtualenv.pypa.io/en/latest/user_guide.html)
- In order to make sure you have all packages needed, you should, in shell, enter: pip install -r requirements.txt
- [requirements can be found here](https://github.com/Qiyiiii/py_g22/blob/4e266a714d9fa10989a0df46797518ea24077f17/matchapp/requirements.txt)
- also the version of python during initial development is Python 3.9.12
  
# Database start-up
## In order to import required tables and pre-created data into the database
**warning** please setup the virtualenv first or make sure all required packages are downloaded before this step
in the database directory (for mac usrer):
- chmod u+x script.sh
- ./script.sh
  
or you can
- sqlite3 matchapp.db < schema.sql
- sqlite3 matchapp.db < data.sql

to first load the required table for "entity class" and then load pre-created data


  

