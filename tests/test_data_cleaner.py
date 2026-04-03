"""Tests for data_cleaner.py"""

import os

import pandas as pd
import pytest

from data_cleaner import clean_data


def _write_raw(tmp_path, rows):
    raw_dir = tmp_path / "data" / "raw"
    raw_dir.mkdir(parents=True)
    df = pd.DataFrame(rows)
    csv_path = raw_dir / "nyc_payroll_checkbook.csv"
    df.to_csv(csv_path, index=False)
    return str(tmp_path)


def test_clean_data_produces_output(tmp_path, monkeypatch):
    rows = [
        {"agency_name": "NYPD", "amount": "1000.50"},
        {"agency_name": "DOE", "amount": "500.00"},
    ]
    base = _write_raw(tmp_path, rows)
    monkeypatch.chdir(base)

    clean_data()

    out = os.path.join(base, "data", "processed", "cleaned_payroll.csv")
    assert os.path.exists(out)
    result = pd.read_csv(out)
    assert len(result) == 2


def test_clean_data_drops_null_agency(tmp_path, monkeypatch):
    rows = [
        {"agency_name": "NYPD", "amount": "1000"},
        {"agency_name": None, "amount": "500"},
    ]
    base = _write_raw(tmp_path, rows)
    monkeypatch.chdir(base)

    clean_data()

    out = os.path.join(base, "data", "processed", "cleaned_payroll.csv")
    result = pd.read_csv(out)
    assert len(result) == 1
    assert result["agency_name"].iloc[0] == "NYPD"


def test_clean_data_drops_non_positive_amounts(tmp_path, monkeypatch):
    rows = [
        {"agency_name": "NYPD", "amount": "100"},
        {"agency_name": "DOE", "amount": "0"},
        {"agency_name": "DOT", "amount": "-50"},
    ]
    base = _write_raw(tmp_path, rows)
    monkeypatch.chdir(base)

    clean_data()

    out = os.path.join(base, "data", "processed", "cleaned_payroll.csv")
    result = pd.read_csv(out)
    assert len(result) == 1
    assert result["agency_name"].iloc[0] == "NYPD"


def test_clean_data_raises_when_raw_missing(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    with pytest.raises((FileNotFoundError, Exception)):
        clean_data()
