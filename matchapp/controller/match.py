import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from use_case.dataManager import *
from sklearn.preprocessing import MinMaxScaler  # to normalize for scoring
import numpy as np

def haversine_distance(my_lat,my_long,lat,long):
    """
    Gives the shortest distance between two points on a sphere (Earth) in km
    :param my_lat: latitude of user
    :param my_long: longitude of user
    :param lat: latitude of potential match
    :param long: longitude of potential match
    :return: the distance in km
    """
    r = 6371 #earth radius in km
    lat1,long1 = np.radians(my_lat) , np.radians(my_long)
    lat2,long2 = np.radians(lat) , np.radians(long)

    d1 = np.sin((lat2-lat1)/2)**2 + np.cos(lat1)*np.cos(lat2)*np.sin((long2-long1)/2)**2
    d2 = 2*r*np.arcsin(np.sqrt(d1))
    return d2

def calculate_weights(uid):
    """
    Normalizes the weights (assigned by the user) to the importance of taste similarity, distance,
    and age similarity
    :param uid: user id of user
    :return: normalized weights alpha, beta, gamma (sum to 1)
    """
    weights = np.array[get_weights(uid)]
    weights = weights/np.sum(weights)
    return weights

## TODO temp ##
weights = np.array([0.4,0.4,0.2])
###

def find_match(uid):
    """
    Create a dataframe of people that could be potential matches with our user.
    Calculate the similarity in TV taste, the geographical distance, and the age difference.
    Produce overall scores and rank potential matches.

    :param uid: user id of user
    :return: on success, return the uid of the person we think the user will like best
    else: return -1
    """
    my_profile = get_user_info(uid)  # Get info of user to compare to other profiles
    print(my_profile)
    my_gender = my_profile[2]
    my_age = my_profile[4]

    yrs = 5  # Set minimum and maximum age range to look for
    my_min_age = my_age - yrs # For now, set preferred age range to +/- 5 years
    my_max_age = my_age + yrs

    rec = get_users(uid, my_gender, my_min_age, my_max_age) #get a table of matches along with their interests (from dataManager)

    if rec.empty: #if there are no potential matches
        return -1

    ### Calculating similarities ###
    # Age difference #
    rec['age dist'] = np.abs(my_age - rec['age'])  #age distance

    # Interests #
    my_interests = np.array(get_user_interest(uid)) #get an array of the user's interests
    my_total_interests = len(my_interests) #total number of interest for user

    rec['interest'] = rec['interest'].isin(my_interests) #turn interests into True/False if they are one of the user's interests
    users_total_interests = rec.groupby('uid')['interest'].transform('count')
    total_shared_interests = rec.groupby('uid')['interest'].transform('sum')
    union_of_interests = my_total_interests + users_total_interests - total_shared_interests
    rec['similarity'] = np.where(union_of_interests != 0, total_shared_interests / union_of_interests, 0) #Jaccard similarity: intersection divided by the union; 0 if union is 0

    rec.drop(['interest'], axis=1, inplace=True) #drop columns we don't need anymore
    rec.drop_duplicates(inplace=True) #now that the interests column is gone we'll have duplicate rows

    # Geographic distance #
    my_location = get_user_location(uid) # Get the location of user
    my_lat = my_location[1] #unpack latitude and longitude
    my_long = my_location[2]

    rec['geo_distance'] = haversine_distance(my_lat,my_long,rec['latitude'],rec['longitude']) #vectorized geographic distance calculation

    #Scale distance and similarity between 0 and 1

    scaler = MinMaxScaler()
    rec['normed_geo_distance'] = scaler.fit_transform(rec[['geo_distance']])
    rec['normed_similarity'] = scaler.fit_transform(rec[['similarity']])
    rec['normed_age_dist'] = scaler.fit_transform(rec[['age dist']])

    #Calculate total score for each user#
    alpha,beta,gamma = weights[0], weights[1], weights[2]
    rec['overall_score'] = alpha * rec['normed_similarity'] + beta * (1-rec['normed_geo_distance']) + gamma * (1-rec['normed_age_dist'])

    #Like/Dislike Penalty#
    rec['like'] = rec['like'].map({1.0: 1, np.nan: 0, 0.0:-1}) #change like, dislike, and Null to 1, -1, 0
    penalty = rec['like']*0.2
    rec['overall_score'] += penalty  #if the user has already liked them, add 0.2 to their score. If they have disliked, subtract 0.2

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

#  example code
#if __name__ == "__main__":
    #print(find_match(2))