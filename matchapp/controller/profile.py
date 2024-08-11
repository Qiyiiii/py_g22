import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from use_case.dai import *



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
    # TODO: HINT: use get_user_info(uid) from dai.py
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

def delete_user(uid):
    """
    delete the user with (uid)

    Return:
    On success, return True
    else False
    """
    # TODO: HINT: use function remove_user_with_id(cursor, uid) from use_case/dai.py
    pass
def get_liked_users(uid):
    """
    get a list of people that User with (uid) liked

    Return: 
    List: people that User with (uid) liked
    """
    # TODO: HINT: use get_user_likes(uid)
    pass

def get_liked_users(uid):
    """
    get a list of people that User with (uid) unliked

    Return: 
    List: people that User with (uid) unliked
    """
    # TODO: HINT: use get_user_unlikes(uid)
    pass
def get_mutual_liked_users(uid):
    """
    get a list of people that User with (uid) liked and that also liked User with (uid)

    Return:
    List: people that User with (uid) liked and that also liked User with (uid)
    """
    # TODO: HINT: use get_mutual_likes(uid):
    pass


#  example code
if __name__ == "__main__":
    user_id = add_user('Pokemon', 'pk123@rotman.com', 'Male', 'Trt', 25)


