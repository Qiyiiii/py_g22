import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from use_case.dataManager import *
#import pgeocode  # for distances
#from geopy.distance import geodesic  # for distances
#from sklearn.preprocessing import MinMaxScaler  # to normalize for scoring
##

def find_match(uid):
    """
    IMPORTANT: core algorithm of this project

    find a match for the User with (uid)

    Return:
    on success, return the uid of user that matched with the current user
    else: return -1
    """
    nomi = pgeocode.Nominatim('ca')

    #Get info about the user to compare to other profiles
    my_profile = get_user_info(uid)
    my_age = my_profile[4]
    my_postal_code = my_profile[3]
    my_location = nomi.query_postal_code(my_postal_code)
    my_interests = get_user_interest(uid)

    my_lat_long = (my_location.latitude, my_location.longitude)

    rec = get_users(uid) #get the table of potential matches

    #Filter out based on age
    yrs = 5 # Set preferred age range to +/- 5 years
    min_age = my_age - yrs
    max_age = my_age + yrs
    rec = rec[(rec.age >= min_age) & (rec.age <= max_age)] #Filter out people outside that age range

    #Find common interets
    rec['shared_interest'] = (rec.interest.isin(my_interests)).astype(int) #create new column called "shared interest" with value of 0 or 1
    rec['similarity'] = rec.groupby('uid')['shared_interest'].transform('sum')
    #TODO: Jaccard similarity
    rec.drop(['interest', 'shared_interest'], axis=1, inplace=True)
    rec.drop_duplicates(inplace=True)

    #Calculate geographical distance
    def geo_distance(row):
        try:
            postal_code = row['location']
            location = nomi.query_postal_code(postal_code)
            lat_long = (location.latitude, location.longitude)
            distance = geodesic(my_lat_long, lat_long).kilometers
        except ValueError:
            distance = 1000 #TODO: This is a temporary way of dealing with invalid postal codes in the DB
        return distance

    rec['geo_distance'] = rec.apply(geo_distance, axis=1)

    #Scale distance and similarity between 0 and 1
    scaler_geo_distance = MinMaxScaler()
    rec['normed_geo_distance'] = scaler_geo_distance.fit_transform(rec[['geo_distance']])
    scaler_similarity = MinMaxScaler()
    rec['normed_similarity'] = scaler_similarity.fit_transform(rec[['similarity']])

    #TODO: Age similarity

    #Calculate total score for each user
    def overall_score(row):
        alpha, beta = 0.5, 0.5
        score = alpha * row['normed_similarity'] - beta * row['normed_geo_distance']
        return score

    rec['overall_score'] = rec.apply(overall_score, axis=1)

    #Put them in order of high score to low score
    rec.sort_values('overall_score', ascending=False, inplace=True)
    rec = rec.reset_index()
    our_pick = rec.iloc[0]['uid']

    return our_pick



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

