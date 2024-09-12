from operator import itemgetter

from toolz import first
from repository.json_repositori import read_json
from api.weather_api import get_weather_from_api
from api.weather_api import get_location_from_api
from service.location_service import convert_to_location_model
from toolz.curried import partial, get_in, pipe
from model.target_model import Target
from service.weather_service import convert_to_weather_model

def get_data(json):
    city = itemgetter("Target City")(json)
    location = pipe(
        city,
        get_location_from_api,
        lambda data: convert_to_location_model(data, city)
    )
    weather = pipe(
        city,
        get_weather_from_api,
        lambda data: convert_to_weather_model(data, city)
    )
    return Target(target_city=city, priority=json["Priority"],weather=weather, location=location)

def create_list_targets(json_list):
    return pipe(json_list,partial(map, get_data),list)


