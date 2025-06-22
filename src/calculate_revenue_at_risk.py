import os
import pandas as pd

def calculate_revenue_at_risk(predictions_folder, output_csv):
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    results = []

    for filename in sorted(os.listdir(predictions_folder)):
        if not filename.endswith(".csv"):
            continue

        path = os.path.join(predictions_folder, filename)
        df = pd.read_csv(path)

        if "PredictedChurn" not in df.columns:
            print(f"⚠️ {filename} missing 'PredictedChurn' column")
            continue

        churned = df[df["PredictedChurn"] == 1]
        revenue = churned["MonthlyCharges"].sum()

        results.append({
            "day": filename.replace(".csv", ""),
            "revenue_at_risk": revenue
        })

    pd.DataFrame(results).to_csv(output_csv, index=False)
    print(f"✅ Revenue at risk saved to {output_csv}")

if __name__ == "__main__":
    calculate_revenue_at_risk(
        predictions_folder="predictions",
        output_csv="output/revenue_at_risk.csv"
    )
