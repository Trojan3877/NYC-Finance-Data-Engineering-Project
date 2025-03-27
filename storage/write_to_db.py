# storage/write_to_db.py

import pandas as pd
import sqlite3
import os

CLEAN_DATA_PATH = "data/processed/cleaned_payroll.csv"
DB_PATH = "data/nyc_finance.db"

def write_to_sqlite():
    df = pd.read_csv(CLEAN_DATA_PATH)

    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    df.to_sql("payroll_data", conn, if_exists="replace", index=False)
    conn.close()
    print(f"Data successfully written to SQLite at: {DB_PATH}")

if __name__ == "__main__":
    write_to_sqlite()
