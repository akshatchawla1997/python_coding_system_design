from WeatherStation import WeatherStation
from TVDisplay import TVDisplay
from MobileDisplay import MobileDisplay

ws = WeatherStation()
tv = TVDisplay()
m = MobileDisplay()

ws.addObserver(tv)
ws.addObserver(m)
ws.updateTemperature(30)
ws.removeObserver(tv)
ws.updateTemperature(45)