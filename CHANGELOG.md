# Changelog

## [Unreleased]
- Added `docker-compose.yml` for Postgres + ETL service containerization.
- Introduced unit tests for `transform.py` and `load.py`.

## [2025-06-10] v1.0.1
- Fixed bug in `load.py` where null values were causing insert failures.
- Improved `transform.py` to handle new column `VendorName`.

## [2025-05-25] v1.0.0
- Initial release of NYC Finance Data Engineering Project.
- Features:
  - `extract.py` fetches CSV from NYC Open Data portal.
  - `transform.py` cleans and normalizes transaction data.
  - `load.py` writes to Postgres database.
  - Basic unit tests and CI configuration.
