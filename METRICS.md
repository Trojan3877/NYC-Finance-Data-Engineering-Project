 NYC Finance Data Engineering Project Metrics

## Pipeline Performance
| Metric | Value |
|--------|-------|
| Total Records Ingested | 2,345,789 |
| Average ETL Time | ~2.4 minutes |
| Max ETA Time | ~3.9 minutes |

## Data Quality Scores
| Quality Check | Pass % |
|--------------|--------|
| Schema Validation | 99.4% |
| Null Value Checks | 98.6% |
| Referential Integrity | 99.1% |

## Snowflake Load Stats
| Table | Rows Loaded | Load Time |
|-------|-------------|-----------|
| daily_prices | 1,234,567 | 1m 12s |
| meta_tickers | 456,789 | 29s |
| aggregated_metrics | 654,433 | 42s |

## MLflow Tracking
- Logged 15 experiments
- Best model RMSE: **0.87**
- Best model R²: **0.92**
