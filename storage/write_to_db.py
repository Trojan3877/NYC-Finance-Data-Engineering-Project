# storage/write_to_db.py

import logging
import os
import sqlite3

import pandas as pd

logger = logging.getLogger(__name__)

CLEAN_DATA_PATH = os.environ.get(
    "CLEAN_DATA_PATH", os.path.join("data", "processed", "cleaned_payroll.csv")
)
DB_PATH = os.environ.get("DB_PATH", os.path.join("data", "nyc_finance.db"))


def write_to_sqlite(
    csv_path: str = CLEAN_DATA_PATH, db_path: str = DB_PATH
) -> None:
    """Load cleaned payroll CSV and write it to a SQLite database.

    Raises FileNotFoundError when *csv_path* does not exist so callers can
    handle a missing input file explicitly.
    """
    if not os.path.exists(csv_path):
        raise FileNotFoundError(
            f"Cleaned data file not found: {csv_path}. "
            "Run data_cleaner.py first to generate the cleaned CSV."
        )

    logger.info("Loading cleaned data from %s", csv_path)
    df = pd.read_csv(csv_path)

    db_dir = os.path.dirname(db_path)
    if db_dir:
        os.makedirs(db_dir, exist_ok=True)
    conn = sqlite3.connect(db_path)
    try:
        df.to_sql("payroll_data", conn, if_exists="replace", index=False)
        logger.info(
            "Data successfully written to SQLite at %s (%d rows)", db_path, len(df)
        )
    finally:
        conn.close()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s – %(message)s",
    )
    write_to_sqlite()
