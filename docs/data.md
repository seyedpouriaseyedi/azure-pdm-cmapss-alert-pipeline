# Dataset: NASA C-MAPSS (Turbofan Engine Degradation)

## Summary
NASA C-MAPSS is a simulated turbofan engine degradation dataset used for predictive maintenance.
It contains multivariate time-series sensor readings per engine ("unit") over operating cycles until failure.

## Subset used (MVP)
**FD001** (single operating condition, single fault mode) — chosen to keep the baseline demo simple.

## Raw zone layout (Azure target)
- `raw/cmapss/FD001/train_FD001.txt`
- `raw/cmapss/FD001/test_FD001.txt`
- `raw/cmapss/FD001/RUL_FD001.txt`

## Local dev layout (VS Code)
- `data/raw/cmapss/FD001/*` (ignored by git)
- `sample-data/cmapss_fd001_train_sample.csv` (committed; tiny sample)

## File format
`train_*.txt` and `test_*.txt` are whitespace-separated with no header.
Each row = one unit-cycle observation.

## Columns
- `unit` : engine ID
- `cycle`: cycle index (time)
- `setting1`, `setting2`, `setting3`: operational settings
- `s1` … `s21`: sensor measurements

Total columns: 26.

## Labels 
We will derive a binary label from Remaining Useful Life (RUL), e.g.:
`will_fail_within_N_cycles = (RUL <= N)`, and use predicted probability as `risk_score`.