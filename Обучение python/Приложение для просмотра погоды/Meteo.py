import eel
import pyowm

owm = pyowm.OWM("")
city = ""

@eel.expose
def get_weather(place):
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(city)
    w = observation.weather

    temp = w.temperature('celsius')['temp']

    return f"В городе {city} сейчас {str(temp)} градусов"
    


eel.init("web")

eel.start("mein.html", size=(700, 700))