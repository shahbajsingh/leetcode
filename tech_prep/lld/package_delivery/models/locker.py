class Locker:
    def __init__(self, locker_id, location, slots=None):
        self.locker_id = locker_id
        self.location = location
        # Initialize slots as an empty list if no slots are passed
        self.slots = slots if slots is not None else []
        self.map = {}

    def add_slot(self, slot):
        """Add a slot to the locker."""
        self.slots.append(slot)

    def reserve_slot(self, slot, package):
        """Reserve a slot for a package."""
        if slot.size >= package.size:
            slot.package_id = package.package_id
            slot.expiration_date = package.expiration_date
            self.map[slot.slot_id] = slot
        else:
            print(f"Slot {slot.slot_id} is too small for package {package.package_id}")

    def retrieve_package(self, package_id):
        """Retrieve a package from the locker."""
        for slot in self.slots:
            if slot.package_id == package_id:
                print(f"Package {package_id} retrieved from locker {self.locker_id}, slot {slot.slot_id}")
                slot.package_id = None
                return
        print(f"Package {package_id} not found in locker {self.locker_id}")

    def lookup(self, package_size):
        """Find available slots for a package of a certain size."""
        available_slots = [slot for slot in self.slots if slot.size >= package_size and slot.package_id is None]
        return available_slots

    def check_expired(self):
        """Check if any package in the locker is expired."""
        expired = []
        for slot in self.slots:
            if slot.package_id and datetime.now() > datetime.strptime(slot.expiration_date, "%Y-%m-%d"):
                expired.append(slot.package_id)
        return expired
