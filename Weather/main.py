import requests
import json
import pyttsx3


engine = pyttsx3.init()
print("----------- Welcome to Weather App 1.1 - Created By Rudra -----------".center(80))
engine.say("Welcome to the weather app created by Rudra.")
engine.runAndWait()
engine.say("Enter the name of the city")
engine.runAndWait()
city = input("- Enter the name of the city:")

url = f"https://api.weatherapi.com/v1/current.json?key=28bdeee13bf84addba2155041231312&q={city}"

r = requests.get(url)
Weather_dict = json.loads(r.text)
Weather_Temp = Weather_dict["current"]["temp_c"]
print(f"- The weather in {city} is {Weather_Temp} ºC")
engine.say(f"The weather in {city} is {Weather_Temp} Degree Celsius")
engine.runAndWait()
print("- Thank you for using the Weather App")
engine.say("Thank you for using the Weather App")
engine.runAndWait()