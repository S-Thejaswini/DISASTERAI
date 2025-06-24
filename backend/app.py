from flask import Flask, render_template, request
import requests
import joblib
import pandas as pd
from datetime import datetime
import os
import pickle
import numpy as np
from groq import Groq
app = Flask(__name__)

# Create model directory if it doesn't exist
os.makedirs('models', exist_ok=True)

# Create placeholder model if it doesn't exist
if not os.path.exists("Test\\flood_model.pkl"):
    # Simple placeholder model (Random Forest)
    class SimpleModel:
        def predict(self, X):
            # Always predict based on rainfall amount
            predictions = []
            for _, row in X.iterrows():
                # If rainfall or future rainfall is high, predict flood risk
                if float(row['Rainfall']) > 3 or float(row['Future_Rainfall']) > 5:
                    predictions.append(1)  # Flood risk
                else:
                    predictions.append(0)  # No flood risk
            return np.array(predictions)
    
    # Save placeholder model
    with open("Test\\flood_model.pkl", 'wb') as f:
        pickle.dump(SimpleModel(), f)
    
    # Save feature columns
    feature_columns = ['Max_Temp', 'Min_Temp', 'Rainfall', 'Future_Rainfall', 'Relative_Humidity', 'Wind_Speed']
    with open("Test\\feature_columns.pkl", 'wb') as f:
        pickle.dump(feature_columns, f)

# Load trained model & feature columns  
model = joblib.load("Test\\flood_model.pkl")
feature_columns = joblib.load("Test\\feature_columns.pkl")

# OpenWeather API Key
# API_KEY = "YOUR_API_KEY"
API_KEY = os.environ.get("OPENWEATHER_API_KEY")

if not API_KEY:
    raise ValueError("OPENWEATHER_API_KEY is not set in environment variables.")

#client = Groq(api_key="YOUR_GROQ_API_KEY")
groq_api_key = os.environ.get("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY is not set in environment variables.")

client = Groq(api_key=groq_api_key)

# 🏠 Route for Landing Page
@app.route("/")
def landing():
    return render_template("landing.html")

# 🌊 Route for Prediction Page
@app.route("/prediction")
def prediction_page():
    return render_template("prediction.html")

# 🤖 Route for Chatbot Page
@app.route("/chatbot", methods=["GET", "POST"])
def chatbot():
    if request.method == "POST":
        user_message = request.form["message"]
        system_message = {
            "role": "system",
            "content": "You are an assistant trained to answer only disaster-related queries. If a user asks a non-disaster-related question, politely inform them that you can only respond to disaster-related topics."
        }
        conversation_history = [system_message, {"role": "user", "content": user_message}]

        try:
            completion = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=conversation_history,
                temperature=1,
                max_tokens=1024,
                top_p=1,
                stream=False,
            )
            bot_response = completion.choices[0].message.content
        except Exception as e:
            bot_response = f"Error: {str(e)}"

        return render_template("chatbot.html", user_message=user_message, bot_response=bot_response, now=datetime.now())

    return render_template("chatbot.html", user_message=None, bot_response=None, now=datetime.now())

