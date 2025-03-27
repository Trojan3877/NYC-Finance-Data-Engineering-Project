# NYC-Finance-Data-Engineering-Project
A Modular data pipeline that ingests, cleans, stores, and analyzes NYC government financiak data, simulating scalable, cloud-ready architecture using open data.
# data_ingestion/nyc_data_fetcher.py

import requests
import os

DATA_URL = "https://data.cityofnewyork.us/api/views/xywu-7bv9/rows.csv?accessType=DOWNLOAD"
SAVE_DIR = "data/raw"
FILENAME = "nyc_payroll_checkbook.csv"

def fetch_and_save_data():
    os.makedirs(SAVE_DIR, exist_ok=True)
    response = requests.get(DATA_URL)
    if response.status_code == 200:
        with open(os.path.join(SAVE_DIR, FILENAME), "wb") as f:
            f.write(response.content)
        print("Data downloaded and saved successfully.")
    else:
        print(f"Failed to fetch data: {response.status_code}")

if __name__ == "__main__":
    fetch_and_save_data()

