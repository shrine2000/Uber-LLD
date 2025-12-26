from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from ridesharing.model.trip import Trip


class User:
    def __init__(self, user_id: str, name: str, contact: str):
        self.id = user_id
        self.name = name
        self.contact = contact
        self.trip_history: List["Trip"] = []

    def add_trip_to_history(self, trip: "Trip") -> None:
        self.trip_history.append(trip)
