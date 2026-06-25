from abc import ABC, abstractmethod
class Bank_app(ABC):
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance
    def database(self):
        print(f"connected to the database")

    @abstractmethod
    def security(self):
        pass

class SBI_Bank_app(Bank_app):
    def mobile_login(self):
        print(f"mobile login successful")
    
    def security(self):
        print(f"security code is 1234")

mobile_login1 = SBI_Bank_app("John", 1000)
mobile_login1.mobile_login()
mobile_login1.security()