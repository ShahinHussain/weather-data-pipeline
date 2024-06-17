import requests
import json
import os
from datetime import datetime

API_KEY = 'your_openweathermap_api_key'
CITY = 'London'
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"

def fetch_weather_data():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        filename = f"data/weather_{CITY}_{timestamp}.json"
        os.makedirs('data', exist_ok=True)
        with open(filename, 'w') as f:
            json.dump(data, f)
        print(f"Data saved to {filename}")
    else:
        print(f"Failed to fetch data: {response.status_code}")

if __name__ == '__main__':
    fetch_weather_data()
