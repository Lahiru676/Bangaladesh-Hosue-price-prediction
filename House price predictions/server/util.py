import pickle
import json
import numpy as np

__city = ['faisalabad', 'islamabad', 'karachi', 'lahore', 'rawalpindi']
__data_columns = ["baths", "bedrooms", "area_in_marla", "faisalabad", "islamabad", "karachi", "lahore", "rawalpindi", "farm house", "flat", "house", "lower portion", "penthouse", "room", "upper portion"]
__model = None

def get_estimated_price(city,area_in_marla,bedrooms,baths):
    try:
        loc_index = __data_columns.index(city.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = area_in_marla
    x[1] = baths
    x[2] = bedrooms
    if loc_index>=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __city

    with open('server/artifacts/columns.json', "r") as f:
        __data_columns = json.load(f)['data_columns']
        __city = __data_columns[3:8]  # first 3 columns are sqft, bath, bhk

    global __model
    if __model is None:
        with open('server/artifacts/House_price_prediction.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    return __city

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('lahore',10, 3, 3))
    print(get_estimated_price('lahore', 20, 2, 2))
    print(get_estimated_price('islamabad', 10, 2, 2)) # other location
    print(get_estimated_price('faisalabad', 10, 2, 2))  # other location