from models import Car, Bike, ParkingLot, ParkingFloor, ParkingSpot
from services import ParkingManager

# Initialize parking lot
parking_lot = ParkingLot("Downtown Parking")

# Add floors and spots
floor1 = ParkingFloor(1)
floor1.add_spot(ParkingSpot(1, "Car"))
floor1.add_spot(ParkingSpot(2, "Bike"))
floor1.add_spot(ParkingSpot(3, "Truck"))

parking_lot.add_floor(floor1)

# Parking manager
manager = ParkingManager(parking_lot)

# Park vehicles
print(manager.handle_parking(Car("ABC-123")))
print(manager.handle_parking(Bike("XYZ-789")))

# Remove vehicle
print(manager.handle_exit("ABC-123"))
