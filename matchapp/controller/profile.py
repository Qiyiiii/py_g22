import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from use_case.dataManager import *
from geopy.geocoders import Nominatim
import ssl
import certifi

from enum import Enum
class Content_type(Enum):
    NAME = 1
    GENDER = 2
    LOCATION = 3
    AGE = 4

class Preferences_type(Enum):
    SIM_WEIGHT = 1
    LOC_WEIGHT = 2
    AGE_WEIGHT = 3


def geocode_location(location):
    """
    Find the latitude and longitude of a U.S. Zip Code

    Return
    On success, return latitude, longitude coordinates
    else -1
    """
    ctx = ssl.create_default_context(cafile=certifi.where()) #set up for geopy API...
    nomi = Nominatim(user_agent="my_geocoding_app", ssl_context=ctx)

    try:
        found_location = nomi.geocode(location + ', United States') #finds the location of a U.S. Zip code
        latitude, longitude = (found_location.latitude, found_location.longitude) #collects latitude and longitude
    except Exception:
        return -1

    return latitude, longitude

def add_user(name, email, gender, location, age, interests=[]):
    """
    add User with name, email, gender, location, age into databse

    Return:
    On success, return uid of the user created
    else -1
    """
    location_result = geocode_location(location)
    if location_result != -1:
        latitude,longitude = location_result
        uid = create_user(name, email, gender, age, location, latitude, longitude, interests)
        return uid if uid > 0 else -1

    else:
        return -1

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
    if content_type == Content_type.NAME:
        return update_user_name(uid, content)
    elif content_type == Content_type.GENDER:
        return update_user_gender(uid, content)
    elif content_type == Content_type.LOCATION:
        location_result = geocode_location(content)
        if location_result != -1:
            new_latitude, new_longitude = location_result
            return update_user_location(uid, content, new_latitude, new_longitude)
        else:
            return -1
    elif content_type == Content_type.AGE:
        return update_user_age(uid, content)
    else:
        return False  # If an unsupported content type is passed


def user_weights(uid):
    """
    Get the preferences of User with (uid).
    The weights indicate relative importance (integers 1-10) assigned to TV similarity,
    geographic distance, and age similarity.

    Return:
    Tuple: (sim_weight, loc_weight, age_weight) for User (uid)
    """
    return get_user_weights(uid)

def change_weights(Preferences_type, uid, new_weight):
    """
    Based on the type of content, change the preferences of User with (uid).
    The weights indicate relative importance (integers 1-10) assigned to TV similarity,
    geographic distance, and age similarity.

    Return:
    bool: True on success, False otherwise.
    """
    if Preferences_type == Preferences_type.SIM_WEIGHT:
        return update_sim_weight(uid, new_weight)
    elif Preferences_type == Preferences_type.LOC_WEIGHT:
        return update_loc_weight(uid, new_weight)
    elif Preferences_type == Preferences_type.AGE_WEIGHT:
        return update_age_weight(uid, new_weight)
    return False

def add_interest(uid, interest):
    """
    add the interest to the interes of the user with (uid)

    Return:
    bool: True on success, False otherwise.
    
    """
    # Attempt to add the interest and store the result

    return add_user_interest(uid, interest)
 


def get_interest(uid):
    """
    get a list of interes of the user with (uid)

    Return:
    List(str): interests of the user with uid
    """
    return get_user_interest(uid)

def delete_user(uid):
    """
    delete the user with (uid)

    Return:
    On success, return True
    else False
    """
    return remove_user_with_id(uid)
def get_liked_users(uid):
    """
    get a list of users that User with (uid) liked

    Return: 
    List: (name, emails) of users that User with (uid) liked
    """
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
    return get_mutual_likes(uid)




# #  example code
# if __name__ == "__main__":
#     add_interest(2, "hello")

#     print(get_interest(2))
