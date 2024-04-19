from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

from custom_operator.collect_data_fruits_operator import CollectDataFruitsOperator

default_args = {
    "owner":"ika",
    "retries":5,
    "retry_delay":timedelta(minutes=5),
}

with DAG(
    dag_id="exploration_dag_v1",
    default_args=default_args,
    description="soal eksplorasi",
    start_date=datetime(2024, 4, 10),
    schedule_interval='@daily',
) as dag:
    create_table_task = PostgresOperator(
        task_id="create_table_task",
        postgres_conn_id="my_postgres",
        sql="sql/create_fruits_table.sql",
    )
    
    collect_data_fruits_task = CollectDataFruitsOperator(task_id="collect_data_fruits_task")
    
    insert_data_task = PostgresOperator(
        task_id="insert_data_task",
        postgres_conn_id="my_postgres",
        sql="sql/insert_data_fruits.sql",
    )
    
    create_table_task >> collect_data_fruits_task >> insert_data_task