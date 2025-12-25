from ridesharing.model.enums import RideType

class Vehicle:
    def __init__(self, model: str, license_number: str, ride_type: RideType):
        self.model = model
        self.license_number = license_number
        self.type = ride_type
