import requests
import os
import sys
from datetime import datetime


BASE_URL = 'http://api.weatherapi.com'
def get_weather(api_key, city_name, date=None):
    # Construct the URL for current weather
    url = f"{BASE_URL}/v1/current.json?q={city_name}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        data = response.json()
        temperature = data['current']['temp_c']
        condition = data['current']['condition']['text']
        return f"The temperature in {city_name} for date:{date} is {temperature}°C, Condition: {condition}"
    else:
        return "Failed to fetch weather data"
        

#api_key = os.getenv('API_TOKEN')
api_key='aad50edd35ed4d579c995156242408'
if __name__ == "__main__":
    api_key='aad50edd35ed4d579c995156242408'
#    city_name = input("Please enter the city name: ")
     city_name = os.getenv('CITY_NAME')
    # Ask for future date
    while True:
#        date_str = input("Please enter a future date (YYYY-MM-DD): ")
         date_str = os.getenv('FUTURE_DATE')
        try:
            future_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            if future_date == datetime.today().date():
                print("FYI you add Current date.")
                future_date=datetime.today().date()
                break
            elif future_date < datetime.today().date():
                 print("The date must be in the future. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
    
    get_weather(city_name, future_date.isoformat())

print (get_weather(api_key, city_name , future_date.isoformat()))
