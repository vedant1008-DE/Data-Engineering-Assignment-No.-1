# Power BI Model Notes

## Data Sources
- `data/patient_vitals_clean.csv`
- `data/daily_aggregates.csv`

## Recommended Relationships
- Use `date` as the key to relate the aggregates to a Date table if you add one.

## Measures (DAX examples to add manually in Power BI)
- `Tachycardia Cases` = SUM('daily_aggregates'[tachy_cases])
- `Hypertension Cases` = SUM('daily_aggregates'[htn_cases])
- `Hyperglycemia Cases` = SUM('daily_aggregates'[hypergly_cases])
- `Hypoxemia Cases` = SUM('daily_aggregates'[hypox_cases])
- `Fever Cases` = SUM('daily_aggregates'[fever_cases])

- `Avg HR` = AVERAGE('daily_aggregates'[avg_hr])
- `Avg SBP` = AVERAGE('daily_aggregates'[avg_sys])
- `Avg DBP` = AVERAGE('daily_aggregates'[avg_dia])
- `Avg Glucose` = AVERAGE('daily_aggregates'[avg_glucose])
- `Avg SpO2` = AVERAGE('daily_aggregates'[avg_spo2])
- `Avg Temperature` = AVERAGE('daily_aggregates'[avg_temp])

## Pages
- Summary
- Trends
- Anomalies