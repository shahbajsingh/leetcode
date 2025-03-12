class Vehicle:
    def __init__(self, license_plate: str, vehicle_type: str):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type
        
class Car(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, 'Car')
        
class Bike(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, 'Bike')
        
class Truck(Vehicle):
    def __init__(self, license_plate: str):
        super.__init__(license_plate, 'Truck')
