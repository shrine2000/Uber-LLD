# Ridesharing Service - Low Level Design Implementation

A complete Python implementation of a ridesharing service (like Uber) based on object-oriented design principles.

## 📁 Project Structure

```
Uber-LLD/
├── ridesharing/
│   ├── __init__.py
│   ├── model/
│   │   ├── __init__.py
│   │   ├── enums.py           # Enumerations (RideType, DriverStatus, TripStatus)
│   │   ├── location.py        # Location class with distance calculation
│   │   ├── vehicle.py         # Vehicle class
│   │   ├── user.py            # Base User class
│   │   ├── rider.py           # Rider class (extends User, implements Observer)
│   │   ├── driver.py          # Driver class (extends User, implements Observer)
│   │   └── trip.py            # Trip class with Observer pattern
│   ├── observer/
│   │   ├── __init__.py
│   │   └── trip_observer.py   # TripObserver interface
│   ├── strategy/
│   │   ├── __init__.py
│   │   ├── pricing_strategy.py         # Pricing strategies
│   │   └── driver_matching_strategy.py # Driver matching strategies
│   └── service/
│       ├── __init__.py
│       └── trip_manager.py    # TripManager singleton
├── main.py                    # Demo application
└── README.md
```

## 🎯 Design Patterns Used

1. **Observer Pattern**: Trip status updates notify riders and drivers
2. **Strategy Pattern**: 
   - Pricing strategies (Flat Rate, Vehicle-based)
   - Driver matching strategies (Nearest driver)
3. **Singleton Pattern**: TripManager ensures single instance

## 🚀 Features

- **User Management**: Riders and Drivers with contact information
- **Vehicle Types**: SUV, SEDAN, AUTO
- **Trip Lifecycle**: Request → Assign → In Progress → Complete/Cancel
- **Real-time Notifications**: Observer pattern for status updates
- **Flexible Pricing**: Pluggable pricing strategies
- **Smart Matching**: Driver matching based on location and vehicle type
- **Trip History**: Track completed trips for users

## 📊 Class Diagram Components

### Enums
- `RideType`: SUV, SEDAN, AUTO
- `DriverStatus`: IN_TRIP, OFFLINE, ONLINE
- `TripStatus`: COMPLETED, ASSIGNED, REQUESTED, IN_PROGRESS, CANCELLED

### Core Classes
- `Location`: GPS coordinates with distance calculation
- `Vehicle`: Model, license number, and ride type
- `User`: Base class for Rider and Driver
- `Rider`: User who requests trips
- `Driver`: User who provides trips
- `Trip`: Represents a ride with observer notifications

### Design Pattern Classes
- `TripObserver`: Interface for trip status notifications
- `PricingStrategy`: Interface for fare calculation
- `DriverMatchingStrategy`: Interface for finding available drivers
- `TripManager`: Singleton service managing all trips

## 🏃 Running the Demo

```bash
python main.py
```

## 💡 Usage Example

```python
from ridesharing.service.trip_manager import TripManager
from ridesharing.model.rider import Rider
from ridesharing.model.location import Location
from ridesharing.model.enums import RideType

# Get TripManager instance
trip_manager = TripManager()

# Create a rider
rider = Rider("R001", "Alice", "+1-555-0101")

# Request a trip
pickup = Location(37.7749, -122.4194)
dropoff = Location(37.8049, -122.3894)
trip = trip_manager.request_trip(rider, pickup, dropoff, RideType.SEDAN)

# Start and complete trip
trip_manager.start_trip(trip.id)
trip_manager.complete_trip(trip.id)
```

## 🔧 Extending the System

### Add a New Pricing Strategy

```python
from ridesharing.strategy.pricing_strategy import PricingStrategy

class SurgePricingStrategy(PricingStrategy):
    def calculate_fare(self, pickup, dropoff, ride_type):
        # Your implementation
        pass

# Use it
trip_manager.set_pricing_strategy(SurgePricingStrategy())
```

### Add a New Matching Strategy

```python
from ridesharing.strategy.driver_matching_strategy import DriverMatchingStrategy

class RatingBasedMatchingStrategy(DriverMatchingStrategy):
    def find_drivers(self, drivers, pickup, ride_type):
        # Your implementation
        pass

# Use it
trip_manager.set_matching_strategy(RatingBasedMatchingStrategy())
```

## 📝 Key Design Decisions

1. **Observer Pattern**: Ensures riders and drivers get real-time updates
2. **Strategy Pattern**: Allows runtime switching of pricing and matching algorithms
3. **Singleton TripManager**: Central coordination point for all trips
4. **Type Safety**: Using Enums for status and types
5. **Separation of Concerns**: Clear separation between models, strategies, and services

## 🎓 Learning Objectives

This implementation demonstrates:
- SOLID principles
- Design patterns in practice
- Clean code architecture
- Python best practices
- Object-oriented design
