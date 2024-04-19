from datetime import datetime, timedelta

import pandas as pd
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from custom_operator.collect_data_products_operator import CollectDataProductsOperator
from io import StringIO
import json

def write_csv_file(products):
    if products:
        try:
            products_list = pd.read_json(products)           
            # df_products = pd.DataFrame(products)
            # products(df_products)
            products_list.to_csv("dags/file/products.csv", index=False, sep=',')
            print("CSV file successfully written.")
        except Exception as e:
            print(f"An error occurred while writing CSV file: {e}")
    else:
        print("Failed to write CSV file")

# def write_csv_file(products):
#     if products:
#         try:
#             # Menguraikan string JSON menjadi objek Python
#             products_list = json.loads(products)
            
#             # Menyiapkan DataFrame kosong untuk menyimpan data produk
#             df_products = pd.DataFrame(columns=["id", "title", "price", "description", "category", "image", "rating_rate", "rating_count"])
            
#             for product in products_list:
#                 df_products = df_products.append(product, ignore_index=True)
            
#             df_products.to_csv("dags/file/products.csv", index=False)
            
#             print("CSV file successfully written.")
#         except Exception as e:
#             print(f"An error occurred while writing CSV file: {e}")
#     else:
#         print("Failed to write CSV file")


def write_txt_file(products):
    if products: 
        try:
            with open("dags/file/products.txt", "w") as txtfile:
                # txtfile.write(products)
                json.dump(products, txtfile)
            print("TXT file successfully written.")
        except Exception as e:
            print(f"An error occurred while writing TXT file: {e}")
    else:
        print("Failed to write TXT file")


default_args = {
    "owner":"ika",
    "retries":5,
    "retry_delay":timedelta(minutes=5),
}

with DAG(
    dag_id="priority_two_dag_v1",
    default_args=default_args,
    description="soal prioritas 2",
    start_date=datetime(2024, 4, 10),
    schedule_interval='@daily',
) as dag:
    collect_data_task = CollectDataProductsOperator(task_id="collect_data_task")
    
    write_csv_task = PythonOperator(
        task_id="write_csv_task",
        python_callable=write_csv_file,
        op_kwargs={"products": "{{ task_instance.xcom_pull(task_ids='collect_data_task') }}"},
    )
    
    write_txt_task = PythonOperator(
        task_id="write_txt_task",
        python_callable=write_txt_file,
        op_kwargs={"products": "{{ task_instance.xcom_pull(task_ids='collect_data_task') }}"},
    )
    
    finish_task = BashOperator(
        task_id="finish_task",
        bash_command="echo 'done!'",
    )
    
    collect_data_task >> [write_csv_task, write_txt_task] >> finish_task