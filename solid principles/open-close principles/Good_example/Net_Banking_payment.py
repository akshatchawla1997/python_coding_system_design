from Payment_method import PaymentMethod
class NetBankingPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paying from Net Banking {amount}")