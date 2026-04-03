"""
src/pipelines/etl.py

ETL pipeline for NYC Finance data.
Provides load_raw(), transform(), and save_processed() used by the Airflow DAG,
the benchmarks runner, and the top-level run_etl.py entry point.
"""

import logging
import os

import pandas as pd

logger = logging.getLogger(__name__)

RAW_PATH = os.environ.get(
    "RAW_DATA_PATH", os.path.join("data", "raw", "nyc_finance_synthetic.csv")
)
PROCESSED_PATH = os.environ.get(
    "PROCESSED_DATA_PATH",
    os.path.join("data", "processed", "nyc_finance_processed.csv"),
)


def load_raw(path: str = RAW_PATH) -> pd.DataFrame:
    """Load raw NYC finance CSV data from *path*."""
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Raw data file not found: {path}. "
            "Run the data generator or provide the CSV before executing the pipeline."
        )
    logger.info("Loading raw data from %s", path)
    df = pd.read_csv(path)
    logger.info("Loaded %d rows", len(df))
    return df


def transform(df: pd.DataFrame) -> pd.DataFrame:
    """Compute derived columns and normalise timestamps."""
    df = df.copy()

    if "close" in df.columns and "open" in df.columns:
        df["return"] = (df["close"] - df["open"]) / df["open"]

    if "timestamp" in df.columns:
        df["day_of_week"] = pd.to_datetime(df["timestamp"]).dt.day_name()

    logger.info("Transform complete. Columns: %s", list(df.columns))
    return df


def save_processed(df: pd.DataFrame, path: str = PROCESSED_PATH) -> None:
    """Persist *df* to *path*, creating parent directories as needed."""
    out_dir = os.path.dirname(path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    df.to_csv(path, index=False)
    logger.info("Saved processed data to %s (%d rows)", path, len(df))
