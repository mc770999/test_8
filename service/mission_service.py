from toolz import compose,pipe
from toolz.curried import reduce

from model.data_sorce import Data_Source
from model.mission import Mission
from model.weight import Weight


def create_mission(pilot,target,aircraft):
    return Mission(pilot,target,aircraft)

def create_missions(data_sorce : Data_Source):
    missions = []
    for pilot in data_sorce.pilots:
        for air_craft in data_sorce.air_crafts:
            for target in data_sorce.targets:
                missions.append(create_mission(pilot,target,air_craft))


    return missions