class Location:
    def __init__(self,location,let,lon):
        self.location = location
        self.let = let
        self.lon = lon

    def __str__(self):
        return f"{self.location} : let : {self.let}, lon : {self.lon} "