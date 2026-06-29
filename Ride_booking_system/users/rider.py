from Ride_booking_system.users.user import User

class Rider(User):
    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)

    def get_user_type(self):
        return "Rider"

    def signup(self):
        # Implement rider-specific signup logic here
        print(f"Rider {self.name} signed up with email {self.email}")

    def login(self):
        # Implement rider-specific login logic here
        print(f"Rider {self.name} logged in.")

    def logout(self):
        # Implement rider-specific logout logic here
        print(f"Rider {self.name} logged out.")

    def update_profile(self, name=None, email=None):
        if name:
            self.name = name
        if email:
            self.email = email