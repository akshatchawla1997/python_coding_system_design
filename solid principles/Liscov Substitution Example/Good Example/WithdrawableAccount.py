from Account import Account, abstractmethod
class WithdrawAbleAccount(Account):
    def __init__(self, balance):
        super().__init__(balance)

    def withdraw(self, abstract):
        pass