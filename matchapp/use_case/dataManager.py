import sqlite3
import pandas as pd
import numpy as np

DB_PATH = "matchapp/database/matchapp.db"

def create_user(name, email, gender, age, location, latitude,longitude, interests):
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
                INSERT INTO User (name, email, gender, location, age, sim_weight, loc_weight, age_weight)
                VALUES (?, ?, ?, ?, ?, 10, 10, 5)
            ''', (name, email, gender, location, age))
            # Get id of the new user
            user_id = cursor.lastrowid
            # Commit the changes to the database
            connection.commit()

            cursor.execute('''
                INSERT INTO Coordinates (uid, latitude, longitude)
                VALUES (?, ?, ?)
            ''', (user_id, latitude, longitude))
            connection.commit()
            for interest in interests:
                print(f"Processing interest: {interest}, Type: {type(interest)}")
                if not add_user_interest(user_id, interest):
                    print(f"Failed to add interest '{interest}' for user {user_id}")
                    return -1  # Rollback or handle error as needed

            # Commit the changes to the database
            connection.commit()

            print(f"User {name} added successfully with ID {user_id}.")
            return user_id          

    except sqlite3.Error as e:
        print(f"Error creating user: {e}")
        return -1

def get_user_coordinates(uid):
    try:
        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT latitude, longitude FROM Coordinates WHERE uid = ?', (uid,))
            return cursor.fetchone()

    except sqlite3.Error as e:
        # print error message
        print(f"Could not retrieve coordinates: {e}")
        return ()

def get_users(uid, my_gender, my_min_age, my_max_age):
    """
    get a datafrmae of users that who could be compatible with our user (uid)

    Returns:
    Dataframe: user
    """
    try:
        with sqlite3.connect(DB_PATH) as connection:
            create_matches_table = """
            SELECT user.uid, user.age, A.like, interest.interest, coordinates.latitude, coordinates.longitude
            FROM user
            LEFT JOIN Actions ON user.uid = Actions.uid2 AND Actions.uid1 = ?
            LEFT JOIN Actions as A ON user.uid = A.uid1 AND A.uid2 = ?
            LEFT JOIN Interest ON user.uid = interest.uid
            LEFT JOIN Coordinates ON user.uid = coordinates.uid
            WHERE Actions.uid2 IS NULL 
            AND user.gender != ?
            AND user.age BETWEEN ? AND ?;
            """

            rec = pd.read_sql_query(create_matches_table, connection, params=(uid, uid,my_gender, my_min_age, my_max_age), dtype={'latitude': np.float64, 'longitude': np.float64,'like':np.float64})
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

def get_user_weights(uid):
    try:
        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                SELECT sim_weight, loc_weight, age_weight FROM User WHERE uid = ?
            ''', (uid,))
            result = cursor.fetchone()
            if result:
                return result  # This will return a tuple (sim_weight, loc_weight, age_weight)
            else:
                return ()  # Return an empty tuple if the user was not found
    except sqlite3.Error as e:
        print(f"Error fetching user weights: {e}")
        return ()

def remove_user_with_id(uid):
    try:
        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()
            
            # Delete the specified user
            
            cursor.execute('PRAGMA foreign_keys = ON;')
            cursor.execute('DELETE FROM user WHERE uid = ?', (uid,))
            connection.commit()
            cursor.execute('SELECT interest FROM Interest WHERE uid = ?', (uid,))
            print( cursor.fetchone())
        
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
            cursor.execute("UPDATE user SET gender = ? WHERE uid = ?", (new_gender, uid))
            connection.commit()
            if cursor.rowcount == 0:
                return False
            return True

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
            cursor.execute("UPDATE user SET age = ? WHERE uid = ?", (new_age, uid))
            connection.commit()
            if cursor.rowcount == 0:
                return False
            return True

    except sqlite3.Error as e:
        # print error message
        # change it to your own
        print(f"Not succuessful: {e}")
        return ()

