from Payment_method import PaymentMethod
class PaymentProcessor:
    def process_payment(self, payment_method:PaymentMethod, amount):
        PaymentMethod.pay(payment_method, amount)