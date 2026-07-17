class PhoneDisplay:
    def update(self, new_temp):
        print(f"phone display temperature is {new_temp}")

class TVDisplay:
    def update(self, new_Temp):
        print(f"TV display temperature is {new_Temp}")

class WeatherStation:
    def __init__(self):
        self.__temperature = 0
        self.__phone_display = PhoneDisplay()
        self.__tv_display = TVDisplay()

    def updateTemperature(self, new_temp):
        self.__temperature = new_temp
        self.notifyDisplays()
    def notifyDisplays(self):
        self.__phone_display = self.__phone_display.update(self.__temperature)
        self.__tv_display = self.__tv_display.update(self.__temperature)

ws = WeatherStation()
ws.updateTemperature(30)
