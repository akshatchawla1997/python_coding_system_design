from WithdrawableAccount import WithdrawAbleAccount
class SavingAccount(WithdrawAbleAccount):
    def __init__(self, amount):
        super().__init__(amount)
    
    def withdraw(self, amount):
        if self.balance < amount:
            print("insufficient balance")
        else:
            self.balance -= amount
            print(f"amount withdrawn successfully, remaining balance {self.balance}")
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposited successfully, Remaining Balance {self.balance}")