from random import random
import random

from model.weight import Weight
from utils.distance_helper import haversine_distance


# Generate a random float between 0 and 1


class Mission:
    def __init__(self,pilot,target,aircraft,score=0):

        self.start_lat = 31.79592425
        self.start_lon = 35.21198075969497
        self.name = pilot.name
        self.skill = pilot.skill

        self.target_city = target.target_city
        self.priority = target.priority
        self.let = target.location.let
        self.lon = target.location.lon

        self.weather_main = target.weather.weather_main
        self.clouds_all = target.weather.clouds_all
        self.wind_speed = target.weather.wind_speed
        self.date_time_text = target.weather.date_time_text


        self.type_craft = aircraft.type_craft
        self.speed = aircraft.speed
        self.fuel_capacity = aircraft.fuel_capacity

        self.score = self.get_score()


    def __str__(self):
        return f"{self.score}"

    def get_score(self):
        w = Weight()
        w.target = self.target_score()
        w.pilot_skill = self.pilot_skill_score()
        w.aircraft_type = self.aircraft_type_score()
        w.weather_conditions = self.weather_conditions_score()
        w.execution_time = self.execution_time_score()

        return w.get_score()

    def target_score(self):
        distance = haversine_distance(self.start_lat, self.start_lon, self.let, self.lon)

        return random.random()

    def aircraft_type_score(self):
        return random.random()
    def pilot_skill_score(self):

        return random.random()
    def weather_conditions_score(self):

        return random.random()
    def execution_time_score(self):
        return random.random()