import os
import logging
from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

logger = logging.getLogger("airflow.task")

with DAG(
	dag_id="nba_stats_scraper",
	start_date=datetime(2022, 7, 23),
	schedule=None,
	max_active_runs=1
) as dag:
	task = BashOperator(
		task_id="execute_scraping",
		bash_command="python3 ~/desktop/nba_mvp_predictor/main.py",
		dag=dag
	)
