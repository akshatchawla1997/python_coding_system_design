from ride_booking_system.payments.payment import payment

class CardPayment(Payment):
    def __init__(self, transaction_id, card_no, cvv, name):
        super().__init__(transaction_id)
        self.__card_no = card_no
        self.__cvv = cvv
        self.__name = name
    def process_payment(self, amount):
        print(f"Paid {amount} using Card")