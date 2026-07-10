class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    
    def get_user_info(self):
        print(f"my info is {self.name} {self.age} and email is {self.email}")

    def is_adult(self)->bool:
        return self.age >= 18
    
    def add_to_database(self):
        print(f"{self.name} is saved to database")

    def del_from_database(self):
        print(f"{self.name} is deleted from db")