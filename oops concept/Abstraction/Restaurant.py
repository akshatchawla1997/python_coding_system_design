from abc import ABC, abstractmethod

class Restaurant(ABC):
    def __init__(self, name, menu):
        self.__name = name
        self.__menu = menu

    @abstractmethod
    def show_Menu(self):
        pass
    
    @abstractmethod
    def place_order(self):
        pass
    
class Veg_Restaurant(Restaurant):
    def __init__(self, name, menu):
        super().__init__(name, menu)
    def show_Menu(self):
        print(f"Menu: {self.__menu}")
    def place_order(self):
        print(f"Order placed")

class Non_Veg_Restaurant(Restaurant):
    def __init__(self, name, menu):
        super().__init__(name, menu)
    def show_Menu(self):
        print(f"Menu: {self.__menu}")
    def place_order(self):
        print(f"Order placed")

class Customer:
    def __init__(self, name, order):
        self.__name = name
        self.__order = order
    def show_order(self):
        print(f"Order: {self.__order}")
    def place_order(self):
        print(f"Order placed")

class Order:
    def __init__(self, item, quantity):
        self.__item = item
        self.__quantity = quantity
    def get_item(self):
        return self.__item
    def get_quantity(self):
        return self.__quantity
    def set_item(self, item):
        self.__item = item
    def set_quantity(self, quantity):
        self.__quantity = quantity
    def show_order(self):
        print(f"Order: {self.__item} {self.__quantity}")
    def place_order(self):
        print(f"Order placed")
    
