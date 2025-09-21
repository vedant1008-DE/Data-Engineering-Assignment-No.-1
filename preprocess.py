import pandas as pd

# Load dataset
df = pd.read_csv("patient_vitals.csv")

# Display first few records
print("Initial Data:")
print(df.head())

# Handle missing values (if any)
df = df.fillna(method='ffill')

# Normalize columns (example: scale vitals between 0 and 1)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()

vitals = ["HeartRate", "BloodPressure_Systolic", "BloodPressure_Diastolic", "GlucoseLevel", "OxygenSaturation"]
df[vitals] = scaler.fit_transform(df[vitals])

# Save cleaned dataset
df.to_csv("patient_vitals_cleaned.csv", index=False)

print("\nCleaned & Normalized Data:")
print(df.head())
