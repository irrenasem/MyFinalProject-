import requests
import os
from datetime import datetime

BASE_URL = 'http://api.weatherapi.com'
def get_weather(api_key, city_name):
    # Construct the URL for current weather
    url = f"{BASE_URL}/v1/current.json?q={city}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        temperature = data['current']['temp_c']
        condition = data['current']['condition']['text']
        return f"Current temperature in {city_name} is {temperature}°C, Condition: {condition}"
    else:
        return "Failed to fetch weather data"

api_key = os.getenv('API_TOKEN')
city_name = 'Tel Aviv'
print(get_weather(api_key, city_name))
