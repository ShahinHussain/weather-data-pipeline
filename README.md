# Weather Data Pipeline

## Description
This project fetches weather data from the OpenWeatherMap API, cleans and processes the data, stores it in a SQLite database, and visualises it using Matplotlib.


## Project Structure
```
weather-data-pipeline/
├── data/
├── scripts/
│ ├── fetch_weather_data.py
│ ├── clean_weather_data.py
│ └── visualise_weather_data.py
├── weather.db
├── requirements.txt
└── README.md
```

## Setup Instructions
1. Clone the repository.
2. Install the required packages:
    ```
    pip install -r requirements.txt
    ```
3. Fetch weather data:
    ```
    python scripts/fetch_weather_data.py
    ```
4. Clean and process the data:
    ```
    python scripts/clean_weather_data.py
    ```
5. Visualise the data:
    ```
    python scripts/visualise_weather_data.py
    ```

## Note
Replace `your_openweathermap_api_key` in `fetch_weather_data.py` with your actual OpenWeatherMap API key.
