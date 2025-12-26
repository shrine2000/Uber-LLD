from enum import Enum, auto


class RideType(Enum):
    SUV = auto()
    SEDAN = auto()
    AUTO = auto()


class DriverStatus(Enum):
    IN_TRIP = auto()
    OFFLINE = auto()
    ONLINE = auto()


class TripStatus(Enum):
    COMPLETED = auto()
    ASSIGNED = auto()
    REQUESTED = auto()
    IN_PROGRESS = auto()
    CANCELLED = auto()
