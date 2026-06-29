from Ride_booking_system.users.user import User

class Driver(User):
    def __init__(self, user_id, name, email, license_number):
        super().__init__(user_id, name, email)
        self.license_number = license_number

    def get_user_type(self):
        return "Driver"

    def signup(self):
        # Implement driver-specific signup logic here
        print(f"Driver {self.name} signed up with email {self.email} and license number {self.license_number}")

    def login(self):
        # Implement driver-specific login logic here
        print(f"Driver {self.name} logged in.")
    def logout(self):
        # Implement driver-specific logout logic here
        print(f"Driver {self.name} logged out.")

    def update_profile(self, name=None, email=None, license_number=None):
        if name:
            self.name = name
        if email:
            self.email = email
        if license_number:
            self.license_number = license_number