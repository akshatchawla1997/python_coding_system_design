from typing import List
from Observer import Observer

class WeatherStation:
    def __init__(self):
        self.__temperature = 0
        self.__observers: List[Observer] = []

    def addObserver(self, newObserver: Observer):
        self.__observers.append(newObserver)
    
    def removeObserver(self, ob:Observer):
        self.__observers.remove(ob)
    
    def updateTemperature(self, new_temp):
        self.__temperature = new_temp
        self.notifyObservers()

    def notifyObservers(self):
        for observer in self.__observers:
            observer.update(self.__temperature)
