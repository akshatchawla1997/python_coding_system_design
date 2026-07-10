from Payment_method import PaymentMethod

class UPIPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paying from UPI {amount}")