# src/summarize_churn.py

import os
import pandas as pd

def summarize_daily_churn(predictions_folder, output_path):
    summary = []

    for filename in sorted(os.listdir(predictions_folder)):
        if not filename.endswith(".csv"):
            continue

        df = pd.read_csv(os.path.join(predictions_folder, filename))
        churn_count = df["PredictedChurn"].sum()

        summary.append({
            "day": filename.replace(".csv", ""),
            "predicted_churn_count": int(churn_count)
        })

    summary_df = pd.DataFrame(summary)
    summary_df.to_csv(output_path, index=False)
    print(f"✅ Summary saved to {output_path}")

if __name__ == "__main__":
    summarize_daily_churn(
        predictions_folder="predictions",
        output_path="output/daily_churn_summary.csv"
    )
