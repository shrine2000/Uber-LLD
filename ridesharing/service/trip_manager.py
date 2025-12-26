from typing import List, Optional
import uuid
from ridesharing.model.trip import Trip
from ridesharing.model.rider import Rider
from ridesharing.model.driver import Driver
from ridesharing.model.location import Location
from ridesharing.model.enums import RideType, DriverStatus
from ridesharing.strategy.pricing_strategy import (
    PricingStrategy,
    VehicleBasedPricingStrategy,
)
from ridesharing.strategy.driver_matching_strategy import (
    DriverMatchingStrategy,
    NearestDriverMatchingStrategy,
)


class TripManager:
    """Singleton class to manage all trips in the system."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TripManager, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return

        self._initialized = True
        self.trips: List[Trip] = []
        self.drivers: List[Driver] = []
        self.pricing_strategy: PricingStrategy = VehicleBasedPricingStrategy()
        self.matching_strategy: DriverMatchingStrategy = NearestDriverMatchingStrategy()

    def set_pricing_strategy(self, strategy: PricingStrategy) -> None:
        self.pricing_strategy = strategy

    def set_matching_strategy(self, strategy: DriverMatchingStrategy) -> None:
        self.matching_strategy = strategy

    def register_driver(self, driver: Driver) -> None:
        if driver not in self.drivers:
            self.drivers.append(driver)

    def request_trip(
        self, rider: Rider, pickup: Location, dropoff: Location, ride_type: RideType
    ) -> Optional[Trip]:
        trip_id = str(uuid.uuid4())
        trip = Trip(trip_id, rider, pickup, dropoff, ride_type)

        available_drivers = self.matching_strategy.find_drivers(
            self.drivers, pickup, ride_type
        )

        if not available_drivers:
            print(f"No drivers available for trip {trip_id}")
            trip.cancel_trip()
            return None

        driver = available_drivers[0]
        driver.status = DriverStatus.IN_TRIP
        trip.assign_driver(driver)

        fare = self.pricing_strategy.calculate_fare(pickup, dropoff, ride_type)
        trip.fare = fare

        self.trips.append(trip)
        print(
            f"Trip {trip_id} created and assigned to driver {driver.name} with fare ${fare:.2f}"
        )

        return trip

    def start_trip(self, trip_id: str) -> bool:
        trip = self._find_trip_by_id(trip_id)
        if trip:
            trip.start_trip()
            return True
        return False

    def complete_trip(self, trip_id: str) -> bool:
        trip = self._find_trip_by_id(trip_id)
        if trip:
            trip.complete_trip(trip.fare)
            if trip.driver:
                trip.driver.status = DriverStatus.ONLINE
            return True
        return False

    def cancel_trip(self, trip_id: str) -> bool:
        trip = self._find_trip_by_id(trip_id)
        if trip:
            trip.cancel_trip()
            if trip.driver:
                trip.driver.status = DriverStatus.ONLINE
            return True
        return False

    def _find_trip_by_id(self, trip_id: str) -> Optional[Trip]:
        for trip in self.trips:
            if trip.id == trip_id:
                return trip
        return None

    def get_trip_history(self, user_id: str) -> List[Trip]:
        return [
            trip
            for trip in self.trips
            if trip.rider.id == user_id or (trip.driver and trip.driver.id == user_id)
        ]
