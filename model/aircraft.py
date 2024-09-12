class Aircraft:
    def __init__(self, type_craft, speed, fuel_capacity):
        self.type_craft = type_craft
        self.speed = speed
        self.fuel_capacity = fuel_capacity
    def __str__(self):
        return f"Type: {self.type_craft}, Speed: {self.speed}, Fuel Capacity: {self.fuel_capacity}"


