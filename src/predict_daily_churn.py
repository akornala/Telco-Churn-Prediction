# src/predict_daily_churn.py

import os
import pandas as pd
import joblib

from src.preprocess import load_and_clean_data

def predict_daily_churn(feed_folder, model_path, output_folder, summary_csv, at_risk_csv):
    os.makedirs(output_folder, exist_ok=True)

    model = joblib.load(model_path)

    summary_rows = []
    last_day_risk = pd.DataFrame()

    for filename in sorted(os.listdir(feed_folder)):
        if not filename.endswith(".csv"):
            continue

        day_path = os.path.join(feed_folder, filename)
        df = pd.read_csv(day_path)

        original = df.copy()
        df_cleaned = load_and_clean_data(day_path)
        X = df_cleaned.drop("Churn", axis=1)

        predictions = model.predict(X)
        original["PredictedChurn"] = predictions

        output_path = os.path.join(output_folder, filename)
        original.to_csv(output_path, index=False)

        # 💡 Daily metrics
        churn_count = (predictions == 1).sum()
        revenue_risk = original.loc[original["PredictedChurn"] == 1, "MonthlyCharges"].sum()

        day_number = int("".join(filter(str.isdigit, filename)))
        summary_rows.append({
            "day": day_number,
            "at_risk_count": churn_count,
            "revenue_at_risk": revenue_risk
        })

        print(f"✅ {filename}: {churn_count} predicted to churn")

        # 🛑 Save last day's risk data
        if day_number == 30:
            last_day_risk = original[original["PredictedChurn"] == 1]

    # 📝 Save summary
    summary_df = pd.DataFrame(summary_rows)
    summary_df = summary_df.sort_values("day")
    summary_df.to_csv(summary_csv, index=False)
