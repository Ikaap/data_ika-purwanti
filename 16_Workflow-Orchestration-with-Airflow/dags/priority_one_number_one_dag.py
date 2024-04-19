from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner":"ika",
    "retries":5,
    "retry_delay":timedelta(minutes=2),
}

with DAG(
    dag_id="priority_one_number_one_dag_v1",
    default_args=default_args,
    description="soal prioritas 1 nomor 1",
    start_date=datetime(2024, 4, 8),
    schedule_interval='@daily',
) as dag:
    task1 = BashOperator(
        task_id="task_1",
        bash_command="echo 'hello airflow'",
    )
    task2 = BashOperator(
        task_id="task_2",
        bash_command="mkdir -p about_us",
    )
    task3 = BashOperator(
        task_id="task_3",
        bash_command="mkdir -p our_works",
    )
    task4 = BashOperator(
        task_id="task_4",
        bash_command="touch about_us/about.txt",
    )
    task5 = BashOperator(
        task_id="task_5",
        bash_command="touch our_works/works.txt",
    )
    task6 = BashOperator(
        task_id="task_6",
        bash_command="echo 'done!'",
    )
    
    task1 >> task2 >> task4 >> task6
    task1 >> task3 >> task5 >> task6