from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from custom_operator.etl_operator import extract_data, transform_data, load_data

default_args = {
    "owner":"ika",
    "retries":2,
    "retry_delay":timedelta(minutes=2),
}

with DAG(
    dag_id="de_with_cloud_exploration_dag_v1",
    default_args=default_args,
    description="soal eksplorasi tugas data engineer in the cloud",
    start_date=datetime(2024, 4, 20),
    schedule_interval="@daily",
) as dag:
    
    extract_data_task = PythonOperator(
        task_id="extract_data_task",
        python_callable=extract_data,
        op_kwargs={"api_url": f"https://fakestoreapi.com/products"},
    )
    
    transform_data_task = PythonOperator(
        task_id="transform_data_task",
        python_callable=transform_data,
        op_kwargs={"df": "{{ task_instance.xcom_pull(task_ids='extract_data_task') }}"},
    )
    
    load_data_task = PythonOperator(
        task_id="load_data_task",
        python_callable=load_data,
        op_kwargs={"df": "{{ task_instance.xcom_pull(task_ids='transform_data_task') }}"},
    )
    
    extract_data_task >> transform_data_task >> load_data_task