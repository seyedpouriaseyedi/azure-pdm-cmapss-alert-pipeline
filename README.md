# azure-pdm-cmapss-alert-pipeline
Scalable cloud workflow for predictive maintenance alerts: data lake ingestion, Databricks scoring, automated notifications, and task creation (Azure).

flowchart LR
  A[raw/ CSV in ADLS] --> B[Databricks ETL -> processed/ Delta/Parquet]
  B --> C[Train + Score -> risk_score]
  C --> D[alerts/ alerts_*.json + summary.json]
  D --> E[Logic App trigger on blob]
  E --> F[Teams/Email notification]
  E --> G[Power Automate -> Planner task]