from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

import random

def generate_random_number(ti):
    random_number_list = []
    for i in range(25):
        number = random.randint(1,50)
        random_number_list.append(number)
        
    ti.xcom_push(key="random_number", value=random_number_list)
    return random_number_list



def sum_list_number(ti):
    list_number = ti.xcom_pull(task_ids="generate_random_number", key="random_number")
    print(f'List number random : {list_number}')
    
    total = 0
    for i in range(len(list_number)):
        total += list_number[i]
    
    ti.xcom_push(key="total_random_number", value=total)
    return total

def check_sum_number(ti):
    total = ti.xcom_pull(task_ids="sum_list_number", key="total_random_number")
    print(f'Total dari list number random : {total}')
    
    if total % 2 == 0:
        print("Even Sum")
    else:
        print("Odd Sum")


default_args = {
    "owner":"ika",
    "retries":5,
    "retry_delay":timedelta(minutes=2),
}

with DAG(
    dag_id="priority_one_number_two_dag_v1",
    default_args=default_args,
    description="soal prioritas 1 nomor 2",
    start_date=datetime(2024, 2, 24),
    schedule_interval='@daily',
) as dag:
    task1 = PythonOperator(
        task_id="generate_random_number",
        python_callable=generate_random_number, 
    )
    task2 = PythonOperator(
        task_id="sum_list_number",
        python_callable=sum_list_number, 
    )
    task3 = PythonOperator(
        task_id="check_sum_number",
        python_callable=check_sum_number, 
    )
    
    task1 >> task2 >> task3