# dashboard.py

import pandas as pd
import streamlit as st

# Load summary data
summary_df = pd.read_csv("output/daily_churn_summary.csv")
summary_df["day"] = summary_df["day"].str.extract(r"(\d+)").astype(int)
summary_df = summary_df.sort_values("day")

# Load revenue data
revenue_df = pd.read_csv("output/revenue_at_risk.csv")
revenue_df["day"] = revenue_df["day"].str.extract(r"(\d+)").astype(int)
revenue_df = revenue_df.sort_values("day")

# Load at-risk customers from Day 30
risk_df = pd.read_csv("output/at_risk_customers_day_30.csv")

# Sidebar filters
st.sidebar.header("Filters")
min_charge = st.sidebar.slider("Min Monthly Charge", 0, 120, 0)
contract_filter = st.sidebar.selectbox("Contract Type", ["All"] + sorted(risk_df["Contract"].unique().tolist()))

# Title
st.title("📊 Telecom Churn Dashboard")

# Line charts
st.subheader("📉 Daily Churn & Revenue at Risk")

col1, col2 = st.columns(2)
with col1:
    st.line_chart(summary_df["predicted_churn_count"])
with col2:
    st.line_chart(revenue_df["revenue_at_risk"])

# Filter and show customers at risk on day 30
st.subheader("🙋 Customers at Risk on Day 30")

filtered_df = risk_df[risk_df["MonthlyCharges"] >= min_charge]
if contract_filter != "All":
    filtered_df = filtered_df[filtered_df["Contract"] == contract_filter]

st.write(f"Total at-risk customers: {len(filtered_df)}")
st.dataframe(filtered_df)
