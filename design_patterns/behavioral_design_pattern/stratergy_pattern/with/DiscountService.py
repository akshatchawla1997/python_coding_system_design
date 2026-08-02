from Discount_stratergy import DiscountStrategy
class DiscountService:
    def __init__(self, discount_strategy : DiscountStrategy):
        self.__strategy = discount_strategy

    def setstrategy(self, discount_strategy : DiscountStrategy):
        self.__strategy = discount_strategy

    def process(self):
        self.__strategy.calculate_discount()