import sqlite3
import pandas as pd

DB_PATH = "../database/matchapp.db"

def create_user(name, email, gender, location, age):
    """
    Create a new user and insert into the database.

    Returns: 
    int: uid of the created user
    """
    try:
        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()
            # Perform Insert to the table
            cursor.execute('''
                INSERT INTO User (name, email, gender, location, age)
                VALUES (?, ?, ?, ?, ?)
            ''', (name, email, gender, location, age))

            # Save change
            connection.commit()

            # Get id of the new user
            user_id = cursor.lastrowid
            
            print(f"User {name} added successfully with ID {user_id}.")
            return user_id
    except sqlite3.Error as e:
        print(f"Error creating user: {e}")
        return -1


def get_users(uid):
    """
    get a datafrmae of users that who could be compatible with our user (uid)

    Returns: 
    Dataframe: user
    """
    my_gender = get_user_info(uid)[2]
    try:
        with sqlite3.connect(DB_PATH) as connection:
            create_matches_table = """
            SELECT user.uid, user.name, user.gender, user.age, user.location, interest.interest
            FROM user
            LEFT JOIN Actions ON user.uid = Actions.uid2 AND Actions.uid1 = ?
            LEFT JOIN interest ON user.uid = interest.uid
            WHERE Actions.uid2 IS NULL 
            AND user.gender != ?;
            """
            rec = pd.read_sql_query(create_matches_table, connection, params=(uid, my_gender,))
            return rec


    except sqlite3.Error as e:
        print(f"Error fetch users: {e}")
        return []

def get_user_info(uid):

    """
    Get the profile information of the User with (uid) from the database.

    Returns: 
    Tuple(name, email, gender, location, age)
    """
    try:
        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT name, email, gender, location, age FROM User WHERE uid = ?', (uid,))
            return cursor.fetchone()

    except sqlite3.Error as e:
        # print error message
        # change it to your own
        print(f"Not succuessful: {e}")
        return ()


def remove_user_with_id(uid):
    """
    Delete an existing user from the database and update other users' references.

    Return:
    bool: True on success, False otherwise.
    """
    try:
        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()

            # Fetch all users
            cursor.execute('SELECT user_id, liked_users, disliked_users, matches FROM users')
            users = cursor.fetchall()

            # Process each user to update their lists
            for user_data in users:
                current_user_id, liked_users, disliked_users, matches = user_data

                liked_users_list = list(map(int, liked_users.split(','))) if liked_users else []
                disliked_users_list = list(map(int, disliked_users.split(','))) if disliked_users else []
                matches_list = list(map(int, matches.split(','))) if matches else []

                # Remove the UID from other users' lists
                if uid in liked_users_list:
                    liked_users_list.remove(uid)
                if uid in disliked_users_list:
                    disliked_users_list.remove(uid)
                if uid in matches_list:
                    matches_list.remove(uid)

                # Update the current user with the modified lists
                updated_liked_users = ','.join(map(str, liked_users_list))
                updated_disliked_users = ','.join(map(str, disliked_users_list))
                updated_matches = ','.join(map(str, matches_list))

                cursor.execute('''
                    UPDATE users
                    SET liked_users = ?, disliked_users = ?, matches = ?
                    WHERE user_id = ?
                ''', (updated_liked_users, updated_disliked_users, updated_matches, current_user_id))

            # Delete the specified user
            cursor.execute('DELETE FROM users WHERE user_id = ?', (uid,))
            connection.commit()
        
        return True
    except sqlite3.Error as e:
        print(f"Failed to remove user: {e}")
        return False


def update_user_gender(uid, new_gender):
    """
    Change the gender of the user with the specific uid.

    Return:
    bool: True on success, False otherwise.
    """

    try:
        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()
            # TODO: Implement the logic to update user gender
            pass

    except sqlite3.Error as e:
        # print error message
        # change it to your own
        print(f"Not succuessful: {e}")
        return False

def update_user_age(uid, new_age):
    """
    Change the age of the user with the specific uid.

    Return:
    bool: True on success, False otherwise.
    """
    
    try:
        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()
            # TODO: Implement the logic to update user age
            pass

    except sqlite3.Error as e:
        # print error message
        # change it to your own
        print(f"Not succuessful: {e}")
        return ()

def update_user_location(uid, new_location):
    """
    Change the location of the user with the specific uid.

    Return:
    bool: True on success, False otherwise.
    """
    try:
        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()
            # TODO: Implement the logic to update user location
            pass

    except sqlite3.Error as e:
        # print error message
        # change it to your own
        print(f"Not succuessful: {e}")
        return False

