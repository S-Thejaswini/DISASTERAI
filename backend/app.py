from flask import Flask, render_template, request
import requests
import joblib
import pandas as pd
from groq import Groq

app = Flask(__name__)

# Load trained model & feature columns  
model = joblib.load("flood_model.pkl")
feature_columns = joblib.load("feature_columns.pkl")

# OpenWeather API Key
API_KEY = "7d3eb5ae386f7f7a066320ab3d177728"

# Initialize Groq chatbot client
GROQ_API_KEY = "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"
client = Groq(api_key=GROQ_API_KEY)

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

        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=conversation_history,
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=False,
        )

        bot_response = completion.choices[0].message.content
        return render_template("chatbot.html", user_message=user_message, bot_response=bot_response)

    return render_template("chatbot.html", user_message=None, bot_response=None)

# 🌊 Route for Flood Prediction
@app.route("/predict", methods=["POST"])
def predict():
    location = request.form["location"]  # Get location input from the form
    WEATHER_URL = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"

    response = requests.get(WEATHER_URL)
    if response.status_code != 200:
        return render_template("result.html", error="Failed to fetch weather data. Please check the location.")

    data = response.json()

    # Extract required features
    live_weather_data = {
        "Max_Temp": data["main"]["temp_max"],
        "Min_Temp": data["main"]["temp_min"],
        "Rainfall": data.get("rain", {}).get("1h", 0),
        "Relative_Humidity": data["main"]["humidity"],
        "Wind_Speed": data["wind"]["speed"]
    }

    # Convert to DataFrame
    live_data_df = pd.DataFrame([live_weather_data], columns=feature_columns)

    # Predict Flood Risk
    prediction = model.predict(live_data_df)
    result = "Yes" if prediction[0] == 1 else "No"

    return render_template("result.html", flood_risk=result, location=location)

if __name__ == "__main__":
    app.run(debug=True)
