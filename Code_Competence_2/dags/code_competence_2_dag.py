from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
import pandas as pd
import google.cloud.storage
from datetime import datetime
import json 

def load_data(ti):
    df_event = pd.read_parquet(f"D:/Alterra Academy/tugas/data_ika-purwanti/Code_Competence_2/dags/file/events.parquet")
    df_customer = pd.read_parquet(f"D:/Alterra Academy/tugas/data_ika-purwanti/Code_Competence_2/dags/file/customers.parquet")
    df_ticket = pd.read_parquet(f"D:/Alterra Academy/tugas/data_ika-purwanti/Code_Competence_2/dags/file/tickets.parquet")
    df_transaction = pd.read_parquet(f"D:/Alterra Academy/tugas/data_ika-purwanti/Code_Competence_2/dags/file/transactions.parquet")
    df_cus_feedback = pd.read_parquet(f"D:/Alterra Academy/tugas/data_ika-purwanti/Code_Competence_2/dags/file/customer_feedback.parquet")
    
    ti.xcom_push(key='df_event', value=df_event)
    ti.xcom_push(key='df_customer', value=df_customer)
    ti.xcom_push(key='df_ticket', value=df_ticket)
    ti.xcom_push(key='df_transaction', value=df_transaction)
    ti.xcom_push(key='df_cus_feedback', value=df_cus_feedback)

def transform_data(ti):
    df_transactions = ti.xcom_pull(task_ids='load_data_task', key='df_transaction')
    df_tickets = ti.xcom_pull(task_ids='load_data_task', key='df_ticket')
    df_events = ti.xcom_pull(task_ids='load_data_task', key='df_event')
    df_customer_feedback = ti.xcom_pull(task_ids='load_data_task', key='df_cus_feedback')
    
    merged_df = pd.merge(df_transactions, df_tickets, on="ticket_id", how="left")
    merged_df = pd.merge(merged_df, df_events, on="event_id", how="left")
        
    # hitung jumlah tiket 
    event_result = merged_df.groupby("event_id").sum()
    tickets_sold = event_result["quantity"]
        
    # total pendapatan
    revenue = event_result["total_amount"]
        
    # gabung table
    feedback_transactions = pd.merge(df_customer_feedback, merged_df, on="transaction_id", how="inner")
    # Analisis rating rata-rata per acara
    event_unique = feedback_transactions.groupby("event_id").mean(numeric_only=True)
    avg_rating = event_unique["rating"]
    
    # Transform data
    ti.xcom_push(key='ticket_sold_per_event', value=tickets_sold)
    ti.xcom_push(key='revenue_per_event', value=revenue)
    ti.xcom_push(key='avg_rating_per_event', value=avg_rating)

def save_to_warehouse(ti):
    ticket_sold_per_event = ti.xcom_pull(task_ids='transform_data_task', key='ticket_sold_per_event')
    revenue_per_event = ti.xcom_pull(task_ids='transform_data_task', key='revenue_per_event')
    avg_rating_per_event = ti.xcom_pull(task_ids='transform_data_task', key='avg_rating_per_event')
    
    ticket_sold_per_event = ticket_sold_per_event.reset_index()
    revenue_per_event = revenue_per_event.reset_index()
    avg_rating_per_event = avg_rating_per_event.reset_index()
    
    ticket_sold_per_event.to_parquet("Tickets_sold_per_event.parquet")
    revenue_per_event.to_parquet("Revenue_per_event.parquet")
    avg_rating_per_event.to_parquet("Feedback_analysis.parquet")
        
    with open(f"D:/Alterra Academy/tugas/data_ika-purwanti/Code_Competence_2/canvas-joy-418901-707fd80a567d.json") as f:
        service_account_info = json.load(f)
        
    credentials_info = google.oauth2.service_account.Credentials.from_service_account_info(
        service_account_info
    )
        
    storage_client = google.cloud.storage.Client(credentials=credentials_info)
    bucket = storage_client.get_bucket("penjualan_tiket_online_cc2")
        
    datetime_now = datetime.now().strftime("%Y-%m-%d")
        
    blob_ticket = bucket.blob(f"{datetime_now}/Tickets_sold_per_event.parquet")
    blob_ticket.upload_from_filename(filename="Tickets_sold_per_event.parquet")
    
    blob_revenue = bucket.blob(f"{datetime_now}/Revenue_per_event.parquet")
    blob_revenue.upload_from_filename(filename="Revenue_per_event.parquet")
    
    blob_feedback = bucket.blob(f"{datetime_now}/Feedback_analysis.parquet")
    blob_feedback.upload_from_filename(filename="Feedback_analysis.parquet")

default_args = {
    "owner":"ika",
    "retries":2,
    "retry_delay":timedelta(minutes=2),
}

with DAG(
    dag_id="code_competence_2_dag_v1",
    default_args=default_args,
    description="Code Competence 2",
    start_date=datetime(2024, 4, 20),
    schedule_interval="@daily",
) as dag:
    
    load_data_task = PythonOperator(
        task_id="load_data_task",
        python_callable=load_data, 
    )
    
    transform_data_task = PythonOperator(
        task_id="transform_data_task",
        python_callable=transform_data, 
    )
    
    save_to_warehouse_task = PythonOperator(
        task_id="save_to_warehouse_task",
        python_callable=save_to_warehouse, 
    )
    
    load_data_task >> transform_data_task >> save_to_warehouse_task