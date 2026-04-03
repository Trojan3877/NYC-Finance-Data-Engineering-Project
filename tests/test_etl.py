"""Tests for src/pipelines/etl.py"""

import os
import tempfile

import pandas as pd
import pytest

from src.pipelines import etl


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def sample_df():
    return pd.DataFrame(
        {
            "timestamp": ["2024-01-01 09:00", "2024-01-02 09:00"],
            "open": [100.0, 105.0],
            "close": [110.0, 100.0],
            "volume": [50000, 75000],
        }
    )


# ---------------------------------------------------------------------------
# load_raw
# ---------------------------------------------------------------------------

def test_load_raw_file_not_found():
    with pytest.raises(FileNotFoundError):
        etl.load_raw("nonexistent/path.csv")


def test_load_raw_returns_dataframe(tmp_path, sample_df):
    csv_path = tmp_path / "data.csv"
    sample_df.to_csv(csv_path, index=False)
    df = etl.load_raw(str(csv_path))
    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(sample_df)


# ---------------------------------------------------------------------------
# transform
# ---------------------------------------------------------------------------

def test_transform_adds_return_column(sample_df):
    result = etl.transform(sample_df)
    assert "return" in result.columns


def test_transform_return_values(sample_df):
    result = etl.transform(sample_df)
    expected_return_0 = (110.0 - 100.0) / 100.0  # 0.10
    assert abs(result["return"].iloc[0] - expected_return_0) < 1e-9


def test_transform_adds_day_of_week(sample_df):
    result = etl.transform(sample_df)
    assert "day_of_week" in result.columns


def test_transform_does_not_mutate_input(sample_df):
    original_cols = list(sample_df.columns)
    etl.transform(sample_df)
    assert list(sample_df.columns) == original_cols


def test_transform_missing_columns():
    """transform() should not crash when optional columns are absent."""
    df = pd.DataFrame({"volume": [1000, 2000]})
    result = etl.transform(df)
    assert "return" not in result.columns
    assert "day_of_week" not in result.columns


# ---------------------------------------------------------------------------
# save_processed
# ---------------------------------------------------------------------------

def test_save_processed_creates_file(sample_df, tmp_path):
    out_path = str(tmp_path / "out" / "processed.csv")
    etl.save_processed(sample_df, path=out_path)
    assert os.path.exists(out_path)


def test_save_processed_roundtrip(sample_df, tmp_path):
    out_path = str(tmp_path / "processed.csv")
    etl.save_processed(sample_df, path=out_path)
    loaded = pd.read_csv(out_path)
    assert list(loaded.columns) == list(sample_df.columns)
    assert len(loaded) == len(sample_df)
