import requests
from decouple import config

def get_weather_data(city):
    api_key = config('OPENWEATHER_API_KEY')
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def get_forecast_data(city):
    api_key = config('OPENWEATHER_API_KEY')
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()
