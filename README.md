# 📉 Telco Customer Churn Prediction

This project predicts customer churn for a telecom company using machine learning and visualizes daily churn and revenue at risk using an interactive dashboard.

---

## 🚀 Features

- ✅ Clean and preprocess telecom churn data  
- ✅ Train a churn prediction model using Random Forest + SMOTE  
- ✅ Simulate daily customer activity data  
- ✅ Predict churn on daily data feeds  
- ✅ Calculate revenue at risk due to churn  
- ✅ Visualize everything using a Streamlit dashboard  

---

## 🧰 Tech Stack

- **Python** 🐍  
- **Pandas**, **scikit-learn**, **imbalanced-learn**  
- **Streamlit** for the dashboard  
- **Matplotlib** for plotting  
- **Git** & GitHub for version control  

---

## 📁 Project Structure


```
telco_churn_pipeline/
├── data/                     # Raw data (optional)
├── daily_feed/              # Simulated daily customer data
├── models/                  # Trained model pickle file
├── output/                  # Output files like predictions, summaries
├── predictions/             # Daily churn predictions
├── src/                     # Source scripts
│   ├── preprocess.py
│   ├── train_model.py
│   ├── simulate_daily_feed.py
│   ├── predict_daily_churn.py
│   ├── calculate_revenue_at_risk.py
│   ├── summarize_churn.py
│   └── extract_day30_at_risk.py
├── dashboard.py             # Streamlit dashboard app
├── requirements.txt         # Dependencies
└── README.md                # Project documentation
```

---

## 🧪 How to Run

### 1. Clone the repository:
```bash
git clone https://github.com/akornala/Telco-Churn-Prediction.git
cd Telco-Churn-Prediction
````

### 2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies:

```bash
pip install -r requirements.txt
```

### 4. Train the model:

```bash
python -m src.train_model
```

### 5. Simulate and predict churn daily:

```bash
python -m src.simulate_daily_feed
python -m src.predict_daily_churn
```

### 6. Calculate revenue at risk:

```bash
python -m src.calculate_revenue_at_risk
python -m src.summarize_churn
python -m src.extract_day30_at_risk
```

### 7. Launch the dashboard:

```bash
streamlit run dashboard.py
```

---

## 📊 Dashboard Overview

### 📉 Daily Churn and Revenue at Risk

<img src="https://raw.githubusercontent.com/akornala/Telco-Churn-Prediction/main/assets/dashboard_overview.png" width="800"/>

### 👥 Customers at Risk Table

<img src="https://raw.githubusercontent.com/akornala/Telco-Churn-Prediction/main/assets/customers_at_risk_table.png" width="800"/>

> 💡 **Live Dashboard Link:** [View Dashboard Here](https://telco-churn-prediction-azjinmnq9dbjndgupnb2yq.streamlit.app/)

---

## 📌 To Do

* [ ] Add support for multiple models
* [ ] Deploy dashboard on Streamlit Cloud or Render
* [ ] Integrate notification/email alert for high-risk days

---

## 👤 Author

**Akhil Kornala**
🔗 GitHub: [@akornala](https://github.com/akornala)

---

## 📄 License

This project is open source under the [MIT License](LICENSE).

