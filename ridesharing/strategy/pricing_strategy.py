from abc import ABC, abstractmethod
from ridesharing.model.location import Location
from ridesharing.model.enums import RideType

class PricingStrategy(ABC):
    @abstractmethod
    def calculate_fare(self, pickup: Location, dropoff: Location, ride_type: RideType) -> float:
        pass

class FlatRatePricingStrategy(PricingStrategy):
    FLAT_RATE = 20.0
    BASE_FARE = 5.0

    def calculate_fare(self, pickup: Location, dropoff: Location, ride_type: RideType) -> float:
        return self.BASE_FARE + self.FLAT_RATE

class VehicleBasedPricingStrategy(PricingStrategy):
    BASE_FARE = 5.0
    RATE_PER_KM = {
        RideType.SUV: 15.0,
        RideType.SEDAN: 10.0,
        RideType.AUTO: 5.0
    }

    def calculate_fare(self, pickup: Location, dropoff: Location, ride_type: RideType) -> float:
        distance = pickup.distance_to(dropoff)
        rate = self.RATE_PER_KM.get(ride_type, 10.0)
        return self.BASE_FARE + (distance * rate)
