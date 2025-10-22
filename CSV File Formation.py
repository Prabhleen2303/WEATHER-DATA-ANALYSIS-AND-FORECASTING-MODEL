import requests
import csv
from datetime import datetime, timedelta

API_KEY = "5a6baf3462c748e5aab172019252309"  # Replace with your actual WeatherAPI.com key
LOCATION = "Mohali"
CSV_FILE = "weather_data.csv"

base_url = "http://api.weatherapi.com/v1/history.json"

# Get dates for the last 7 days (including today)
dates = [(datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(7)]

weather_data = []

for date in dates:
    params = {
        "key": API_KEY,
        "q": LOCATION,
        "dt": date
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    if "forecast" in data:
        day_data = data["forecast"]["forecastday"][0]["day"]
        avg_temp = day_data.get("avgtemp_c", None)
        total_rain = day_data.get("totalprecip_mm", None)
        avg_humidity = day_data.get("avghumidity", None)
        max_wind = day_data.get("maxwind_kph", None)

        weather_data.append([date, LOCATION, avg_temp, total_rain, avg_humidity, max_wind])
    else:
        print(f"Could not fetch data for date: {date}")

# Write to CSV
with open(CSV_FILE, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Date",
        "Location",
        "AvgTemp_C",
        "Rainfall_mm",
        "AvgHumidity",
        "MaxWind_kph"
    ])
    writer.writerows(weather_data)

print(f"✅ CSV file '{CSV_FILE}' created with past 7-day weather data for {LOCATION}!")