#!/usr/bin/env bash
set -e

echo "🔄 [run_etl] Starting ETL pipeline..."

# 1. Create processed data directory if it doesn't exist
mkdir -p data/processed

# 2. Extract (example: download or copy raw files)
python src/extract.py --output_dir data/raw

# 3. Transform (clean, normalize, join CSVs, etc.)
python src/transform.py --input_dir data/raw --output_dir data/processed

# 4. Load (insert into your database)
python src/load.py --data_dir data/processed --db_url "${DATABASE_URL:-postgresql://localhost:5432/nyc_finance}"

echo "✅ ETL complete!"
