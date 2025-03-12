class LockerManager:
    def __init__(self):
        self.lockers = {}
        
    def add_locker(self, locker):
        self.lockers[locker.locker_id] = locker
        
    def remove_locker(self, locker_id):
        if locker_id in self.lockers:
            del self.lockers[locker_id]
            
    def get_locker(self, locker_id):
        return self.lockers.get(locker_id)