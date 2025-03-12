from .parking_spot import ParkingSpot

class ParkingFloor:
    def __init__(self, floor_id: int):
        self.floor_id = floor_id
        self.spots = []
        
    def add_spot(self, spot: ParkingSpot):
        self.spots.append(spot)
        
    def find_available_spot(self, vehicle_type):
        for spot in self.spots:
            if not spot.is_occupied and spot.spot_type == vehicle_type:
                return spot
        return None
