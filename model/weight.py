class Weight:
    def __init__(self):
        self.target = 0 # 20%
        self.aircraft_type = 0  # 25%
        self.pilot_skill = 0  # 25%
        self.weather_conditions = 0  # 20%
        self.execution_time = 0  # 10%

    def get_score(self):
        n25 = (self.aircraft_type + self.pilot_skill) * 0.25
        n20 = (self.weather_conditions + self.target) * 0.2
        n10 = self.execution_time * 0.1
        return n10 + n25 + n20

    # def get_target_score(self):

