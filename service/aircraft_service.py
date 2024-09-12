
from model.aircraft import Aircraft
from toolz import pipe

def convert_to_aircraft_list_model(dict_w):
    return [ Aircraft(
        p["type"],
        p["speed"],
        p["fuel_capacity"]
    ) for p in dict_w ]
