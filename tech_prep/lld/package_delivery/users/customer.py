from .user import User

class Customer(User):
    def drop_off_package(self, locker, package):
        slot = locker.lookup(package.size)
        if slot:
            code = locker.reserve(slot, package)
            package.update_status('arrived')
            return code
        return None
    
    def pick_up_package(self, locker, code):
        package = locker.retrieve(code)
        if package:
            package.update_status('received')
            return package
        return None
