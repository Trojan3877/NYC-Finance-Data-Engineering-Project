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
    print("Running drift detection...")

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
