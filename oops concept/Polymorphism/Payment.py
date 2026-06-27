from abc import ABC, abstractmethod
class Payment(ABC):

    def __init__(self, transaction_id):
        self.__transaction_id = transaction_id
    @abstractmethod
    def process_payment(self, amount):
        pass


class UpiPayment(Payment):

    def __init__(self, transaction_id, upi_id, name):
        super().__init__(transaction_id)
        self.__upi_id = upi_id

    def process_payment(self, amount):
        print(f"Paid {amount} using UPI")

class CardPayment(Payment):
    def __init__(self, transaction_id, card_no, cvv, name):
        super().__init__(transaction_id)
        self.__card_no = card_no
        self.__cvv = cvv
        self.__name = name
    def process_payment(self, amount):
        print(f"Paid {amount} using Card")


class WalletPayment(Payment):

    def __init__(self, transaction_id, wallet, name):
        super().__init__(transaction_id)
        self.__wallet = wallet
        self.__name = name

    def process_payment(self, amount):
        print(f"Paid {amount} using Wallet")


upi = UpiPayment(
    transaction_id=1,
    upi_id="akshat@upi",
    name="Akshat"
)

card = CardPayment(
    transaction_id=2,
    card_no="123456789",
    cvv=123,
    name="Akshat"
)

wallet = WalletPayment(
    transaction_id=3,
    wallet="Paytm",
    name="Akshat"
)

payments = [upi, card, wallet]

for payment in payments:
    payment.process_payment(500)