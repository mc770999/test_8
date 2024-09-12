from operator import itemgetter

from toolz.curried import partial

from model.data_sorce import Data_Source
from repository.json_repositori import read_json
from service.mission_service import create_missions
from service.pilot_service import convert_to_pilot_list_model
from service.location_service import convert_to_location_model
from service.target_service import create_list_targets
from service.weather_service import convert_to_weather_model
from service.aircraft_service import convert_to_aircraft_list_model
from toolz import pipe

if __name__ == "__main__":
    d = Data_Source()
    d.targets = create_list_targets(read_json( "repository/target.json"))
    d.pilots = convert_to_pilot_list_model(read_json("repository/pilots.json"))
    d.air_crafts = convert_to_aircraft_list_model(read_json("repository/aircrafts.json"))

    print(create_missions(d))

    # l = read_json("repository/city_data.json")
    # a = read_json("repository/location_api.json")
    # c = convert_to_weather_model(l["Damascus"],"Damascus")
    # print(c)
    # l1 = convert_to_location_model(a,"Damascus")
    # print(l1)
    # p = read_json("repository/pilots.json")
    # lp = convert_to_pilot_list_model(p)
    # print(lp[0])
    # h = read_json("repository/aircrafts.json")
    # print(convert_to_aircraft_list_model(h)[0])



