
from model.location import Location


def convert_to_location_model(dict_w,location):
    location_d = dict_w
    return Location(
        location,
        location_d[0]["lat"],
        location_d[0]["lon"],
    )
