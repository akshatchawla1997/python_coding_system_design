from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, balance:int):
        self.balance:int = balance

    @abstractmethod
    def withdraw():
        pass

    @abstractmethod
    def deposit():
        pass

class SavingsAccount(BankAccount):
    def __init__(self, balance):
        super().__init__(balance)
    
    def withdraw(self, amount):
        if self.balance<amount:
            print("insufficient balance")
        else:
            self.balance -= amount
            print(f"amount withdrawn successfully, remaining balance {self.balance}")
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposited successfully, Remaining Balance {self.balance}")

class FixedDepositAccount(BankAccount):
    def __init__(self, balance):
        super().__init__(balance)
    
    def withdraw(self, amount):
        raise Exception("Cannot Withdraw from FD")
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposited successfully, Remaining Balance {self.balance}")

# s=SavingsAccount(1000)
# s.deposit(1000)
# s.withdraw(500)

fd = FixedDepositAccount(1000)
fd.deposit(1000)
fd.withdraw(500)