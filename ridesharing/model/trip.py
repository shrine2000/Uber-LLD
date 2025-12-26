from typing import List, Optional
from ridesharing.model.location import Location
from ridesharing.model.rider import Rider
from ridesharing.model.driver import Driver
from ridesharing.model.enums import TripStatus, RideType
from ridesharing.observer.trip_observer import TripObserver


class Trip:
    def __init__(
        self,
        trip_id: str,
        rider: Rider,
        pickup: Location,
        dropoff: Location,
        ride_type: RideType,
    ):
        self.id = trip_id
        self.rider = rider
        self.pickup = pickup
        self.dropoff = dropoff
        self.ride_type = ride_type
        self.driver: Optional[Driver] = None
        self.status = TripStatus.REQUESTED
        self.fare: float = 0.0
        self.observers: List[TripObserver] = []

        self.add_observer(rider)

    def add_observer(self, observer: TripObserver) -> None:
        if observer not in self.observers:
            self.observers.append(observer)

    def remove_observer(self, observer: TripObserver) -> None:
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self.observers:
            observer.on_update(self)

    def assign_driver(self, driver: Driver) -> None:
        self.driver = driver
        self.status = TripStatus.ASSIGNED
        self.add_observer(driver)
        self.notify_observers()

    def start_trip(self) -> None:
        if self.status == TripStatus.ASSIGNED:
            self.status = TripStatus.IN_PROGRESS
            self.notify_observers()

    def complete_trip(self, fare: float) -> None:
        if self.status == TripStatus.IN_PROGRESS:
            self.status = TripStatus.COMPLETED
            self.fare = fare
            self.notify_observers()

            self.rider.add_trip_to_history(self)
            if self.driver:
                self.driver.add_trip_to_history(self)

    def cancel_trip(self) -> None:
        if self.status in [TripStatus.REQUESTED, TripStatus.ASSIGNED]:
            self.status = TripStatus.CANCELLED
            self.notify_observers()
