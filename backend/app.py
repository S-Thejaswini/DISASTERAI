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
API_KEY = "YOUR_API_KEY"

client = Groq(api_key="YOUR_GROQ_API_KEY")

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
