class Slot:
    def __init__(self, slot_id, size, expiration_date):
        self.slot_id = slot_id
        self.size = size
        self.expiration_date = expiration_date
        self.package = None
        
    def is_occupied(self):
        return self.package is not None
    
    def assign_package(self, package):
        self.package = package
        
    def remove_package(self):
        package = self.package
        self.package = None
        return package