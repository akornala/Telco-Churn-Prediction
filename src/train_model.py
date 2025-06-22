# src/train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from imblearn.over_sampling import SMOTE
import joblib
import numpy as np

from src.preprocess import load_and_clean_data

def train_and_save_model(data_path, model_path):
    print("🧠 Running TRAIN_MODEL.PY (Random Forest with SMOTE and tuned params)")

    # 1. Load and preprocess data
    df = load_and_clean_data(data_path)
    X = df.drop("Churn", axis=1)
    y = df["Churn"]

    # 2. Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2
        , random_state=42, stratify=y
    )

    # 3. Apply SMOTE
    smote = SMOTE(random_state=42)
    X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

    print(f"Before SMOTE: {y_train.value_counts().to_dict()}")
    print(f"After SMOTE: {pd.Series(y_train_resampled).value_counts().to_dict()}")

    # 4. Random Forest Classifier (best tuning from before)
    model = RandomForestClassifier(
        n_estimators=300,
        max_depth=12,
        min_samples_split=5,
        min_samples_leaf=2,
        class_weight='balanced',
        random_state=42,
        n_jobs=-1
    )

    print(f"Using model: {model.__class__.__name__}")

    # 5. Train
    model.fit(X_train_resampled, y_train_resampled)

    # 6. Predict
    y_pred = model.predict(X_test)

    # Show class prediction distribution
    unique, counts = np.unique(y_pred, return_counts=True)
    print(f"\nPredicted class distribution: {dict(zip(unique, counts))}")

    # 7. Evaluate
    print("\n=== Evaluation ===")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    # 8. Save model
    joblib.dump(model, model_path)
    print(f"\n✅ Model saved to {model_path}")

if __name__ == "__main__":
    train_and_save_model(
        data_path="data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv",
        model_path="models/churn_model.pkl"
    )
