import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def visualise_weather_data():
    conn = sqlite3.connect('weather.db')
    df = pd.read_sql('SELECT * FROM weather', conn)
    conn.close()
    
    plt.figure(figsize=(10, 6))
    plt.plot(df['timestamp'], df['temperature'], label='Temperature')
    plt.xlabel('Timestamp')
    plt.ylabel('Temperature (C)')
    plt.title('Temperature Over Time')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    visualise_weather_data()
