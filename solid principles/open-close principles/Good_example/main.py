from UPI_method import UPIPayment
from Credit_card_payment import CreditCardPayment
from Net_Banking_payment import NetBankingPayment
from PaymentProcessor import PaymentProcessor
upi = UPIPayment()
credit = CreditCardPayment()
netBanking = NetBankingPayment()

payment = PaymentProcessor()

payment.process_payment(upi, 500)
