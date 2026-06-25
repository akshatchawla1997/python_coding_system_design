class Bank_Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} into {self.name}'s account")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Withdrawn {amount} from {self.name}'s account")

    def get_balance(self):
        return self.balance

account1 = Bank_Account("John", 1000)
account1.deposit(500)
account1.withdraw(200)
print(account1.get_balance())