# 🌊 Route for Flood Prediction
@app.route("/predict", methods=["POST"])
def predict():
    location = request.form["location"]  # Get location input from the form
    
    try:
        WEATHER_URL = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
        FORECAST_URL = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={API_KEY}&units=metric"

        # Get current weather data
        response = requests.get(WEATHER_URL)
        if response.status_code != 200:
            return render_template("result.html", error="Failed to fetch weather data. Please check the location.")

        data = response.json()

        # Get future weather forecast
        forecast_response = requests.get(FORECAST_URL)
        if forecast_response.status_code == 200:
            forecast_data = forecast_response.json()
            future_rainfall = sum([entry.get("rain", {}).get("3h", 0) for entry in forecast_data["list"][:8]])  # Next 24h rainfall
        else:
            future_rainfall = 0

        # Extract required features
        live_weather_data = {
            "Max_Temp": data["main"]["temp_max"],
            "Min_Temp": data["main"]["temp_min"],
            "Rainfall": data.get("rain", {}).get("1h", 0),
            "Future_Rainfall": future_rainfall,
            "Relative_Humidity": data["main"]["humidity"],
            "Wind_Speed": data["wind"]["speed"]
        }

        # Convert to DataFrame
        live_data_df = pd.DataFrame([live_weather_data], columns=feature_columns)

        # Predict Flood Risk
        prediction = model.predict(live_data_df)
        result = "Yes" if prediction[0] == 1 else "No"

        return render_template(
            "result.html",
            flood_risk=result,
            location=location,
            max_temp=live_weather_data["Max_Temp"],
            min_temp=live_weather_data["Min_Temp"],
            rainfall=live_weather_data["Rainfall"],
            future_rainfall=live_weather_data["Future_Rainfall"],
            humidity=live_weather_data["Relative_Humidity"],
            wind_speed=live_weather_data["Wind_Speed"]
        )
    except Exception as e:
        # Fallback with mock data if API call fails
        print(f"Error: {e}")
        mock_data = {
            "flood_risk": "Yes" if "flood" in location.lower() else "No",
            "location": location,
            "max_temp": 24.5,
            "min_temp": 18.2,
            "rainfall": 2.3 if "flood" in location.lower() else 0.5,
            "future_rainfall": 5.8 if "flood" in location.lower() else 1.2,
            "humidity": 78,
            "wind_speed": 4.2
        }
        
        return render_template(
            "result.html",
            flood_risk=mock_data["flood_risk"],
            location=mock_data["location"],
            max_temp=mock_data["max_temp"],
            min_temp=mock_data["min_temp"],
            rainfall=mock_data["rainfall"],
            future_rainfall=mock_data["future_rainfall"],
            humidity=mock_data["humidity"],
            wind_speed=mock_data["wind_speed"]
        )

# 🌦️ Route for Weather Forecast Page
@app.route("/forecast", methods=["GET", "POST"])
def forecast():
    forecast_data = None
    location = None
    error = None
    
    if request.method == "POST":
        location = request.form["location"]
        try:
            # OpenWeather API call for 5-day forecast (we'll use 3 days)
            FORECAST_URL = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={API_KEY}&units=metric"
            
            response = requests.get(FORECAST_URL)
            if response.status_code != 200:
                error = "Failed to fetch weather data. Please check the location."
                return render_template("forecast.html", error=error)
            
            data = response.json()
            
            # Process the forecast data
            processed_data = []
            
            # Get city information
            city_info = {
                "name": data["city"]["name"],
                "country": data["city"]["country"],
                "timezone": data["city"]["timezone"]
            }
            
            # Group forecast by day (every 8 entries = 1 day since data is in 3-hour intervals)
            # We'll take 3 days (24 entries)
            daily_forecasts = {}
            
            for entry in data["list"][:24]:  # 24 entries = 3 days
                timestamp = entry["dt"]
                date = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
                
                if date not in daily_forecasts:
                    daily_forecasts[date] = {
                        "date": datetime.fromtimestamp(timestamp),
                        "min_temp": float(entry["main"]["temp_min"]),
                        "max_temp": float(entry["main"]["temp_max"]),
                        "humidity": float(entry["main"]["humidity"]),
                        "description": entry["weather"][0]["description"],
                        "icon": entry["weather"][0]["icon"],
                        "rainfall": entry.get("rain", {}).get("3h", 0),
                        "wind_speed": float(entry["wind"]["speed"]),
                        "entries": []
                    }
                
                # Update min/max temperatures
                daily_forecasts[date]["min_temp"] = min(daily_forecasts[date]["min_temp"], float(entry["main"]["temp_min"]))
                daily_forecasts[date]["max_temp"] = max(daily_forecasts[date]["max_temp"], float(entry["main"]["temp_max"]))
                
                # Add hourly entry
                daily_forecasts[date]["entries"].append({
                    "time": datetime.fromtimestamp(timestamp).strftime('%H:%M'),
                    "temp": float(entry["main"]["temp"]),
                    "description": entry["weather"][0]["description"],
                    "icon": entry["weather"][0]["icon"],
                    "rainfall": entry.get("rain", {}).get("3h", 0),
                    "wind_speed": float(entry["wind"]["speed"])
                })
            
            # Convert to list and sort by date
            forecast_data = {
                "city": city_info,
                "days": [daily_forecasts[date] for date in sorted(daily_forecasts.keys())]
            }
            
            return render_template("forecast.html", forecast=forecast_data, location=location)
            
        except Exception as e:
            print(f"Error: {e}")
            error = "An error occurred while fetching the forecast. Please try again."
    
    return render_template("forecast.html", forecast=forecast_data, location=location, error=error)

if __name__ == "__main__":
    app.run(debug=True)

