from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from custom_operator.etl_operator import extract_data, transform_data

default_args = {
    "owner":"ika",
    "retries":2,
    "retry_delay":timedelta(minutes=2),
}

with DAG(
    dag_id="data_quality_exploration_dag_v1",
    default_args=default_args,
    description="soal eksplorasi tugas Pemahaman tentang Data Quality dan Data Governance",
    start_date=datetime(2024, 4, 20),
    schedule_interval="@daily",
) as dag:
    
    collect_data_task = PythonOperator(
        task_id="collect_data_task",
        python_callable=extract_data,
        op_kwargs={"api_url": f"https://gist.githubusercontent.com/nadirbslmh/b50406d5579e875e6435896c9ff6c80c/raw/cac8007653b6145e9ad0ec69b1e4fd6c1be718e7/transactions.json"},
    )
    
    transform_data_task = PythonOperator(
        task_id="transform_data_task",
        python_callable=transform_data,
        op_kwargs={"df": "{{ task_instance.xcom_pull(task_ids='collect_data_task') }}"},
    )
    
    collect_data_task >> transform_data_task