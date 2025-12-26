from abc import ABC, abstractmethod
from typing import List
from ridesharing.model.driver import Driver
from ridesharing.model.location import Location
from ridesharing.model.enums import RideType, DriverStatus

class DriverMatchingStrategy(ABC):
    @abstractmethod
    def find_drivers(self, drivers: List[Driver], pickup: Location, ride_type: RideType) -> List[Driver]:
        pass

class NearestDriverMatchingStrategy(DriverMatchingStrategy):
    MAX_DISTANCE_KM = 5.0

    def find_drivers(self, drivers: List[Driver], pickup: Location, ride_type: RideType) -> List[Driver]:
        available_drivers = []
        for driver in drivers:
            if driver.status == DriverStatus.ONLINE and driver.vehicle.type == ride_type:
                if driver.current_location.distance_to(pickup) <= self.MAX_DISTANCE_KM:
                    available_drivers.append(driver)
        
        available_drivers.sort(key=lambda d: d.current_location.distance_to(pickup))
        return available_drivers
