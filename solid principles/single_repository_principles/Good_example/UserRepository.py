from User import User
class UserRepository:
    def __init__(self, db, user, password):
        self.db = db
        self.user = user
        self.password = password
    
    def add_to_database(self, user:"User"):
        print(f"{user.name} is saved to database whose age is {user.age} and their email is {user.email}")

    def del_from_database(self, user:"User"): # how we use annotations
        print(f"{user.name} is deleted from db whose age is {user.age} and their email is {user.email}")