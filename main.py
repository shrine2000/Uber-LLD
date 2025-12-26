from ridesharing.model.location import Location
from ridesharing.model.vehicle import Vehicle
from ridesharing.model.driver import Driver
from ridesharing.model.rider import Rider
from ridesharing.model.enums import RideType, DriverStatus
from ridesharing.service.trip_manager import TripManager
from ridesharing.strategy.pricing_strategy import FlatRatePricingStrategy, VehicleBasedPricingStrategy


def main():
    trip_manager = TripManager()
    
    location1 = Location(37.7749, -122.4194)   
    location2 = Location(37.7849, -122.4094) 
    location3 = Location(37.7949, -122.3994) 
    location4 = Location(37.8049, -122.3894) 
    
    vehicle1 = Vehicle("Tesla Model 3", "ABC123", RideType.SEDAN)
    vehicle2 = Vehicle("Toyota Highlander", "XYZ789", RideType.SUV)
    vehicle3 = Vehicle("Auto Rickshaw", "DEF456", RideType.AUTO)
    
    driver1 = Driver("D001", "John Doe", "+1-555-0101", vehicle1, location1)
    driver2 = Driver("D002", "Jane Smith", "+1-555-0102", vehicle2, location2)
    driver3 = Driver("D003", "Bob Johnson", "+1-555-0103", vehicle3, location3)
    
    trip_manager.register_driver(driver1)
    trip_manager.register_driver(driver2)
    trip_manager.register_driver(driver3)
    
    rider1 = Rider("R001", "Alice Brown", "+1-555-0201")
    rider2 = Rider("R002", "Charlie Davis", "+1-555-0202")
    
    print("-" * 60)
    print("SCENARIO 1: Request SEDAN Trip")
    print("-" * 60)
    trip1 = trip_manager.request_trip(rider1, location1, location4, RideType.SEDAN)
    print()
    
    if trip1:
        print(f" Starting trip {trip1.id}...")
        trip_manager.start_trip(trip1.id)
        print()
        
        print(f" Completing trip {trip1.id}...")
        trip_manager.complete_trip(trip1.id)
        print()
    
    print("-" * 60)
    print("SCENARIO 2: Request SUV Trip")
    print("-" * 60)
    trip2 = trip_manager.request_trip(rider2, location2, location3, RideType.SUV)
    print()
    
    if trip2:
        print(f" Starting trip {trip2.id}...")
        trip_manager.start_trip(trip2.id)
        print()
        
        print(f" Cancelling trip {trip2.id}...")
        trip_manager.cancel_trip(trip2.id)
        print()

    print("-" * 60)
    print("SCENARIO 3: Request AUTO Trip")
    print("-" * 60)
    trip3 = trip_manager.request_trip(rider1, location3, location4, RideType.AUTO)
    print()
    
    if trip3:
        print(f" Starting trip {trip3.id}...")
        trip_manager.start_trip(trip3.id)
        print()
        
        print(f" Completing trip {trip3.id}...")
        trip_manager.complete_trip(trip3.id)
        print()
    
    print("-" * 60)
    print("SCENARIO 4: Using Flat Rate Pricing Strategy")
    print("-" * 60)
    trip_manager.set_pricing_strategy(FlatRatePricingStrategy())
    trip4 = trip_manager.request_trip(rider2, location1, location4, RideType.SEDAN)
    print()
    
    if trip4:
        print(f" Completing trip {trip4.id}...")
        trip_manager.start_trip(trip4.id)
        trip_manager.complete_trip(trip4.id)
        print()
    
    print("=" * 60)
    print("TRIP HISTORY")
    print("=" * 60)
    print(f"\n Rider {rider1.name} trip history:")
    for trip in rider1.trip_history:
        print(f"   - Trip {trip.id[:8]}... | Status: {trip.status.name} | Fare: ${trip.fare:.2f}")
    
    print(f"\n Rider {rider2.name} trip history:")
    for trip in rider2.trip_history:
        print(f"   - Trip {trip.id[:8]}... | Status: {trip.status.name} | Fare: ${trip.fare:.2f}")
    
    print(f"\n Driver {driver1.name} trip history:")
    for trip in driver1.trip_history:
        print(f"   - Trip {trip.id[:8]}... | Status: {trip.status.name} | Fare: ${trip.fare:.2f}")
    
    print()
    print("=" * 60)
    print("DEMO COMPLETED")
    print("=" * 60)


if __name__ == "__main__":
    main()
