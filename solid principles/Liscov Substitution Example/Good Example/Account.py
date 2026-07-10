from abc import abstractmethod, ABC

class Account(ABC):
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self):
        pass

