import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controller.profile import *
from controller.match import *
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database/matchapp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.getenv('SECRET_KEY', 'a_default_secret_key')


db = SQLAlchemy(app)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/profile/<int:uid>')
def profile(uid):
    user_info = get_user_info(uid)
    user_interests = get_interest(uid)

    if user_info:
        return render_template("profile.html", user=user_info, uid=uid, interests = user_interests)
    else:
        flash(f"User with {uid} not found")
        return render_template("index.html")

@app.route('/setting/<int:uid>')
def display_weights(uid):
    weights = get_user_weights(uid)
    if weights:
        sim_weight, loc_weight, age_weight = weights
        return render_template('setting.html', uid=uid, sim_weight=sim_weight, loc_weight=loc_weight, age_weight=age_weight)
    else:
        flash("Could not retrieve preference.", "error")
        return redirect(url_for('profile', uid=uid))

    


# def adjust_weights(uid):
#     sim_weight = request.form.get('sim_weight')
#     loc_weight = request.form.get('loc_weight')
#     age_weight = request.form.get('age_weight')
    
#     # Ensure weights are provided and valid
#     if sim_weight and loc_weight and age_weight:
#         flash("All weights must be provided.", "error")
#         return redirect(url_for('profile', uid=uid))

#     # Convert weights to integers
#     try:
#         sim_weight = int(sim_weight)
#         loc_weight = int(loc_weight)
#         age_weight = int(age_weight)
#     except ValueError:
#         flash("Weights must be valid integers.", "error")
#         return redirect(url_for('profile', uid=uid))

#     # Update weights in the database
#     if update_sim_weight(uid, sim_weight) and update_loc_weight(uid, loc_weight) and update_age_weight(uid, age_weight):
#         flash("Weights updated successfully.", "success")
#     else:
#         flash("Failed to update weights.", "error")

#     return redirect(url_for('profile', uid=uid))

@app.route('/like/<int:uid1>/<int:uid2>')
def like(uid1, uid2):

    like_user(uid1, uid2)

    flash(f"You liked {get_user_info(uid2)[0]}")
    return redirect(url_for('profile', uid=uid1))


@app.route('/unlike/<int:uid1>/<int:uid2>')
def unlike(uid1, uid2):

    unlike_user(uid1, uid2)

    flash(f"You disliked {get_user_info(uid2)[0]}")
    return redirect(url_for('profile', uid=uid1))

    
@app.route('/match/<int:uid1>')
def match(uid1):
    matched_userid = find_match(uid1)
    # matched_userid = 3
    if matched_userid == -1:
        flash(f"Can't find a match for user {uid1}")
        return redirect(url_for('profile', uid=uid1))

    matched_user_info = get_user_info(matched_userid)
    interests = get_interest(matched_userid)

    if matched_userid:
        return render_template("matchedPage.html", user= matched_user_info, uid1=uid1, uid2=matched_userid, interests = interests)
    else:
        flash(f"Can't find a match for user {uid1}")
        return redirect(url_for('profile', uid=uid1))

@app.route('/liked-users/<int:uid>')
def liked_users(uid):
    usersids = get_liked_users(uid)
    users = [list(get_user_info(user_id)) + [get_user_interest(user_id)] for user_id in usersids if get_user_info(user_id)]

    title = "People I Liked"  # Define the title

    if users:
        return render_template("userList.html", users=users, uid=uid, title=title)  
    else:
        flash(f"User with {uid} didn't like any users")
        return render_template("userList.html", users=users, uid=uid, title=title)  


@app.route('/unliked-users/<int:uid>')
def unliked_users(uid):
    usersids = get_unliked_users(uid)
    users = [list(get_user_info(user_id)) + [get_user_interest(user_id)] for user_id in usersids if get_user_info(user_id)]
    title = "People I Unliked"  # Define the title

    if users:
        return render_template("userList.html", users=users, uid=uid, title=title)  
    else:
        flash(f"User with {uid} didn't unlike any users")
        return render_template("userList.html", users=users, uid=uid, title=title)  


@app.route('/mutually-liked-users/<int:uid>')
def mutual_users(uid):
    usersids = get_mutual_liked_users(uid)
    users = [list(get_user_info(user_id)) + [get_user_interest(user_id)] for user_id in usersids if get_user_info(user_id)]
    title = "People Mutually Liked"  

    if users:
        return render_template("userList.html", users=users, uid=uid, title=title)  
    else:
        flash(f"User with {uid} has no mutually liked users")
        return render_template("userList.html", users=users, uid=uid, title=title)  


