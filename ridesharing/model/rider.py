from typing import TYPE_CHECKING
from ridesharing.model.user import User
from ridesharing.observer.trip_observer import TripObserver

if TYPE_CHECKING:
    from ridesharing.model.trip import Trip


class Rider(User, TripObserver):
    def __init__(self, user_id: str, name: str, contact: str):
        super().__init__(user_id, name, contact)

    def on_update(self, trip: "Trip") -> None:
        print(
            f"Rider {self.name} notification: Trip {trip.id} status changed to {trip.status.name}"
        )
