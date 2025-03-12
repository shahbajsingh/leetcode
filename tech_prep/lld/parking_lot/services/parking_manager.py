class ParkingManager:
    def __init__(self, parking_lot):
        self.parking_lot = parking_lot
        
    def handle_parking(self, vehicle):
        return self.parking_lot.park_vehicle(vehicle)
    
    def handle_exit(self, license_plate):
        return self.parking_lot.remove_vehicle(license_plate)