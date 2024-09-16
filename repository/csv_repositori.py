import csv
from typing import List
from model.mission import Mission
from toolz import  pipe, partial

def write_missions_to_csv(missions: List[Mission], filepath: str):
    # self.start_lat = 31.79592425
    # self.start_lon = 35.21198075969497
    # self.name = pilot.name
    # self.skill = pilot.skill
    #
    # self.target_city = target.target_city
    # self.priority = target.priority
    # self.let = target.location.let
    # self.lon = target.location.lon
    #
    # self.weather_main = target.weather.weather_main
    # self.clouds_all = target.weather.clouds_all
    # self.wind_speed = target.weather.wind_speed
    # self.date_time_text = target.weather.date_time_text
    #
    # self.type_craft = aircraft.type_craft
    # self.speed = aircraft.speed
    # self.fuel_capacity = aircraft.fuel_capacity
    #
    # self.score = self.get_score()
    try:
        with open(filepath, 'w', newline='') as csvfile:
            csv_writer = csv.DictWriter(csvfile, fieldnames=["start_lat","start_lon","name","skill","target_city","priority","let","lon","weather_main","clouds_all","wind_speed","date_time_text","type_craft","speed","fuel_capacity","score"])
            csv_writer.writeheader()
            for mission in missions:
                csv_writer.writerow({
                    'start_lat': mission.start_lat,
                    'start_lon': mission.start_lon,
                    'name': mission.name,
                    'skill': mission.skill,
                    'target_city': mission.target_city,
                    'priority': mission.priority,
                    'let': mission.let,
                    'lon': mission.lon,
                    'weather_main': mission.weather_main,
                    'clouds_all': mission.clouds_all,
                    'wind_speed': mission.wind_speed,
                    'date_time_text': mission.date_time_text,
                    'type_craft': mission.type_craft,
                    'speed': mission.speed,
                    'fuel_capacity': mission.fuel_capacity,
                    'score': mission.score,

                })
    except Exception as e:
        print(e)