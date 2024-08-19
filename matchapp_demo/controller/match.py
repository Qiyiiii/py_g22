import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from use_case.dataManager import *
from geopy.geocoders  import Nominatim# for distances
from geopy.distance import geodesic  # for distances
from sklearn.preprocessing import MinMaxScaler  # to normalize for scoring
import numpy as np
import ssl
import certifi

def find_match(uid):
    """
    IMPORTANT: core algorithm of this project

    find a match for the User with (uid)

    Return:
    on success, return the uid of user that matched with the current u ser
    else: return -1
    """
    ctx = ssl.create_default_context(cafile=certifi.where())
    nomi= Nominatim(user_agent="my_geocoding_app", ssl_context=ctx)

    #Get info about the user to compare to other profiles
    my_profile = get_user_info(uid)
    my_age = my_profile[4]
    my_postal_code = my_profile[3]
    my_location = nomi.geocode(my_postal_code)
    my_interests = get_user_interest(uid)
    my_lat_long = (my_location.latitude, my_location.longitude)

    rec = get_users(uid) #get the table of potential matches
    if rec.empty:
        return -1

    #Filter out based on age
    yrs = 5 # Set preferred age range to +/- 5 years
    min_age = my_age - yrs
    max_age = my_age + yrs
    rec = rec[(rec.age >= min_age) & (rec.age <= max_age)] #Filter out people outside that age range
    rec['age dist'] = np.abs(my_age - rec['age'])

    #Find common interets
    rec['shared_interest'] = (rec.interest.isin(my_interests)).astype(int) #create new column called "shared interest" with value of 0 or 1
    my_total_interests = len(my_interests)
    union_of_interests = rec.groupby('uid')['interest'].transform('count') + my_total_interests

    rec['similarity'] = rec.groupby('uid')['shared_interest'].transform('sum')/(union_of_interests)
    rec.loc[union_of_interests == 0, 'similarity'] = 0

    rec.drop(['interest', 'shared_interest'], axis=1, inplace=True)
    rec.drop_duplicates(inplace=True)

    if rec.empty:
        return -1

## Old version ##
    #Calculate geographical distance
    def geo_distance(row):
        try:
            postal_code = row['location']
            location = nomi.geocode(postal_code +', United States')
            lat_long = (location.latitude, location.longitude)
            distance = geodesic(my_lat_long, lat_long).kilometers
        except Exception:
            distance = 1000 #TODO: This is a temporary way of dealing with invalid postal codes in the DB
        return distance

    rec['geo_distance'] = rec.apply(geo_distance, axis=1)

    #Scale distance and similarity between 0 and 1
    scaler = MinMaxScaler()
    rec['normed_geo_distance'] = scaler.fit_transform(rec[['geo_distance']])
    rec['normed_similarity'] = scaler.fit_transform(rec[['similarity']])
    rec['normed_age_dist'] = scaler.fit_transform(rec[['age dist']])

    #Calculate total score for each user
    def overall_score(row):
        alpha, beta, gamma = 0.4, 0.4, 0.2
        score = alpha * row['normed_similarity'] + beta * (1-row['normed_geo_distance']) + gamma * (1-row['normed_age_dist'])
        return score

    rec['overall_score'] = rec.apply(overall_score, axis=1)

    #Put them in order of high score to low score
    rec.sort_values('overall_score', ascending=False, inplace=True)
    rec = rec.reset_index()
    our_pick = rec.iloc[0]['uid']

    return int(our_pick)

def like_user(uid1, uid2):
    """
    add action that User with uid1 liked the User with uid2

    Return:
    bool: True on success, False otherwise.
    """
    add_action(uid1, uid2, 'like')

def unlike_user(uid1, uid2):
    """
    add action that User with uid1 unliked the User with uid2

    Return:
    bool: True on success, False otherwise.
    """
    add_action(uid1, uid2, 'dislike')

# def get_scores(uid):
#     """
#     get scores of other users to the user with (uid)

#     Return:
#     List: list of (score and userid)
#     """
#     # TODO: 

# def get_score(uid1, uid2):
#     """
#     get scores between user with uid1 and user with uid2

#     Return:
#     int: score of two users
#     """
#     # TODO: 


# def get_top_5_user(uid):
#     """
#     return (uid, score) of top 5 users that mutually liked by user with uid

#     Return:
#     List: (uid, score) of users with top 5 scores 
#     """
#     # TODO: return the list of top 5 users
#     return []

#  example code
if __name__ == "__main__":
    print(find_match(31))
