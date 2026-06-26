
class Car:
    def __init__(self, window, door, engine_type):
        self.window = window
        self.door = door
        self.engine_type = engine_type

    def driving(self):
        print(f"car is used for driving")

# Single Inheritance as Audi is a Car
class Audi(Car):
    def __init__(self, window, door, engine_type, speed):
        super().__init__(window, door, engine_type)
        self.speed = speed

audiq7 = Audi(4, 4, "V8", 200)
print(f"Audi Q7 window: {audiq7.window}")
print(f"Audi Q7 door: {audiq7.door}")
print(f"Audi Q7 engine type: {audiq7.engine_type}")
audiq7.driving()
print(f"Audi Q7 speed: {audiq7.speed}")