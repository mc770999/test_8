
class Target:
    def __init__(self,target_city,priority, location=None, weather=None):
        self.target_city = target_city
        self.priority = priority
        self.location = location
        self.weather = weather
    def __str__(self):
        return f"{self.target_city} {self.priority}"