def update_user_name(uid, new_name):
    """
    Change the name of the user with the specific uid.

    Return:
    bool: True on success, False otherwise.
    """
    try:
        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()
            # TODO: Implement the logic to update user name
            pass

    except sqlite3.Error as e:
        # print error message
        # change it to your own
        print(f"Not succuessful: {e}")
        return False

# Action CRUD
def add_action(uid1, uid2, action):
    """
    Add a specific user interaction from user with (uid1) to user with (uid2).

    Return:
    bool: True on success, False otherwise.
    """

    try:
        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()
            if action == 'like':
                like_value = True
            elif action == 'dislike':
                like_value = False
            else:
                raise ValueError("Invalid action specified. Must be 'like' or 'dislike'.")

            insert_query = """INSERT INTO Actions (uid1, uid2, like)
                                      VALUES (?, ?, ?);"""

            cursor.execute(insert_query, (uid1, uid2, like_value))
            connection.commit()
            pass

    except sqlite3.Error as e:
        # print error message
        # change it to your own
        print(f"Not succuessful: {e}")
        return False

# def change_action(uid1, uid2, action):
#     """
#     Change a specific user interaction from user with (uid1) to user with (uid2).

#     Return:
#     bool: True on success, False otherwise.
#     """
    
#     try:
#         with sqlite3.connect(DB_PATH) as connection:
#             cursor = connection.cursor()
#             # TODO: Implement the logic to change an action
#             pass

#     except sqlite3.Error as e:
#         # print error message
#         # change it to your own
#         print(f"Not succuessful: {e}")
#         return False

# def get_user_action(uid):
#     """
#     Find all actions from that user to other people.

#     Return:
#     List: actions that from User with (uid)
#     """
#     try:
#         with sqlite3.connect(DB_PATH) as connection:
#             cursor = connection.cursor()
#             # TODO: Implement the logic to retrieve user actions
#             pass

#     except sqlite3.Error as e:
#         # print error message
#         # change it to your own
#         print(f"Not succuessful: {e}")
#         return []

def get_user_likes(uid):
    """
    Find all ids of Users that the User with (uid) liked.

    Return:
    List: Users that the User with (uid) liked
    """
    try:
        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()
            # TODO: Implement the logic to retrieve liked users
            pass

    except sqlite3.Error as e:
        # print error message
        # change it to your own
        print(f"Not succuessful: {e}")
        return []

def get_user_unlikes(uid):
    """
    Find all ids of Users that the User with (uid) unliked.

    Return:
    List: Users that the User with (uid) unliked
    """
    try:
        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()
            # TODO: Implement the logic to retrieve unliked users
            pass

    except sqlite3.Error as e:
        # print error message
        # change it to your own
        print(f"Not succuessful: {e}")
        return []

def get_mutual_likes(uid):
    """
    Find all ids of Users that the User with (uid) liked that also likes User with (uid).

    Return:
    List: all Users that the User with (uid) liked that also likes User with (uid).
    """
    try:
        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()
            # TODO: Implement the logic to retrieve users that also likes the User with uid
            pass

    except sqlite3.Error as e:
        # print error message
        # change it to your own
        print(f"Not succuessful: {e}")
        return []


# Interest CRUD
def add_user_interest(uid, interest):
    """
    Add interest to a User with (uid).

    Return:
    bool: True on success, False otherwise.
    """
    try:
        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()
            # TODO: Implement the logic to add interest
            pass

    except sqlite3.Error as e:
        # print error message
        # change it to your own
        print(f"Not succuessful: {e}")
        return False

# def remove_interest(uid, interest):
#     """
#     Remove interest from a User with (uid).

#     Return:
#     bool: True on success, False otherwise.
#     """
#     try:
#         with sqlite3.connect(DB_PATH) as connection:
#             cursor = connection.cursor()
#             # TODO: Implement the logic to remove interest
#             pass

#     except sqlite3.Error as e:
#         # print error message
#         # change it to your own
#         print(f"Not succuessful: {e}")
#         return False

def get_interest(uid):
    """
    Get interests of a User with (uid).

    Return:
    List: interests of the User with (uid)
    """
    
    try:
        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT interest FROM Interest WHERE uid = ?', (uid,))
            interests_tuples = cursor.fetchall()
            interests_list = [item[0] for item in interests_tuples]
            return interests_list

            pass

    except sqlite3.Error as e:
        # print error message
        # change it to your own
        print(f"Not succuessful: {e}")
        return []
    
# Example usage
#if __name__ == "__main__":
#    user_id = create_user('Pokemon', 'pk@rotman.com', 'Male', 'Trt', 25)

