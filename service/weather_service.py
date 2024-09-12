
from toolz import first,pipe

from model.weather import Weather


def convert_to_weather_model(dict_w,location):
    hour_list = dict_w["list"]
    the_corect_hour = pipe(
        hour_list,
        lambda l : filter(lambda i :  i["dt_txt"].endswith("00:00:00"), l),
        next
    )
    print(the_corect_hour)
    return Weather(
        location,
        the_corect_hour["weather"][0]["main"],
        the_corect_hour["clouds"]["all"],
        the_corect_hour["wind"]["speed"],
        the_corect_hour["dt_txt"]
    )
