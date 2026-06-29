from abc import ABC, abstractmethod
class Payments(ABC):

    def __init__(self, transaction_id, name):
        self.__transaction_id = transaction_id
        self.__name = name

    @abstractmethod
    def process_payment(self):
        pass