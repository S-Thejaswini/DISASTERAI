import pandas as pd
import requests
import joblib

# 📌 Load Trained Model & Feature Names
model = joblib.load("flood_model.pkl")
feature_columns = joblib.load("feature_columns.pkl")

# 📌 OpenWeatherMap API Configuration
API_KEY = "YOUR_API_KEY"  # Replace with your actual API key
CITY = "Palakkad"  # Example city
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

# 📌 Fetch Live Weather Data
response = requests.get(URL)
data = response.json()

if response.status_code == 200:
    # Extract relevant features with corrected column names
    live_weather_data = {
        "Max_Temp": data["main"]["temp_max"],  # Max temperature
        "Min_Temp": data["main"]["temp_min"],  # Min temperature
        "Rainfall": data.get("rain", {}).get("1h", 0),  # Rainfall in last 1 hour
        "Relative_Humidity": data["main"]["humidity"],  # Humidity
        "Wind_Speed": data["wind"]["speed"]  # Wind speed
    }

    # Convert live data to DataFrame with matching feature names
    live_data_df = pd.DataFrame([live_weather_data], columns=feature_columns)

    # Predict Flood Risk
    prediction = model.predict(live_data_df)
    print("🌊 Flood Risk Prediction:", "Yes" if prediction[0] == 1 else "No")
else:
    print("⚠️ Error fetching weather data. Check API key & city name.")
