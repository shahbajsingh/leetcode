from .parking_floor import ParkingFloor
from .parking_spot import ParkingSpot

class ParkingLot:
    def __init__(self, lot_name: str):
        self.lot_name = lot_name
        self.floors = []
        
    def add_floor(self, floor: ParkingFloor):
        self.floors.append(floor)
        
    def park_vehicle(self, vehicle):
        for floor in self.floors:
            spot = floor.find_available_spot(vehicle.vehicle_type)
            if spot:
                spot.park(vehicle)
                return f'Vehicle {vehicle.license_plate} parked at Floor {floor.floor_id}, Spot {spot.spot_id}'
        return 'No available spot'

    def remove_vehicle(self, license_plate):
        for floor in self.floors:
            for spot in floor.spots:
                if spot.is_occupied and spot.vehicle.license_plate == license_plate:
                    spot.remove_vehicle()
                    return f'Vehicle {license_plate} removed from Floor {floor.floor_id}, Spot {spot.spot_id}'
        return 'Vehicle not found'