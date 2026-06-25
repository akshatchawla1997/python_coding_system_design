class Atm_machine:
    def __init__(self, balance, pin):
        self.__balance = balance
        self.__pin = pin

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount} into the account")

    def withdraw(self, amount, pin):
        if self.__pin == pin:
            self.__balance -= amount
            print(f"Withdrawn {amount} from the account")
        else:
            print("Invalid pin")

    def get_balance(self):
        return self.__balance

atm1 = Atm_machine(1000, 1234)
print(f"Initial Balance: {atm1.get_balance()}")
atm1.deposit(500)
atm1.withdraw(200, 1234)
atm1.withdraw(200, 1235)
print(f"Final Balance: {atm1.get_balance()}")