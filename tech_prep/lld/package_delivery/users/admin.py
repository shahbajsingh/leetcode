from .user import User

class Admin(User):
    def add_locker(self, locker_manager, locker):
        locker_manager.add_locker(locker)
        
    def remove_locker(self, locker_manager, locker_id):
        locker_manager.remove_locker(locker_id)