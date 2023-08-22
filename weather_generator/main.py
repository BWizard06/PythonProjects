import requests
from termcolor import colored

print(colored("Hier können sie das Wetter einer beliebigen Stadt auswählen", "cyan"))

API_KEY = "c8a0861ae4f94f253b1b8284ed7040c4"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
unit = "metric"
lang = input(colored("Wollen Sie Englisch(en) oder Deutsch(de) benutzen:  ", "green"))


if lang =="de":
    city = input(colored("Wählen Sie eine Stadt: ", "green"))
elif lang == "en":
    city = input(colored("Enter a city name: ", "green"))

request_url = f"{BASE_URL}?appid={API_KEY}&q={city}&units={unit}&lang={lang}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data["weather"][0]["description"]
    temperature = round(data["main"]["temp"], 1)
    feeling = round(data["main"]["feels_like"], 1)
    wind_speed = round(data["wind"]["speed"] * 3.6, 2)
    country = data["sys"]["country"]
    if lang == "de":
        print(f"Angaben zu {city.capitalize()} in {country}:")
        print(f"Wetter: {weather}")
        print(f"Temperatur: {temperature} Grad")
        print(f"Es fühlt sich wie {feeling} Grad an ")
        print(f"Geschwindigkeit des Windes: {wind_speed} km/h")
    else:
        print(f"Data on {city.capitalize()} in {country}:")
        print(f"Weather: {weather}")
        print(f"Temperature: {temperature} Celsius")
        print(f"It fells like {feeling} Celsius ")
        print(f"Speed of the wind: {wind_speed} km/h")

else:
    if lang == "de":
        print(colored("Diese Stadt steht nicht zur Verfügung", "red"))
    else:
        print(colored("This city is not available", "red"))