@app.route('/add_interest/<int:uid>', methods=['POST'])
def add_user_interest(uid):
    interest = request.form.get('interest')
    add_interest(uid, interest)
    return redirect(url_for('profile', uid=uid))

@app.route('/create_user', methods=['POST'])
def create_user():
    name = request.form['name']
    email = request.form['email']
    gender = request.form['gender']
    location = request.form['location']
    age = request.form['age']
    interests = request.form.get('interests')  

    interests_list = interests.split(",") if interests else []

    userid = add_user(name, email, gender, location, age, interests_list)
    
    if userid > 0:
        flash(f"User created successfully with Userid {userid}")
        return redirect(url_for('profile', uid=userid))
    else:
        flash("Failed to create user")
        return redirect(url_for('index'))

@app.route('/editname/<int:uid>', methods=['POST'])
def edit_name(uid):
    
    content= request.form.get('content')
    print(content)
    if change_profile(Content_type.NAME, uid, content):
        flash(f"Profile changed")
    return redirect(url_for('profile', uid=uid))

@app.route('/editgender/<int:uid>', methods=['POST'])
def edit_gender(uid):
    
    content= request.form.get('content')

    if change_profile(Content_type.GENDER, uid, content):
        flash(f"Profile changed")
    return redirect(url_for('profile', uid=uid))

@app.route('/editlocation/<int:uid>', methods=['POST'])
def edit_location(uid):
    
    content= request.form.get('content')
    if change_profile(Content_type.LOCATION, uid, content):
        flash(f"Profile changed")
    return redirect(url_for('profile', uid=uid))

@app.route('/editage/<int:uid>', methods=['POST'])
def edit_age(uid):
    
    content= request.form.get('content')
    if change_profile(Content_type.AGE, uid, content):
        flash(f"Profile changed")
    return redirect(url_for('profile', uid=uid))

@app.route('/edit_similarity_weight/<int:uid>', methods=['POST'])
def edit_similarity_weight(uid):
    content = request.form.get('content')
    if not content:
        flash("No content received.", "error")
        return redirect(url_for('display_weights', uid=uid))
    
    try:
        new_weight = int(content)
    except ValueError:
        flash("Invalid content: must be an integer.", "error")
        return redirect(url_for('display_weights', uid=uid))

    if update_sim_weight(uid, new_weight):
        flash("Interest preference updated successfully.", "success")
    else:
        flash("Failed to update interest preference.", "error")
    return redirect(url_for('display_weights', uid=uid))

@app.route('/edit_location_weight/<int:uid>', methods=['POST'])
def edit_location_weight(uid):
    content = request.form.get('content')
    if not content:
        flash("No content received.", "error")
        return redirect(url_for('display_weights', uid=uid))
    
    try:
        new_weight = int(content)
    except ValueError:
        flash("Invalid content: must be an integer.", "error")
        return redirect(url_for('display_weights', uid=uid))

    if update_loc_weight(uid, new_weight):
        flash("Location preference updated successfully.", "success")
    else:
        flash("Failed to update location preference.", "error")
    return redirect(url_for('display_weights', uid=uid))

@app.route('/edit_age_weight/<int:uid>', methods=['POST'])
def edit_age_weight(uid):
    content = request.form.get('content')
    if not content:
        flash("No content received.", "error")
        return redirect(url_for('display_weights', uid=uid))
    
    try:
        new_weight = int(content)
    except ValueError:
        flash("Invalid content: must be an integer.", "error")
        return redirect(url_for('display_weights', uid=uid))

    if update_age_weight(uid, new_weight):
        flash("Age preference updated successfully.", "success")
    else:
        flash("Failed to update age preference.", "error")
    return redirect(url_for('display_weights', uid=uid))



@app.route('/delete_user/<int:uid>', methods=['POST'])
def delete_user(uid):
    success = remove_user_with_id(uid)
    if success:
        flash(f"User {uid} has been deleted successfully.")
        return render_template("index.html")
    else:
        flash(f"Failed to delete User {uid}.")
        return redirect(url_for('profile', uid=uid))


if __name__ == "__main__":
  
    

    port = int(os.getenv('PORT', 8000))  # Default to 8000 if PORT is not set
    app.run(debug=True, host="0.0.0.0", port=port)