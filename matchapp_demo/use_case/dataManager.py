import sqlite3
import pandas as pd

DB_PATH = "matchapp_demo/database/matchapp.db"

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
            # TODO: Implement the logic to update user gender
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
            # TODO: Implement the logic to update user age
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
            cursor.execute("UPDATE user SET location = ? WHERE uid = ?", (new_location, uid))
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
            # TODO: Implement the logic to update user name
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
            # TODO: Implement the logic to retrieve unliked users
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
    Add interest to a User with (uid).

    Return:
    bool: True on success, False otherwise.
    """
    try:
        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()
            # TODO: Implement the logic to add interest
            cursor.execute(
                "INSERT INTO interest (uid, interest) VALUES (?, ?)",
                (uid, interest)
            )

            connection.commit()

            return True

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

def get_user_interest(uid):
    """
    Get interests of a User with (uid).

    Return:
    List: interests of the User with (uid)
    """
    
    try:
        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()

            # TODO: Implement the logic to retrieve user interests
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
    

sql_commands = """
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Interest;
DROP TABLE IF EXISTS Actions;

CREATE TABLE IF NOT EXISTS User (
    uid INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL,
    gender VARCHAR(5) CHECK (gender IN ('Male', 'Female')),
    location VARCHAR(100),
    age INTEGER
);

CREATE TABLE IF NOT EXISTS Actions (
    uid1 INTEGER,
    uid2 INTEGER,
    like BOOLEAN NOT NULL,
    PRIMARY KEY (uid1, uid2),
    FOREIGN KEY (uid1) REFERENCES User(uid) ON DELETE CASCADE,
    FOREIGN KEY (uid2) REFERENCES User(uid) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Interest (
    uid INTEGER,
    interest VARCHAR(100) NOT NULL,
    PRIMARY KEY (uid, interest),
    FOREIGN KEY (uid) REFERENCES User(uid) ON DELETE CASCADE
);
"""

# conn = sqlite3.connect(DB_PATH)

# # Create a cursor object
# cursor = conn.cursor()

# try:
#     # Execute the SQL commands
#     cursor.executescript(sql_commands)
#     print("Tables created successfully.")
# except sqlite3.Error as e:
#     print(f"An error occurred: {e}")
# finally:
#     # Commit the changes and close the connection
#     conn.commit()
#     conn.close()
# Example usage
# if __name__ == "__main__":
 
#    user_id = create_user('Pokemon', 'pk@rotman.com', 'Male', 'Trt', 25)
#    remove_user_with_id(user_id)


