import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from use_case.dataManager import *



from enum import Enum
class Content_type(Enum):
    NAME = 1
    GENDER = 2
    Location = 3
    AGE = 4


def add_user(name, email, gender, location, age):
    """
    add User with name, email, gender, location, age into databse

    Return:
    On success, return uid of the user created
    else -1
    """
    return create_user(name, email, gender, location, age)


def get_user_profile(uid):
    """
    get the profile of the user with (uid)

    Return:
    On success, return tuple(name, email, gender, location, age)
    else ()
    """
    return get_user_info(uid)

def change_profile(content_type, uid, content):
    """
    based on the type of content, change profile

    Return:
    On success, return True
    else False

    Example:
    change_profile(Content_type.AGE, uid, "UOFT") 
    will change the name of the user

    HINT: use the functions, e.g. update_user_gender(curosr, uid, new_gender)
    from use_case/dai.py
    """
    if content_type == Content_type.AGE:
        # TODO:
        pass
    elif content_type == Content_type.GENDER:
        # TODO
        pass
    # TODO: keep handling rest cases


def add_interest(uid, interest):

    """
    add the interest to the interes of the user with (uid)

    Return:
    bool: True on success, False otherwise.
    
    """
    # TODO: HINT: add_user_interest(uid, interest)
    cursor.execute(
        "INSERT INTO interest (user_id, interest) VALUES (?, ?)",
        (uid, interest)
    )
    connection.commit()
    return True

def get_interest(uid):
    """
    get a list of interes of the user with (uid)

    Return:
    List(str): interests of the user with uid
    """
    # TODO: HINT: use get_user_likes(uid)
    #return []
    try:
        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()
            # TODO: Implement the logic to retrieve user interests
            cursor.execute(
                "SELECT interest FROM interest WHERE user_id = ?",
                (uid,)
            )
            interests = [interest[0] for interest in cursor.fetchall()]
            return interests

    except sqlite3.Error as e:
        # print error message
        # change it to your own
        print(f"Not succuessful: {e}")
        return []

def delete_user(uid):
    """
    delete the user with (uid)

    Return:
    On success, return True
    else False
    """
    # TODO: HINT: use function remove_user_with_id(cursor, uid) from use_case/dai.py
    success = remove_user_with_id(uid)
    return success
def get_liked_users(uid):
    """
    get a list of users that User with (uid) liked

    Return: 
    List: (name, emails) of users that User with (uid) liked
    """
    # TODO: HINT: use get_user_likes(uid), but be careful you should return a list of ((name, emails))
    return get_user_likes(uid)

def get_unliked_users(uid):
    """
    get a list of users that User with (uid) unliked

    Return: 
    List: (name, emails) of users that User with (uid) unliked
    """

    return get_user_unlikes(uid)


def get_mutual_liked_users(uid):
    """
    get a list of users that User with (uid) liked and that also liked User with (uid)

    Return:
    List: (name, emails) of users that User with (uid) liked and that also liked User with (uid)
    """
    # TODO: HINT: use get_mutual_likes(uid), but be careful you should return a list of ((name, emails))
    return []
    pass



#  example code
#if __name__ == "__main__":
#    user_id = add_user('Pokemon', 'pk123@rotman.com', 'Male', 'Trt', 25)

get_interest(1)
