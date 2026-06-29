from users.rider import Rider
from users.driver import Driver

from Ride_booking_system.vehicles.Vehicle import Vehicle

from Ride_booking_system.payments.upi import UpiPayment

from rides.ride_manager import RideManager


# Create Rider
rider = Rider(
    email="rider@gmail.com",
    password="1234"
)

# Create Driver
driver = Driver(
    email="driver@gmail.com",
    password="5678"
)

# Create Vehicle
vehicle = Vehicle(
    vehicle_number="DL01AB1234",
    vehicle_type="SUV",
    model="Hyundai Creta"
)

# Assign Vehicle to Driver
driver.assign_vehicle(vehicle)

# Create Payment Object
payment = UpiPayment(
    transaction_id=1001,
    upi_id="akshat@upi",
    name="Akshat"
)

# Create Ride Manager
ride_manager = RideManager()

# Create Ride
ride = ride_manager.create_ride(
    rider=rider,
    driver=driver,
    source="Delhi",
    destination="Noida",
    distance=25,
    payment=payment
)

# Start Ride
ride.start_ride()

# Complete Ride
ride.complete_ride()

# Show All Rides
ride_manager.show_all_rides()

