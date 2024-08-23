# **Index**
1. [Introduction](#introduction)
2. [Matchapp Demo](#matchapp_demo)
3. [Matchapp](#matchapp)
4. [Walkthrough](#walkthrough)
5. [Architecture](#architecture)
    - [User Entity](#user)
    - [Interest Entity](#interest)
    - [Actions Entity](#actions)
    - [Coordinates Entity](#coordinates)
    - [Encapsulation & Clean Architecture](#encapsulation--clean-architecture)
6. [Matching Algorithm](#matching-algorithm)
7. [Frontend Content](#frontend-content)
8. [Requirements](#requirements)
9. [How to Start This Project](#how-to-start-this-project)
10. [Milestones](#milestones)
# Introduction
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
- 
# Walkthrough
### Getting Started
To start the app (either remotely or locally), see the instructions in the section [How to Start This Project](#how-to-start-this-project).

### Creating a Profile
To create a new profile, click on "Create Account." You will be prompted to enter your first name, email, gender, a valid U.S. zip code, and your age (must be 18 or older). 

Our database is pre-loaded with singles aged 18-30 living in New York City. For the best results, choose a Manhattan zip code (e.g. 10001) and an age between 18 and 35. 

Choose TV genres that you're interested in. You can select as many as you would like from our list. When you're satisfied with your profile, click "Join." Our app will automatically log you in and show you a user ID. Make sure to note your user ID for future logins.

Help: If you encounter the error "Failed to create user," ensure your email is unique, your age is 18 or older, and you’ve entered a valid U.S. zip code.

### Logging In/Out
To log in, click "Login" on the home page. You will be prompted to enter your unique user ID. 

To log out, click "Log out" in the bottom right corner of the profile page. 

### Finding a Match and Liking/Disliking Users
Click "New Match" to view a profile of a potential match. If you're interested, click "Like User"; if not, click "Dislike User."

On the profile page, you can view profiles you have liked or disliked by clicking "Liked" or "Disliked." If you liked someone and they liked you back, congratulations! You’ve found a match, and they will appear on your "Matches" page. 

### Editing your profile
To update your information, go to the profile page and click the "Edit" buttons next to your current name, gender, location, or age.

Help: If you do not see updates to your age or location, ensure that your age is 18 or older and you’ve entered a valid U.S. zip code.

### Customizing preferences
At chill, we tailor recommendations based on TV tastes, distance, and age difference. To adjust how important these factors are to you, visit the "Preferences" page and click "Edit" to rate them on a scale from 1 (not important) to 10 (very important). We will adjust your algorithm based on the proportion of these ratings.

### Deleting your profile
We’re sorry to see you go! To delete your profile, click "Delete User" in the bottom left corner of the profile page and confirm by clicking "Ok."

# Architecture:
<img src="https://github.com/Qiyiiii/py_g22/blob/main/imgs/Group22.png" alt="Class Responsibility Collaborator Card" width="700" height="500">

## Four **entity class** are stored in the database
### User:
basic information: 
- uid: system assigned id of the user 
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

# Matching Algorithm

When a user wants to find a new match, our app searches for people in our database whom the user has not yet liked or disliked. In the current version, the app looks for people of the opposite gender within an age range of +/- 10 years. The resulting table is stored as  a pandas dataframe. 

The algorithm evaluates three primary factors: similarity in TV tastes, geographic distance, and age difference. The app then generates an overall score between 0 and 1. In chill 2.0, this score may be adjusted with a penalty/bonus.

1.	TV interests similarity: The Jaccard similarity between our user’s interests and the interests of potential matches.
3.	Geographic distance: Calculated using the Haversine distance formula, which determines the distance between two points on the Earth's surface based on latitude and longitude. We have used numpy to vectorize this calculation. 
4.	Age difference: The absolute value of the age difference between our user and potential matches.

Each potential match receives a score for each factor. These scores are normalized using sklearn's MinMaxScaler() before being combined. The factors are weighted so that the maximum combined score is 1.00. By default, similarity, distance, and age are weighted at 0.4, 0.4, and 0.2, respectively. In chill 2.0, users can adjust these weights according to their preferences. 

In chill 2.0, an additional bonus/penalty is applied to the overall score. If a potential match has already liked the user, their score is increased by 0.2. If they have already disliked the user, their score is decreased by 0.2. This increases the chances of our user getting a match.

The user ID of the individual with the highest overall score is returned as the recommended match.



## [Frontend content](https://github.com/Qiyiiii/py_g22/tree/main/matchapp/app)
### html files are stored in [here](https://github.com/Qiyiiii/py_g22/tree/main/matchapp/app/templates) under template directory
- index.html is the start page after running the program
### css and other static files are stored in [here](https://github.com/Qiyiiii/py_g22/tree/main/matchapp/app/templates)

# Requirements
[here to view required package for this project to be deployed in the local](https://github.com/Qiyiiii/py_g22/blob/main/matchapp/requirements.txt)
# How to start this project:
1. **Remotely**:
   - this project is remotely depolyed on qiyizhang71.com/ and chill-btgvfufugfdkgpbj.canadacentral-01.azurewebsites.net
   - [click here to see our project that is hosted in the Azure cloud](https://qiyizhang71.com/)
2. **Locally**
   - Firstly, download required packages that can be found [here](https://github.com/Qiyiiii/py_g22/blob/main/matchapp/requirements.txt)
   - in the terminal, in the root page, enter: "./matchapp/database/script.sh", it will automatically load the example data and run the project
   - or run the commands line by line from the script.sh file that can be found [here](https://github.com/Qiyiiii/py_g22/blob/main/matchapp/database/script.sh)

  
# Milestones
The process of the production of this project has been tracked and followed by plans
- Skeleton of the code structure were designed and implemented (Aug 9th - Aug 11th)
- Completion of the project backend (Aug 12th - Aug 13th)
- Completion of the project frontend + better looking interface + fixed bugs in project backend (Aug 14th)
- Debug the project as a whole, improve user experience(Aug 15th)
- Brainstorm new features as well as potential improvement of the project (Aug 17th)
- New features been implemented: 1. User can choose favorite movie genre in the register page 2. User can set thier match preferences 3. Quicker matching speed 4.User can only add true US postal code as their location 4. Error handlings, e.g. user must enter valid user id in the log in page (Aug 18th - Aug 21th)

  

