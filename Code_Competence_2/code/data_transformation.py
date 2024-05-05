import pandas as pd
import google.cloud.storage
from datetime import datetime
import json 

class DataWarehouseLoader:
    def load_data(self, file_path):
        df = pd.read_parquet(file_path)
        return df
    
    def transform_data(self, df_transactions, df_tickets, df_events, df_customer_feedback):
        # gabung data
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
        
        return tickets_sold, revenue, avg_rating
    
    def save_to_warehouse(self, df, table_name):
        df.to_parquet(table_name)
        
        with open(f"D:/Alterra Academy/tugas/data_ika-purwanti/Code_Competence_2/canvas-joy-418901-707fd80a567d.json") as f:
            service_account_info = json.load(f)
        
        credentials_info = google.oauth2.service_account.Credentials.from_service_account_info(
            service_account_info
        )
        
        storage_client = google.cloud.storage.Client(credentials=credentials_info)
        bucket = storage_client.get_bucket("penjualan_tiket_online_cc2")
        
        datetime_now = datetime.now().strftime("%Y-%m-%d")
        
        blob = bucket.blob(f"{datetime_now}/{table_name}")
        blob.upload_from_filename(filename=table_name)
        
        return True

data_warehouse_load = DataWarehouseLoader()

df_event = data_warehouse_load.load_data("D:/Alterra Academy/tugas/data_ika-purwanti/Code_Competence_2/data_file_parquet/events.parquet")
df_customer = data_warehouse_load.load_data("D:/Alterra Academy/tugas/data_ika-purwanti/Code_Competence_2/data_file_parquet/customers.parquet")
df_ticket = data_warehouse_load.load_data("D:/Alterra Academy/tugas/data_ika-purwanti/Code_Competence_2/data_file_parquet/tickets.parquet")
df_transaction = data_warehouse_load.load_data("D:/Alterra Academy/tugas/data_ika-purwanti/Code_Competence_2/data_file_parquet/transactions.parquet")
df_customer_feedback = data_warehouse_load.load_data("D:/Alterra Academy/tugas/data_ika-purwanti/Code_Competence_2/data_file_parquet/customer_feedback.parquet")
print("Finish load data")

ticket_sold_per_event, revenue_per_event, avg_rating_per_event = data_warehouse_load.transform_data(df_transaction, df_ticket, df_event, df_customer_feedback)
print("Finish transform data")

data_warehouse_load.save_to_warehouse(ticket_sold_per_event.reset_index(), "Tickets_sold_per_event.parquet")
data_warehouse_load.save_to_warehouse(revenue_per_event.reset_index(), "Revenue_per_event.parquet")
data_warehouse_load.save_to_warehouse(avg_rating_per_event.reset_index(), "Feedback_analysis.parquet")
print("Finish upload data")