from datetime import datetime

class Package:
    def __init__(self, package_id, size, locker_id=None, slot_id=None, expiration_date=None, code=None, status='preparing'):
        self.package_id = package_id
        self.size = size
        self.status = status
        self.locker_id = locker_id
        self.slot_id = slot_id
        self.expiration_date = expiration_date
        self.code = code
        
    def update_status(self, status):
        self.status = status
        
    def update_locker_info(self, locker_id, slot_id, code):
        self.locker_id = locker_id
        self.slot_id = slot_id
        self.code = code
        
    def check_expiration(self):
        if not self.expiration_date:
            return False  # no expiration date set
        return datetime.now() > datetime.strptime(self.expiration_date, '%Y-%m-%d')
    
    def __repr__(self):
        return f'Package(ID: {self.package_id}, Status: {self.status}, Expires: {self.expiration_date})'