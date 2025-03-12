class ParkingSpot:
    def __init__(self, spot_id: int, spot_type: str):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.is_occupied = False
        self.vehicle = None
        
    def park(self, vehicle):
        if not self.is_occupied:
            self.vehicle = vehicle
            self.is_occupied = True
            
        return False
    
    def remove_vehicle(self):
        self.vehicle = None
        self.is_occupied = False
