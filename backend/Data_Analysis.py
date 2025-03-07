#data_analysis.py                                                                                                                                                           import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("floodprediction_openweathermap.csv")

# Display basic information
print("Dataset Overview:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe())

# Check for missing values
print("\nMissing Values:")
print(df.isna().sum())

# Visualizing correlations
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Feature Correlation Heatmap")
plt.show()

# Histogram of Rainfall Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["Rainfall"], bins=30, kde=True)
plt.title("Rainfall Distribution")
plt.xlabel("Rainfall (mm)")
plt.ylabel("Frequency")
plt.show()

# Countplot for Flood Occurrences
plt.figure(figsize=(6, 4))
sns.countplot(x=df["Flood?"], palette="Set2")
plt.title("Flood Occurrence Count")
plt.xlabel("Flood (0 = No, 1 = Yes)")
plt.ylabel("Count")
plt.show()

print("Data Analysis Completed!")
