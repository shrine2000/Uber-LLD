from abc import ABC, abstractmethod

class TripObserver(ABC):
    @abstractmethod
    def on_update(self, trip) -> None:
        pass
