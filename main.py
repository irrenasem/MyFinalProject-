import requests
import os
from datetime import datetime

BASE_URL = 'http://api.weatherapi.com'
def get_weather(api_key, city_name,date=None):
    # Construct the URL for current weather
    url = f"{BASE_URL}/v1/current.json?q={city}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        data = response.json()
        temperature = data['current']['temp_c']
        condition = data['current']['condition']['text']
        return f"Current temperature in {city_name} is {temperature}°C, Condition: {condition}"
    else:
        return "Failed to fetch weather data"
        
    if date:
         # Construct the URL for future weather (7 days forecast)
        url = f"{BASE_URL}/v1/current.json?q={city}&key={api_key}"
        response = requests.get(url)
        data = response.json()
            for item in data['list']:
                dt = datetime.fromtimestamp(item['dt'])
                if dt.date() == datetime.strptime(date, '%Y-%m-%d').date():
                    print(f"\nWeather forecast for {city_name} on {date}:")
                    print(f"Temperature: {item['main']['temp']}°C")
                    print(f"Weather: {item['weather'][0]['description']}")
                    return
            print("No forecast data available for the given date.")
    else:
        return "Failed to fetch weather date"
api_key = os.getenv('API_TOKEN')
city_name = 'Tel Aviv'
print(get_weather(api_key, city_name,))
