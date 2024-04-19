from datetime import datetime, timedelta

import pandas as pd
import requests
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

def extract_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        if response.status_code == 200:
            books = response.json()['data']
            print("Successfully collect data books")
            df_book = pd.DataFrame(books)
            df_book.to_csv("dags/file/books.csv")
            print("Successfully extract data books to CSV file")
            return df_book
        else:
            print(f"Unexpected status code : {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making the request : {e}")
    
    return None

default_args = {
    "owner":"ika",
    "retries":1,
    "retry_delay":timedelta(minutes=5),
}

with DAG(
    dag_id="data_ingest_exploration_dag_v1",
    default_args=default_args,
    description="soal eksplorasi tugas data ingestion",
    start_date=datetime(2024, 4, 15),
    schedule_interval="0 9 * * 1",
) as dag:
    
    extract_data_task = PythonOperator(
        task_id="extract_data_task",
        python_callable=extract_data,
        op_kwargs={"api_url": f"https://gist.githubusercontent.com/nadirbslmh/8922f71875948802321ef479a017f4c0/raw/1fbbc4b3d55f8ae717eb197d9aaf530ed1bc7ed2/sample.json"},
    )
    
    finish_task = BashOperator(
        task_id="finish_task",
        bash_command="echo 'finish extract data!'",
    )
    
    extract_data_task >> finish_task