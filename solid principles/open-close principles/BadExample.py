class PaymentProcessor:
    def pay(self, payment_method:str, amount:int):
        if payment_method == 'UPI':
            print(f"Starting {payment_method} transation of rs {amount}")
            print(f"upi transaction finished")
        elif payment_method == 'Credit Card':
            print(f"Starting {payment_method} transation of rs {amount}")
            print(f"{payment_method} transaction finished")

        elif payment_method == 'Net Banking':
            print(f"Starting {payment_method} transation of rs {amount}")
            print(f"{payment_method} transaction finished")
            