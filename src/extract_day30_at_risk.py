# src/extract_day30_at_risk.py

import pandas as pd

def extract_day30_at_risk(predictions_path, output_path):
    df = pd.read_csv(predictions_path)
    at_risk = df[df["PredictedChurn"] == 1]

    columns_to_keep = ["tenure", "MonthlyCharges", "TotalCharges", "Contract"]
    at_risk = at_risk[columns_to_keep]

    at_risk.to_csv(output_path, index=False)
    print(f"✅ Saved at-risk customers for Day 30 to {output_path}")

if __name__ == "__main__":
    extract_day30_at_risk(
        predictions_path="predictions/day_30.csv",
        output_path="output/at_risk_customers_day_30.csv"
    )

