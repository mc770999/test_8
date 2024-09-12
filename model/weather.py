class Weather:
    def __init__(self, location, weather_main, clouds_all, wind_speed,date_time_text):
        self.location = location
        self.weather_main = weather_main
        self.clouds_all = clouds_all
        self.wind_speed = wind_speed
        self.date_time_text = date_time_text
    def __str__(self):
        return f"{self.location} : {self.weather_main}, on {self.date_time_text}"
