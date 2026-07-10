from abc import ABC, abstractmethod

class workable(ABC):
    @abstractmethod
    def work(self):
        pass
    

class Eatable(ABC):
    
    @abstractmethod
    def eat(self):
        pass

class Robot(workable):
    def work(self):
        print("Robot is working")

class Employee(Eatable, workable):
    
    def work(self):
        print("Employee is working")

    def eat(self):
        print("Employee is Eating")

e = Employee()
e.work()
e.eat()

r = Robot()
r.work()