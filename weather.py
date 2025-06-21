import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

icons = {
    "Clear": "☀️",
    "Clouds": "☁️",
    "Rain": "🌧️",
    "Drizzle": "🌦️",
    "Thunderstorm": "⛈️",
    "Snow": "❄️",
    "Mist": "🌫️",
    "Smoke": "💨",
    "Haze": "🌫️",
    "Dust": "🌪️",
    "Fog": "🌁",
    "Sand": "🏜️",
    "Ash": "🌋",
    "Squall": "💨",
    "Tornado": "🌪️"
}



api_key = os.getenv("OPENWEATHER_API_KEY")

while True:
    city = input("Enter a city name : ").capitalize() 
    if city == "Q":
        break
    r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}")
    if not r.ok:
        print("invalid input")
    data = r.json()
    weather = data['weather'][0]
    main = data['main']
    lat = data['coord']['lat']
    lon = data['coord']['lon']

    tz_r = requests.get(f"https://timeapi.io/api/TimeZone/coordinate?latitude={lat}&longitude={lon}")
    if not tz_r:
        print("Something went wrong")
        continue
    current_time = tz_r.json()['currentLocalTime']
    local_time = current_time.split('T')[0] + ' ' + current_time.split('T')[1].split('.')[0]
    icon = icons[weather['main']]
    intro = f"{icon}   Weather in {city} {local_time}"
    print(f"{intro}\n{'-'*len(intro)}")

