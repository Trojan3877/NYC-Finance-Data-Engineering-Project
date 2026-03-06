import pandas as pd
from datetime import datetime

def load_raw():
    df = pd.read_csv("data/raw/nyc_finance_synthetic.csv")
    return df

def transform(df):
    df["return"] = (df["close"] - df["open"]) / df["open"]
    df["day_of_week"] = pd.to_datetime(df["timestamp"]).dt.day_name()
    return df

def save_processed(df):
    df.to_csv("data/processed/nyc_finance_processed.csv", index=False)

if __name__=="__main__":
    df = load_raw()
    df = transform(df)
    save_processed(df)
