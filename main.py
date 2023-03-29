import requests
from api_key import key
import json
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# print(voices[1].id)
engine.setProperty("voice", voices[0].id)

def say(audio):
    engine.say(audio)
    engine.runAndWait()

city = input("Enter the name of the city\n")
url = f"https://api.weatherapi.com/v1/current.json?key={key}&q={city}"
r=  requests.get(url)
# print(r.text)
wdic = json.loads(r.text)
w = wdic.get("current").get('temp_c')
say(f"The current weather in {city} is {w} degree")