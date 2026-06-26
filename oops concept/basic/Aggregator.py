class Customer:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    def show_address(self):
        print(f"Address: {self.address.city}, {self.address.state}, {self.address.country}")

class Address:
    def __init__(self, city, state, country):
        self.city = city
        self.state = state
        self.country = country

customer1 = Customer("John", 20, Address("New York", "NY", "USA"))
customer1.show_address()
