# Patient Health Monitoring — Mini Project (Healthcare Domain)

This repository demonstrates an end-to-end mini project that maps the **data lifecycle** from **capture → storage → processing → visualization** for a healthcare use case.

## 🎯 Use Case
Monitor patient vitals (heart rate, blood pressure, glucose, SpO₂, temperature, BMI) over time to spot anomalies and visualize trends.

## 📂 Repository Structure
```
PatientHealthMonitoring/
├─ data/
│  ├─ patient_vitals_raw.csv
│  ├─ patient_vitals_clean.csv
│  └─ daily_aggregates.csv
├─ scripts/
│  └─ main.py
├─ notebooks/
│  └─ exploration.ipynb  (optional placeholder)
├─ powerbi/
│  └─ model_notes.md
├─ requirements.txt
└─ README.md
```

## 🧭 Data Lifecycle

1. **Capture** — Synthetic vitals are generated programmatically to simulate real-world readings for 120 patients across 30 days.
2. **Storage** — Data is stored as CSVs (easy to share and ingest into BI tools).
3. **Processing** — A Python script cleans outliers, adds anomaly flags, and computes daily aggregates.
4. **Visualization** — Import `patient_vitals_clean.csv` and `daily_aggregates.csv` into **Power BI** to build dashboards (see suggestions below).

## 🛠️ Quickstart

```bash
# 1) (optional) create a virtual environment
python -m venv .venv
# activate:
#   Windows: .venv\Scripts\activate
#   macOS/Linux: source .venv/bin/activate

# 2) install dependencies
pip install -r requirements.txt

# 3) run the data pipeline
python scripts/main.py
```

Outputs will be saved into the `data/` folder.

## 📈 Suggested Power BI Visuals

- **Cards**: Average HR, BP, Glucose, SpO₂, Temperature (last day / selected period)
- **Line Charts**: Trends for average vitals over time (`daily_aggregates.csv`)
- **Clustered Bar**: Count of anomaly flags per day (tachycardia, hypertension, hyperglycemia, hypoxemia, fever)
- **Table/Matrix**: Patient-level latest readings with conditional formatting
- **Slicers**: Date, Sex, Age group, BMI group, Anomaly type

### Power BI Steps
1. Open Power BI Desktop → **Get Data** → **Text/CSV** → load `data/patient_vitals_clean.csv` and `data/daily_aggregates.csv`.
2. Create **date table** if needed for time intelligence.
3. Build visuals listed above. Add bookmarks for **Summary**, **Trends**, **Anomalies** pages.
4. Publish to Power BI Service if required.

## 📏 Data Dictionary (key columns)

- `patient_id`: Identifier (P0001..P0120)
- `date`: ISO date (YYYY-MM-DD)
- `sex`: Male/Female
- `age`: Years
- `bmi`: Body Mass Index
- `heart_rate_bpm`: 40–180 (clipped)
- `systolic_bp_mmHg`: 80–220 (clipped)
- `diastolic_bp_mmHg`: 45–140 (clipped)
- `glucose_mg_dL`: 60–450 (clipped)
- `spo2_percent`: 85–100 (clipped)
- `temperature_c`: 35.0–41.0 (clipped)

**Flags** (0/1):
- `flag_tachycardia`: HR > 100
- `flag_hypertension`: SBP ≥ 140 or DBP ≥ 90
- `flag_hyperglycemia`: Glucose ≥ 180
- `flag_hypoxemia`: SpO₂ < 94
- `flag_fever`: Temp ≥ 37.8

## 🧪 Validation Ideas

- Percentage of anomalous readings per day
- Patients with 3+ anomaly types in the same day
- Trend of anomalies vs. BMI groups or age groups

## 🔗 How to cite in your assignment document

Use a line like:  
**GitHub Repository Link:** `https://github.com/<YourUsername>/PatientHealthMonitoring`

(Replace with your actual URL after uploading.)

## 📜 License
MIT — use freely for learning and demos.