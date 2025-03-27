# data_processing/data_cleaner.py

import pandas as pd
import os

RAW_PATH = "data/raw/nyc_payroll_checkbook.csv"
CLEAN_PATH = "data/processed/cleaned_payroll.csv"

def clean_data():
    df = pd.read_csv(RAW_PATH)

    # Example cleaning steps
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    df = df.dropna(subset=["agency_name", "amount"])
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df = df[df["amount"] > 0]

    os.makedirs("data/processed", exist_ok=True)
    df.to_csv(CLEAN_PATH, index=False)
    print("Data cleaned and saved successfully.")

if __name__ == "__main__":
    clean_data()
