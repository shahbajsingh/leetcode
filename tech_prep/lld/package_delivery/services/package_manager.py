from models.package import Package
from datetime import datetime

class PackageManager:
    def __init__(self):
        self.packages = {}
        
    def add_package(self, package):
        '''Add new package to system.'''
        self.packages[package.package_id] = package 
    
    def update_package_status(self, package_id, status):
        '''Update status of a package.'''
        package = self.packages.get(package_id)
        if package:
            package.update_status(status)
            return True
        return False
    
    def get_package(self, package_id):
        '''Retrieve package by ID.'''
        return self.packages.get(package_id)
    
    def check_expirations(self):
        '''Check for expired packages in the system.'''
        expired_packages = []
        for package in self.packages.values():
            if self.is_expired(package):
                expired_packages.append(package)
        return expired_packages
    
    def is_expired(self, package):
        '''Check if a package has expired based on its expiration date.'''
        return datetime.now() > datetime.strptime(package.expiration_date, '%Y-%m-%d')
        
    def track_package(self, package_id):
        '''Track location and status of a package.'''
        package = self.packages.get(package_id)
        if package:
            return {
                'status': package.status,
                'locker_id': package.locker_id,
                'slot_id': package.slot_id,
                'expiration_date': package.expiration_date,
                'code': package.code
            }
        return None