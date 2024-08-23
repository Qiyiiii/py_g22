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
Welcome to **chill**, a **tinder-like matching app** developed by **Group 22**. chill is a dating app designed for TV lovers, matching users based on their TV genre preferences. 

Our app is a very simple program that allows a user to 
- Create a Profile: Register and add their details to our database
- Log In: Access their account using a unique, auto-generated user ID
- Edit/Delete Profile: Update or remove their information; deletion will permanently erase the user's data from our database
- Manage TV Genres: Add their favorite TV genres on both the registration page and profile page
- Get Personalized Matches: Receive recommended profiles based on our matching algorithm
- Adjust Preferences: Customize the importance of factors like similarity, distance, and age on the preferences page
- Make and view actions: Like/dislike suggested profiles and view their own like/dislike history
- View Matches: See a list of users they've liked who have also liked them back


# matchapp_demo 
### [click here to redirect](https://github.com/Qiyiiii/py_g22/tree/main/matchapp_demo)
- The version of the project that was presented on Aug 16, 2024
- Can be deployed locally
- Satisfies all basic project specifications
- Matching algorithm weights are set to default values
- Long matching time; algorithm slowed down by fetching latitudes/longitudes and by non-vecotrized distance calculations
- Very limited imput validation and error handling
- User can only add TV genres in the profile page

# matchapp
### [click here to redirect](https://github.com/Qiyiiii/py_g22/tree/main/matchapp)
Update (chill 2.0):
- Can be deployed locally and remotely
- User can only enter a valid U.S. Zip code and an age of 18 or older
- Improved input validation and error handling
- User can add their preferred TV genres on the register page
- TV genres are displayed as buttons rather than as free-text
- Added a "Preferences" page, where a user can adjust the weights in the matching algorithm.
- New "Coordinates" table added to store latitudes and longitudes of our users
- Haversine distance is used to calculate the geographic distance between user; operation is vectorized for improved matching speed
- Penalties/Bonuses are applied in the matching algorithm, based on liking history
  
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
At chill, we tailor recommendations based on similairty of TV interests, geographic distance, and age similarity. To adjust how important these factors are to you, visit the "Preferences" page and click "Edit" to rate them on a scale from 1 (not important) to 10 (very important). We will adjust your algorithm based on the proportion of these ratings.

### Deleting your profile
We’re sorry to see you go! To delete your profile, click "Delete User" in the bottom left corner of the profile page and confirm by clicking "Ok."

# Architecture:
<img src="https://github.com/Qiyiiii/py_g22/blob/main/imgs/Group22.png" alt="Class Responsibility Collaborator Card" width="700" height="400">

## Four **entity class** are stored in the database
### User:
basic information: 
- uid: auto-generated unique user ID 
- name: name of the user
- email: email of the user.   **Notice**: each email address can be used to register only once (must be unique)
- gender: gender of the user.   **Notice**: limited to male and female
- location: zip code (U.S. only) of the user
- age: age of the user. **Notice**: must be greater than or equal to 18
- sim_weight: the relative importance of TV taste similarity in the matching algorithm
- loc_weight: the relative importance of distance in the matching algorithm
- age_weight: the relative importance of age similarity in the matching algorithm
### Interest
Favorite TV genres of a user in the format (userid, interest)
- userid references the User instance with uid
- If the user with userid is deleted (delete profile), all interests related to the user with this userid will be automatically removed
### Actions
- Actions (likes/dislikes) between two users in the format (userid1, userid2, action)
- userid1 is the id of the user who does the action, and userid2 is the id of the user who receives the action
### Coordinates
Coordinates of the user's location, stored automatically when a user registers or changes their zip code
- uid: user id of the user
- latitude: latitude of the user's location
- longitude: longitude of the user's location
### Encapsulation & clean architecture:
- Information is stored under database.db with schema.sql and some preloaded information in data.sql
- Only dataManager.py (as use case classes for data management in SQLite) can access database.db and do CRUD operations on it
- match.py and profile.py (under controller directory) can access functions in dataManager.py, and they represent two main functions that our program can do
- Flask can serve frontend content and use functions from match.py as well as profile.py to complete updates
<img src="https://raw.githubusercontent.com/Qiyiiii/py_g22/0a0637e2f47acc0d9fb2b0edb6552501fee9d6a5/imgs/clean.png" alt="Clean Architecture Diagram" width="600" height="400">

# Matching Algorithm

When a user wants to find a new match, our app searches for people in our database whom the user has not yet liked or disliked. In the current version, the app looks for people of the opposite gender within an age range of +/- 10 years. The resulting table is stored as  a pandas dataframe. 

The algorithm evaluates three primary factors: similarity in TV tastes, geographic distance, and age difference. The app then generates an overall score between 0 and 1. In chill 2.0, this score may be adjusted with a penalty/bonus.

1.	TV interests similarity: The Jaccard similarity between our user’s interests and the interests of potential matches.
3.	Geographic distance: Calculated using the Haversine distance formula, which determines the distance between two points on the Earth's surface based on latitude and longitude. We have used numpy to vectorize this calculation. 
4.	Age difference: The absolute value of the age difference between our user and potential matches.

Each potential match receives a score for each factor. These scores are normalized using sklearn's MinMaxScaler() before being combined. The factors are weighted so that the maximum combined score is 1.00. By default, similarity, distance, and age are weighted at 0.4, 0.4, and 0.2, respectively. In chill 2.0, users can adjust these weights according to their preferences. Users rate the importance of each factor between 1 and 10, so these values are normalized before being used in the matching algorithm

In chill 2.0, an additional bonus/penalty is applied to the overall score. If a potential match has already liked the user, their score is increased by 0.2. If they have already disliked the user, their score is decreased by 0.2. This increases the chances of our user getting a match. The maximum possible score is 1.2.

Equation: $\alpha(\textrm{TV similarity}) + \beta(1 - \textrm{distance}) + \gamma(1 - \textrm{age difference}) + \textrm{penalty}$

Defaults: $\alpha = 0.4,\beta = 0.4, \gamma = 0.2$

Penalty: $-0.2, 0, \textrm{or } 0.2$

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

  

