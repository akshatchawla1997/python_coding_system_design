from ride_booking_system.payments.payment import payment

class UpiPayment(Payment):

    def __init__(self, transaction_id, upi_id, name):
        super().__init__(transaction_id)
        self.__upi_id = upi_id

    def process_payment(self, amount):
        print(f"Paid {amount} using UPI")
