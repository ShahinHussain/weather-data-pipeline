import json
import os
import pandas as pd
import sqlite3

def clean_weather_data():
    files = [f for f in os.listdir('data') if f.endswith('.json')]
    data_list = []
    
    for file in files:
        with open(f'data/{file}', 'r') as f:
            data = json.load(f)
            cleaned_data = {
                'city': data['name'],
                'temperature': data['main']['temp'] - 273.15,
                'humidity': data['main']['humidity'],
                'pressure': data['main']['pressure'],
                'weather': data['weather'][0]['description'],
                'timestamp': data['dt']
            }
            data_list.append(cleaned_data)
    
    df = pd.DataFrame(data_list)
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    
    conn = sqlite3.connect('weather.db')
    df.to_sql('weather', conn, if_exists='replace', index=False)
    conn.close()
    print("Data cleaned and stored in weather.db")

if __name__ == '__main__':
    clean_weather_data()
