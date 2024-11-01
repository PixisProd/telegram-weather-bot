import requests
from config import WEATHER_API_KEY


def get_weather_by_name(name: str):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={name}&appid={WEATHER_API_KEY}&units=metric'
    request = requests.get(url=url)

    return request.json()
