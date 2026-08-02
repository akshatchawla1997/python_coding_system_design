from DiscountService import DiscountService
from diwali import DiwaliStrattegy 
from holi import HoliStrattegy

diwali_strategy = DiwaliStrattegy()
holi_strategy = HoliStrattegy()
discount_service = DiscountService(diwali_strategy)
discount_service.process()


discount_service = DiscountService(holi_strategy)
discount_service.process()