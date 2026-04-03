"""
src/pipelines/drift_detection.py

Simple data-drift detection helper for the NYC Finance pipeline.
Compares basic statistics of a new batch against a stored reference baseline.
"""

import logging
import os

import pandas as pd

logger = logging.getLogger(__name__)

BASELINE_PATH = os.environ.get(
    "BASELINE_DATA_PATH",
    os.path.join("data", "processed", "nyc_finance_processed.csv"),
)

# Threshold: flag drift when a column's mean shifts by more than this fraction.
DRIFT_THRESHOLD = float(os.environ.get("DRIFT_THRESHOLD", "0.10"))


def detect_drift(
    new_df: pd.DataFrame,
    baseline_path: str = BASELINE_PATH,
    threshold: float = DRIFT_THRESHOLD,
) -> dict:
    """
    Compare *new_df* against the baseline CSV saved at *baseline_path*.

    Returns a dict mapping column name → drift_detected (bool).
    Logs a warning for each column that exceeds *threshold*.
    """
    if not os.path.exists(baseline_path):
        logger.warning(
            "Baseline file not found at %s – skipping drift detection.", baseline_path
        )
        return {}

    baseline = pd.read_csv(baseline_path)
    numeric_cols = new_df.select_dtypes(include="number").columns.intersection(
        baseline.select_dtypes(include="number").columns
    )

    results: dict = {}
    for col in numeric_cols:
        baseline_mean = baseline[col].mean()
        new_mean = new_df[col].mean()
        if baseline_mean == 0:
            drifted = new_mean != 0
        else:
            drifted = abs((new_mean - baseline_mean) / baseline_mean) > threshold
        results[col] = drifted
        if drifted:
            logger.warning(
                "Drift detected in column '%s': baseline mean=%.4f, new mean=%.4f",
                col,
                baseline_mean,
                new_mean,
            )

    return results
