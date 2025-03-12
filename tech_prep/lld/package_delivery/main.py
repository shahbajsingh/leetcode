from datetime import datetime, timedelta
from models.package import Package
from models.locker import Locker
from models.slot import Slot
from services.package_manager import PackageManager

# Initialize the package manager
package_manager = PackageManager()

# Initialize lockers and slots
locker1 = Locker(locker_id="L001", location="Floor 1")
locker2 = Locker(locker_id="L002", location="Floor 2")

# Add slots to lockers
slot1 = Slot(size=10, slot_id="S001", expiration_date=(datetime.now() + timedelta(days=10)).strftime("%Y-%m-%d"))
slot2 = Slot(size=15, slot_id="S002", expiration_date=(datetime.now() + timedelta(days=5)).strftime("%Y-%m-%d"))

locker1.add_slot(slot1)
locker2.add_slot(slot2)

# Create new packages
package1 = Package(package_id=1001, size=10, status="preparing", expiration_date=(datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d"))
package2 = Package(package_id=1002, size=15, status="shipped", expiration_date=(datetime.now() + timedelta(days=3)).strftime("%Y-%m-%d"))

# Add packages to the manager
package_manager.add_package(package1)
package_manager.add_package(package2)

# Assign packages to lockers and slots
locker1.reserve_slot(slot1, package1)
locker2.reserve_slot(slot2, package2)

# Update package statuses
package_manager.update_package_status(1001, "arrived")
package_manager.update_package_status(1002, "received")

# Track packages
tracking_info1 = package_manager.track_package(1001)
tracking_info2 = package_manager.track_package(1002)

print(f"Tracking Info for Package 1001: {tracking_info1}")
print(f"Tracking Info for Package 1002: {tracking_info2}")

# Check for expired packages
expired_packages = package_manager.check_expirations()
print(f"Expired Packages: {expired_packages}")

# Retrieve packages from lockers
locker1.retrieve_package(1001)
locker2.retrieve_package(1002)

# Check again for expired packages after retrieval
expired_packages = package_manager.check_expirations()
print(f"Expired Packages After Retrieval: {expired_packages}")
