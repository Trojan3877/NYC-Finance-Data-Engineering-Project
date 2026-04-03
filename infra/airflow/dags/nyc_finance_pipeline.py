from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from src.pipelines import etl
from src.pipelines.drift_detection import detect_drift

def run_etl():
    df = etl.load_raw()
    df = etl.transform(df)
    etl.save_processed(df)

def run_drift():
    import pandas as pd
    import os

    processed_path = etl.PROCESSED_PATH
    if not os.path.exists(processed_path):
        print("No processed data found; skipping drift detection.")
        return

    df = pd.read_csv(processed_path)
    results = detect_drift(df)
    drifted = [col for col, flag in results.items() if flag]
    if drifted:
        print(f"Drift detected in columns: {drifted}")
    else:
        print("No drift detected.")

with DAG(
    dag_id="nyc_finance_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@hourly",
    catchup=False,
) as dag:

    etl_task = PythonOperator(
        task_id="run_etl",
        python_callable=run_etl
    )

    drift_task = PythonOperator(
        task_id="run_drift",
        python_callable=run_drift
    )

    etl_task >> drift_task
