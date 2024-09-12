
from model.pilot import Pilot
from toolz import pipe

def convert_to_pilot_list_model(dict_w):
    return [ Pilot(
        p["name"],
        p["skill"]
    ) for p in dict_w ]
