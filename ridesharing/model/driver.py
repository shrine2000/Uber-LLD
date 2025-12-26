from typing import TYPE_CHECKING
from ridesharing.model.user import User
from ridesharing.observer.trip_observer import TripObserver
from ridesharing.model.vehicle import Vehicle
from ridesharing.model.location import Location
from ridesharing.model.enums import DriverStatus

if TYPE_CHECKING:
    from ridesharing.model.trip import Trip


class Driver(User, TripObserver):
    def __init__(
        self,
        user_id: str,
        name: str,
        contact: str,
        vehicle: Vehicle,
        current_location: Location,
    ):
        super().__init__(user_id, name, contact)
        self.vehicle = vehicle
        self.current_location = current_location
        self.status = DriverStatus.ONLINE

    def on_update(self, trip: "Trip") -> None:
        print(
            f"Driver {self.name} notification: Trip {trip.id} status changed to {trip.status.name}"
        )
