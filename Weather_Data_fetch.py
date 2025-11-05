from datetime import datetime
import pandas as pd
from meteostat import Point, Daily

# Mohali Coordinates
city = Point(30.7046, 76.7179)

# 5 years range
start = datetime(2021, 6, 1)
end = datetime.now()

print(" Fetching Mohali DAILY weather data (2021 → 2025)...")

data = Daily(city, start, end).fetch().reset_index()

# show columns
print("Fetched Columns:", data.columns.tolist())

# Keep only available columns
valid_cols = [c for c in ['time','tavg','tmin','tmax','wspd','prcp','pres'] if c in data.columns]
data = data[valid_cols]

# Rename
data = data.rename(columns={
    "time": "date",
    "tavg": "AvgTemp_C",
    "tmin": "MinTemp_C",
    "tmax": "MaxTemp_C",
    "wspd": "MaxWind_kph",
    "prcp": "Rainfall_mm",
    "pres": "Pressure_mb"
})

# If humidity missing, approximate it
if "AvgHumidity" not in data.columns:
    data["AvgHumidity"] = 70 - (data["MaxWind_kph"] * 0.5) + ((data["Pressure_mb"] - 1010) * 0.1)
    data["AvgHumidity"] = data["AvgHumidity"].clip(30, 98)

# Drop NA temp
data = data.dropna(subset=["AvgTemp_C"])

# Lag features
data["Temp_Lag1"] = data["AvgTemp_C"].shift(1)
data["Rain_Lag1"] = data["Rainfall_mm"].shift(1)
data["Humidity_Lag1"] = data["AvgHumidity"].shift(1)

# Rolling features
data["Temp_Roll3"] = data["AvgTemp_C"].rolling(3).mean()
data["Rain_Roll3"] = data["Rainfall_mm"].rolling(3).mean()

data = data.dropna().reset_index(drop=True)

# Save CSV
file_name = "mohali_5_year_weather.csv"
data.to_csv(file_name, index=False)

print(f" 5-Year Dataset Saved → {file_name}")
print(f" Rows: {len(data)}")
print(data.head())

