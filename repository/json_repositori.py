import json

#from model.aircraft import Warrior



def read_json(path):
    try:
        with open(path, "r",encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print("json",e)
        return []

