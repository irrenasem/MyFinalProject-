import requests
import os

def get_weather(api_key, city):
    url = f"http://api.weatherapi.com/v1/current.json?q={city}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        temperature = data['current']['temp_c']
        condition = data['current']['condition']['text']
        return f"Current temperature in {city} is {temperature}°C, Condition: {condition}"
    else:
        return "Failed to fetch weather data"

api_key = os.getenv('API_TOKEN')
city = 'Tel Aviv'
print(get_weather(api_key, city))