def update_user_location(uid, new_location, new_latitude, new_longitude):
    """
    Change the location of the user with the specific uid.

    Return:
    bool: True on success, False otherwise.
    """
    try:
        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE User SET location = ? WHERE uid = ?",(new_location, uid))
            cursor.execute("UPDATE Coordinates SET latitude = ?, longitude = ? WHERE uid = ?", (new_latitude, new_longitude, uid))
            connection.commit()
            if cursor.rowcount == 0:
                return False
            return True
        
        

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
            cursor.execute("UPDATE user SET name = ? WHERE uid = ?", (new_name, uid))
            connection.commit()
            if cursor.rowcount == 0:
                return False
            return True

    except sqlite3.Error as e:
        # print error message
        # change it to your own
        print(f"Not succuessful: {e}")
        return False
        
def update_sim_weight(uid, new_sim_weight):
    """
    Change the importance of TV taste similarity to a User with (uid)

    Return:
    bool: True on success, False otherwise.
    """
    try:
        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE user SET sim_weight = ? WHERE uid = ?", (new_sim_weight, uid))
            connection.commit()
            return cursor.rowcount > 0
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False

def update_loc_weight(uid, new_loc_weight):
    """
    Change the importance geographic distance to a User with (uid)

    Return:
    bool: True on success, False otherwise.
    """
    try:
        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE user SET loc_weight = ? WHERE uid = ?", (new_loc_weight, uid))
            connection.commit()
            return cursor.rowcount > 0
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False

def update_age_weight(uid, new_age_weight):
    """
    Change the importance of age difference to a User with (uid)

    Return:
    bool: True on success, False otherwise.
    """
    try:
        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE user SET age_weight = ? WHERE uid = ?", (new_age_weight, uid))
            connection.commit()
            return cursor.rowcount > 0
    except sqlite3.Error as e:
        print(f"Database error: {e}")
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
            return True
      

    except sqlite3.Error as e:
        # print error message
        # change it to your own
        print(f"Not succuessful: {e}")
        return False

def get_user_likes(uid):
    """
    Find all ids of Users that the User with (uid) liked.

    Return:
    List: Users that the User with (uid) liked
    """
    try:
        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT uid2 FROM Actions WHERE uid1= ? and like = True ", (uid,))
            liked_users = [row[0] for row in cursor.fetchall()]
            return liked_users

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
            cursor.execute("""
                            SELECT uid2 FROM Actions WHERE uid1 = ? and like = False
                        """, (uid,))

            unliked_users = [row[0] for row in cursor.fetchall()]
            return unliked_users

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
            query = """
                SELECT u.uid
                FROM Actions a 
                JOIN User u ON u.uid = a.uid2
                WHERE a.uid1 = ? AND a.like = True
                AND EXISTS (
                    SELECT 1 FROM Actions
                    WHERE uid1 = a.uid2 AND uid2 = ? AND like = True
                );
            """
            cursor = connection.cursor()
            cursor.execute(query, (uid, uid))
            result = [row[0] for row in cursor.fetchall()]

            
            if result:
                print("Mutual likes found!")
            else:
                print("No mutual likes found.")
            
            return result

    except sqlite3.Error as e:
        print(f"Error fetching mutual likes: {e}")
        return pd.DataFrame()


# Interest CRUD
def add_user_interest(uid, interest):
    """
    Add a TV genre to the interests of a User with (uid)

    Return:
    bool: True on success, False otherwise.
    """
    try:
        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO interest (uid, interest) VALUES (?, ?)",
                (uid, interest)
            )
            connection.commit()
            print(f"Added interest '{interest}' for user {uid}")
            return True

    except sqlite3.Error as e:
        print(f"Not successful: {e}")
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

def get_user_interest(uid):
    """
    Get interests of a User with (uid).

    Return:
    List: interests of the User with (uid)
    """
    
    try:
        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()

            cursor.execute(
                "SELECT interest FROM interest WHERE uid= ?",
                (uid,)
            )
            interests = [interest[0] for interest in cursor.fetchall()]
            return interests


    except sqlite3.Error as e:
        # print error message
        # change it to your own
        print(f"Not succuessful: {e}")
        return []
    
# Example usage
# if __name__ == "__main__":
