class Mission:
    def __init__(self,pilot,target=None,aircraft=None,score=0):
        self.pilot = pilot
        self.target = target
        self.aircraft = aircraft
        self.score = score
    def __str__(self):
        return f"{self.pilot} {self.target} {self.score}"