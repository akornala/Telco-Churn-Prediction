# src/simulate_daily_feed.py

import pandas as pd
import os
import numpy as np

def simulate_daily_feed(data_path, output_folder, days=30):
    os.makedirs(output_folder, exist_ok=True)

    df = pd.read_csv(data_path)
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)  # shuffle
    chunks = np.array_split(df, days)

    for i, chunk in enumerate(chunks, 1):
        day_str = f"day_{i:02d}.csv"
        chunk.to_csv(os.path.join(output_folder, day_str), index=False)
        print(f"✅ Saved {day_str} with {len(chunk)} rows")

if __name__ == "__main__":
    simulate_daily_feed(
        data_path="data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv",
        output_folder="daily_feed",
        days=30
    )
