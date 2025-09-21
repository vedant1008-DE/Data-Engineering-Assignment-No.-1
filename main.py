import os
import pandas as pd
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

RAW = os.path.join(DATA_DIR, "patient_vitals_raw.csv")
CLEAN = os.path.join(DATA_DIR, "patient_vitals_clean.csv")
AGG = os.path.join(DATA_DIR, "daily_aggregates.csv")

def ensure_dirs():
    os.makedirs(DATA_DIR, exist_ok=True)

def load_raw():
    if not os.path.exists(RAW):
        raise FileNotFoundError(f"Raw data not found at {RAW}.")
    return pd.read_csv(RAW)

def clean_df(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    # clip outliers
    df["heart_rate_bpm"] = df["heart_rate_bpm"].clip(40, 180)
    df["systolic_bp_mmHg"] = df["systolic_bp_mmHg"].clip(80, 220)
    df["diastolic_bp_mmHg"] = df["diastolic_bp_mmHg"].clip(45, 140)
    df["glucose_mg_dL"] = df["glucose_mg_dL"].clip(60, 450)
    df["spo2_percent"] = df["spo2_percent"].clip(85, 100)
    df["temperature_c"] = df["temperature_c"].clip(35.0, 41.0)

    # flags
    df["flag_tachycardia"] = (df["heart_rate_bpm"] > 100).astype(int)
    df["flag_hypertension"] = ((df["systolic_bp_mmHg"] >= 140) | (df["diastolic_bp_mmHg"] >= 90)).astype(int)
    df["flag_hyperglycemia"] = (df["glucose_mg_dL"] >= 180).astype(int)
    df["flag_hypoxemia"] = (df["spo2_percent"] < 94).astype(int)
    df["flag_fever"] = (df["temperature_c"] >= 37.8).astype(int)

    # drop duplicates
    df = df.drop_duplicates(subset=["patient_id", "date"])
    return df

def make_aggregates(df: pd.DataFrame) -> pd.DataFrame:
    agg_daily = df.groupby("date").agg(
        avg_hr=("heart_rate_bpm", "mean"),
        avg_sys=("systolic_bp_mmHg", "mean"),
        avg_dia=("diastolic_bp_mmHg", "mean"),
        avg_glucose=("glucose_mg_dL", "mean"),
        avg_spo2=("spo2_percent", "mean"),
        avg_temp=("temperature_c", "mean"),
        tachy_cases=("flag_tachycardia", "sum"),
        htn_cases=("flag_hypertension", "sum"),
        hypergly_cases=("flag_hyperglycemia", "sum"),
        hypox_cases=("flag_hypoxemia", "sum"),
        fever_cases=("flag_fever", "sum"),
    ).reset_index()
    return agg_daily

def main():
    ensure_dirs()
    print("Loading raw data...")
    df = load_raw()
    print(f"Raw shape: {df.shape}")

    print("Cleaning data and engineering flags...")
    clean = clean_df(df)
    print(f"Clean shape: {clean.shape}")
    clean.to_csv(CLEAN, index=False)

    print("Computing daily aggregates...")
    agg = make_aggregates(clean)
    agg.to_csv(AGG, index=False)

    print("Done. Files saved:")
    print(" -", CLEAN)
    print(" -", AGG)

if __name__ == "__main__":
    main()