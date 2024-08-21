import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controller.profile import *
import numpy as np

## Run schema.sql first ##

interests_list =  np.array(["Action & Adventure", "Comedy", "Documentary", "Drama", "Horror", "Lifestyle & Entertainment", "Reality TV", "Science Fiction & Fantasy", "Thriller & True Crime", "Historical & Period Drama", "Animated"])
manhattan_postal_codes = np.array([
    "10001", "10002", "10003", "10004", "10005", "10006", "10007", "10009", "10010", "10011",
    "10012", "10013", "10014", "10016", "10017", "10018", "10019", "10020", "10021", "10022",
    "10023", "10024", "10025", "10026", "10027", "10028", "10029", "10030", "10031", "10032",
    "10033", "10034", "10035", "10036", "10037", "10038", "10039", "10040", "10041", "10044",
    "10045", "10048", "10055", "10069", "10090", "10103", "10104", "10105", "10106", "10107",
    "10110", "10111", "10112", "10115", "10118", "10119", "10120", "10121", "10122", "10123",
    "10128", "10152", "10153", "10154", "10155", "10158", "10162", "10165", "10166", "10167",
    "10168", "10169", "10170", "10171", "10172", "10173", "10174", "10175", "10176", "10177",
    "10178", "10199", "10271", "10278", "10279", "10280", "10281", "10282"
])

female_names = np.array([
    "Aisha", "Ava", "Beatrice", "Carmen", "Chiara", "Daphne", "Elena", "Emma",
    "Fatima", "Freya", "Giselle", "Hana", "Imani", "Isabella", "Jada", "Kaia",
    "Lara", "Layla", "Mei", "Mia", "Nia", "Noor", "Priya", "Rosa", "Sanaa",
    "Sofia", "Tara", "Yasmin", "Zainab", "Zoe", "Amara", "Elise", "Ivy",
    "Jasmine", "Kira", "Maya", "Naomi", "Olivia", "Pia", "Quinn", "Riley",
    "Serena", "Talia", "Violet", "Willow", "Zara"
])

# Expanded list of male names
male_names = np.array([
    "Aiden", "Amir", "Carlos", "Darius", "Elijah", "Ethan", "Hassan", "Isaac",
    "Jamal", "Javier", "Kai", "Liam", "Luca", "Mateo", "Nicolas", "Omar",
    "Ravi", "Ruben", "Samir", "Santiago", "Sebastian", "Tariq", "Theo", "Tyler",
    "Umar", "Victor", "William", "Xavier", "Yusuf", "Zachary", "Zain", "Adam",
    "Ben", "Cyrus", "David", "Eli", "Felix", "Graham", "Henry", "Ivan",
    "Jonah", "Khalil", "Lorenzo", "Milo", "Nathan", "Owen", "Paul", "Quentin",
    "Rafael", "Simon", "Tomas", "Uriel"
])

email_domain = np.array(['@gmail.com','@yahoo.com','@hotmail.com'])

def random_profiles(idx):
    name = np.random.choice(female_names)
    email = name + str(idx) + np.random.choice(email_domain)
    num_to_select = np.random.randint(1, 6)
    location = np.random.choice(manhattan_postal_codes)
    age = np.random.randint(18, 31)
    interests = np.random.choice(interests_list, size=num_to_select, replace=False)
    add_user(name, email, 'Female', location, age, interests=interests) #insert a female user; odd uids

    name = np.random.choice(male_names)
    email = name + str(idx) + np.random.choice(email_domain)
    num_to_select = np.random.randint(1, 6)
    location = np.random.choice(manhattan_postal_codes)
    age = np.random.randint(18, 31)
    interests = np.random.choice(interests_list, size=num_to_select, replace=False)
    add_user(name, email, 'Male', location, age, interests=interests) #insert a male user; even uids

num=20

for i in range(num):
    idx= i+1
    random_profiles(idx)

actions = np.array(['like','dislike'])
uids = np.arange(1,2*(num+1))
odd_uids = uids[uids % 2 !=0]
even_uids = uids[uids % 2 ==0]

def random_likes():
    uid1 = int(np.random.choice(odd_uids))
    uid2 = int(np.random.choice(even_uids))
    action = np.random.choice(actions)
    add_action(uid1, uid2, action)
    uid1 = int(np.random.choice(even_uids))
    uid2 = int(np.random.choice(odd_uids))
    action = np.random.choice(actions)
    add_action(uid1, uid2, action)

for i in range(60):
    random_likes()