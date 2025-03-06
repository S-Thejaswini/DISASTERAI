
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 📌 Load Dataset
file_path = "backend\\data\\processed_dataset\\floodprediction_openweathermap.csv"  # Update if needed
df = pd.read_csv(file_path)
print(df.columns)

# 📌 Select Relevant Features Based on OpenWeatherMap API
feature_columns = ["Max_Temp", "Min_Temp", "Rainfall", "Relative_Humidity", "Wind_Speed"]
target_column = "Flood?"  # Keep this unchanged

df = df[feature_columns + [target_column]]

# 📌 Handle Missing Values
df.fillna(df.median(), inplace=True)  # Example: Using median imputation

# 📌 Split Dataset
X = df[feature_columns]
y = df[target_column]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 📌 Train Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 📌 Evaluate Model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save model and feature names for live data integration
import joblib
joblib.dump(model, "flood_model.pkl")
joblib.dump(feature_columns, "feature_columns.pkl")

print("✅ Model saved as 'flood_model.pkl'")
