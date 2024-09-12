import requests

def get_date_from_api(url):
    response = requests.request("GET",url)
    return response.json()

def get_location_from_api(city):
    return get_date_from_api(f"https://api.openweathermap.org/geo/1.0/direct?q={city}&appid=5d06f90c326d9c6fcad20324c803ec76")

def get_weather_from_api(city):
    return get_date_from_api(f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid=5d06f90c326d9c6fcad20324c803ec76")