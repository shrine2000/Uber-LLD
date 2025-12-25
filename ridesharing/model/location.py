import math

class Location:
    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude

    def distance_to(self, other: 'Location') -> float:
        return math.sqrt(math.pow(self.latitude - other.latitude, 2) + 
                         math.pow(self.longitude - other.longitude, 2))
