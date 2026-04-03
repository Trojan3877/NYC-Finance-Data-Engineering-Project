# data_cleaner.py

import logging
import os

import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s – %(message)s",
)
logger = logging.getLogger(__name__)

RAW_PATH = os.environ.get(
    "RAW_DATA_PATH", os.path.join("data", "raw", "nyc_payroll_checkbook.csv")
)
CLEAN_PATH = os.environ.get(
    "CLEAN_DATA_PATH", os.path.join("data", "processed", "cleaned_payroll.csv")
)


def clean_data(raw_path: str = RAW_PATH, clean_path: str = CLEAN_PATH) -> None:
    """Load, clean, and persist NYC payroll data.

    Raises FileNotFoundError when *raw_path* does not exist so callers can
    handle a missing source file explicitly rather than receiving a confusing
    pandas error.
    """
    if not os.path.exists(raw_path):
        raise FileNotFoundError(
            f"Raw data file not found: {raw_path}. "
            "Download or generate the source CSV before running the cleaner."
        )

    logger.info("Loading raw payroll data from %s", raw_path)
    df = pd.read_csv(raw_path)
    logger.info("Loaded %d rows", len(df))

    # Normalise column names
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # Drop rows with null agency or amount
    before = len(df)
    df = df.dropna(subset=["agency_name", "amount"])
    logger.info("Dropped %d rows with null agency_name or amount", before - len(df))

    # Coerce amount to numeric and keep only positive values
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    before = len(df)
    df = df[df["amount"] > 0]
    logger.info("Dropped %d rows with non-positive amount", before - len(df))

    out_dir = os.path.dirname(clean_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    df.to_csv(clean_path, index=False)
    logger.info("Cleaned data saved to %s (%d rows)", clean_path, len(df))


if __name__ == "__main__":
    clean_data()
