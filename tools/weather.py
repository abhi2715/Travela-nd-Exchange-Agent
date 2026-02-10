import os
import requests

def get_weather(city: str):
    key = os.getenv("OPENWEATHER_API_KEY")
    if not key:
        return {"error": "Weather API key missing"}

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={key}&units=metric"
    )

    res = requests.get(url).json()

    if res.get("cod") != 200:
        return {"error": "City not found"}

    return {
        "city": city,
        "temp_celsius": res["main"]["temp"],
        "humidity": res["main"]["humidity"],
        "description": res["weather"][0]["description"],
    }