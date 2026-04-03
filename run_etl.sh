#!/usr/bin/env bash
# run_etl.sh – Wrapper that invokes the Python ETL entry point.
# Usage: bash run_etl.sh
set -euo pipefail

echo "[run_etl.sh] Starting NYC Finance ETL pipeline..."
python run_etl.py
echo "[run_etl.sh] ETL pipeline completed successfully."
