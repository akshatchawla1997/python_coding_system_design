from Payment_method import PaymentMethod
class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paying from Credit card {amount}")