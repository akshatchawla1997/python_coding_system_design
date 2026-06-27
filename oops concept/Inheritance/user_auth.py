from abc import ABC, abstractmethod

class User(ABC):
    @abstractmethod
    def security(self):
        pass
    
class Authentication(User):

    def __init__(self, email, password, phone_number):
        self.email = email
        self.password = password
        self.phone_number = phone_number

    def security(self, email, password):
        if(email == self.email):
            if(password == self.password):
                print(f"user verified successfully with this email {email}")
            
            else:
                print("password dosent matched")
        else:
            print("Check Email as it dosent found in the database try signup")

    @staticmethod
    def signup(email, password, phone_number):
        print(f"Signing up new user: {email}...")
        return Authentication(email, password, phone_number)

new_user = Authentication.signup("akshat@example.com", "secure123", "1234567890")

# 2. Try to log in with the wrong password
new_user.security("akshat@example.com", "wrong_password") 
# Output: Password doesn't match.

# 3. Try to log in with correct credentials
new_user.security("akshat@example.com", "secure123")