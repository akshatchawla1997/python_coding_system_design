from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, password, name, email):
        self.name = name
        self.email = email
        self.password = password
    
    @abstractmethod
    def get_user_type(self):
        pass

    @abstractmethod
    def signup(self):
        pass

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass

    @abstractmethod
    def update_profile(self, name=None, email=None):
        pass
