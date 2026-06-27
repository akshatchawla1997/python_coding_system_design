class Vehicle:
    def __init__(self, name, color, type):
        self._name = name
        self._color = color
        self._type = type

    def show_details(self):
        print(f"Name: {self._name}, Color: {self._color}, Type: {self._type}")

    def drive(self):
        print(f"Driving {self._name}")
    

class Car(Vehicle):
    def __init__(self, name, color, type, engine_type):
        super().__init__(name, color, type)
        self._engine_type = engine_type
    
    def drive(self):
        print(f"Driving {self._name} with {self._engine_type}")
    
class Bike(Vehicle):
    def __init__(self, name, color, type, engine_type):
        super().__init__(name, color, type)
        self._engine_type = engine_type
    def drive(self):
        print(f"Driving {self._name} with {self._engine_type}")

class Truck(Vehicle):
    def __init__(self, name, color, type, engine_type):
        super().__init__(name, color, type)
        self._engine_type = engine_type

    def drive(self):
        print(f"Driving {self._name}")


car = Car("suzuki", "black", "4 viller", "Automatic")
car.drive()
car.show_details()

bike = Bike("Bajaj", "Black + blue", "2 viller", "Manual")
bike.drive()
bike.show_details()

truck = Truck("tata", "white + blue", "6 viller", "Manual")
truck.drive()
truck.show_details()