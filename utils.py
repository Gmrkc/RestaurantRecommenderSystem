import random
import pandas as pd
import numpy as np

# Furkan Gümrükçü 171805057

def create_new_df(unique_cuisine_list, unique_payment_list, unique_smoker_list, unique_ambience_list, unique_transport_list, unique_marital_status_list, unique_job_list, unique_budget_list):

    user_id = 1
    place_id = 1
    user_id_list = []
    place_id_list = []
    new_df = pd.DataFrame()
    unique_rating_list = [1,2,3,4,5]

    for i in range(200000):

        if user_id > 1000:
            temp_user_id = random.choices(user_id_list, k=1)
            user_id = temp_user_id[0]
        if place_id > 1000:
            temp_place_id = random.choices(place_id_list, k=1)
            place_id = temp_place_id[0]
        ambience = random.choices(unique_ambience_list, weights = (882,2427,0,754), k = 1)
        transport = random.choices(unique_transport_list, weights = (1627,0,634,1803), k = 1)
        rating = random.choices(unique_rating_list, weights = (1808,1000,1024,1000,1258), k = 1)

        row = {
            'userId': user_id,
            'placeId': place_id,
            'rating': rating[0],
            'cuisine': "",
            'payment': "",
            'smoker': "",
            'ambience': ambience[0][0],
            'transport': transport[0][0],
            'marital_status': "",
            'job': "",
            'budget': "" 
        }

        if user_id < 1000:
            user_id_list.append(user_id)
        user_id += 1
        if place_id < 1000:
            place_id_list.append(place_id)
        place_id += 1
        new_df = new_df.append(row, ignore_index = True)
        print(i, end='\r')
   
    for i in range(1, 200001, 1):
            cuisine = random.choices(unique_cuisine_list, weights = (14,113,999,14,34,33,26,14,14,14,14,14,24,14,14,44,14,14,14,27,50,14,71,14,14,24,14,14,78,14,14,70,27,14,30,23,14,120,106,24,14,14,18,14,77,40,27,27,14,14,14,27,98,27,14,14,14,14,18,14,24,14,81,14,23,14,14,50,14,55,14,14,44,14,14,27,14,35,14,14,44,24,14,30,37,14,41,14,27,14,14,107,78,14,14,14,63,133,24,77,14,14,28), k=1)
            smoker = random.choices(unique_smoker_list, weights = (3787,303), k = 1)
            payment = random.choices(unique_payment_list, weights = (217,300,204,17,3352), k = 1)
            marital_status = random.choices(unique_marital_status_list, weights = (31,131,3919,0), k = 1)
            job = random.choices(unique_job_list, weights = (8,3655,385,0,17), k = 1)
            budget = random.choices(unique_budget_list, weights = (2012,86,1954,0), k = 1)

            new_df.loc[new_df['placeId'] == i, 'cuisine'] = cuisine[0][0]
            new_df.loc[new_df['placeId'] == i, 'payment'] = payment[0][0]
            new_df.loc[new_df['userId'] == i, 'smoker'] = smoker[0][0]
            new_df.loc[new_df['userId'] == i, 'marital_status'] = marital_status[0][0]
            new_df.loc[new_df['userId'] == i, 'job'] = job[0][0]
            new_df.loc[new_df['userId'] == i, 'budget'] = budget[0][0]
            print(i, end='\r')
                        
    new_df = new_df.sort_values('userId')
    new_df.to_csv("my_restaurant_dataset4.csv",index=False)

