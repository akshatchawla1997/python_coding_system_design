class Ecommerce:
    def __init__(self, products, price):
        self.__products = products
        self.__price = price

    def add_product(self, product, price):
        self.__products.append(product)
        self.__price.append(price)

    def get_all_products(self):
        return self.__products
    def get_product_price(self, product):
        return self.__price[self.__products.index(product)]
    def set_product_price(self, product, price):
        self.__price[self.__products.index(product)] = price
    def apply_discount(self, product, discount):
        print(f"Discount applied to {product}: {discount * 100}%")
        self.__price[self.__products.index(product)] = self.__price[self.__products.index(product)] * (1 - discount)
        print(f"Product {product} price after discount: {self.__price[self.__products.index(product)]}")
    def get_total_price(self):
        return sum(self.__price)
    def get_total_products(self):
        return len(self.__products)
ecommerce1 = Ecommerce(["Product 1", "Product 2", "Product 3"], [100, 200, 300])
print(f"All Products: {ecommerce1.get_all_products()}")
print(f"Product 1 Price: {ecommerce1.get_product_price('Product 1')}")
ecommerce1.add_product("Product 4", 400)
print(f"All Products: {ecommerce1.get_all_products()}")
print(f"Product 4 Price: {ecommerce1.get_product_price('Product 4')}")
print(f"All Products: {ecommerce1.get_all_products()}")
ecommerce1.apply_discount('Product 1', 0.1)
print(f"Total Price: {ecommerce1.get_total_price()}")
print(f"Total Products: {ecommerce1.get_total_products()}")