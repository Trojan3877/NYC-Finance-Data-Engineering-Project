"""
run_etl.py – Entry point for the NYC Finance ETL pipeline.

Delegates to src.pipelines.etl so the same logic is reused by the
Airflow DAG, benchmarks, and direct CLI invocation.

Usage:
    python run_etl.py
"""

import logging

from src.pipelines import etl

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s – %(message)s",
)

if __name__ == "__main__":
    df = etl.load_raw()
    df = etl.transform(df)
    etl.save_processed(df)
