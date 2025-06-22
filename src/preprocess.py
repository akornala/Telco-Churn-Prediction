import pandas as pd

def load_and_clean_data(path):
    df = pd.read_csv(path)

    # Drop customerID
    df.drop("customerID", axis=1, inplace=True)

    # Convert TotalCharges to numeric
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df["TotalCharges"] = df["TotalCharges"].fillna(df["TotalCharges"].median())

    # Strip spaces from column names and string values
    df.columns = df.columns.str.strip()
    str_cols = df.select_dtypes(include="object").columns
    df[str_cols] = df[str_cols].apply(lambda col: col.str.strip())

    # Convert target to binary
    df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

    # Replace 'No internet service' and 'No phone service' with 'No'
    replace_cols = [
        "OnlineSecurity", "OnlineBackup", "DeviceProtection", "TechSupport",
        "StreamingTV", "StreamingMovies", "MultipleLines"
    ]
    for col in replace_cols:
        df[col] = df[col].replace({
            "No internet service": "No", "No phone service": "No"
        })

    # Encode categorical variables using one-hot encoding
    categorical_cols = df.select_dtypes(include="object").columns.tolist()
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    # 🧠 Feature Engineering - bin tenure
    df["TenureGroup"] = pd.cut(
        df["tenure"],
        bins=[0, 12, 24, 48, 60, 100],
        labels=["0-12", "12-24", "24-48", "48-60", "60+"]
    )

    # 🧠 Feature Engineering - bin MonthlyCharges
    df["MonthlyGroup"] = pd.cut(
        df["MonthlyCharges"],
        bins=[0, 35, 70, 120],
        labels=["Low", "Medium", "High"]
    )

    # Convert categorical bins to numeric codes
    df["TenureGroup"] = df["TenureGroup"].cat.codes
    df["MonthlyGroup"] = df["MonthlyGroup"].cat.codes

    return df
