import pandas as pd
import numpy as np

class DataLakeBuilder:
    def read_csv_data(self, file_path):
        df = pd.read_csv(file_path)
        return df
    
    def handle_missing_value(self, df):
        df.replace(0, np.nan, inplace=True)
        df_update = df.dropna()
        return df_update
    
    def handle_outlier(self, df, column):
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
        return df
    
    def save_to_parquet(self, df, file_name):
        return df.to_parquet(file_name)
    
    def validate_data(self, file_path):
        df = pd.read_parquet(file_path)
        return df
data_lake_builder = DataLakeBuilder()

# read csv
df_event = data_lake_builder.read_csv_data("D:/Alterra Academy/tugas/data_ika-purwanti/Code_Competence_2/data_source/events.csv")
df_customer = data_lake_builder.read_csv_data("D:/Alterra Academy/tugas/data_ika-purwanti/Code_Competence_2/data_source/customers.csv")
df_ticket = data_lake_builder.read_csv_data("D:/Alterra Academy/tugas/data_ika-purwanti/Code_Competence_2/data_source/tickets.csv")
df_transaction = data_lake_builder.read_csv_data("D:/Alterra Academy/tugas/data_ika-purwanti/Code_Competence_2/data_source/transactions.csv")
df_cus_feedback = data_lake_builder.read_csv_data("D:/Alterra Academy/tugas\data_ika-purwanti/Code_Competence_2/data_source/customer_feedback.csv")
print("Finish read CSV file")

# handle missing value
df_event = data_lake_builder.handle_missing_value(df_event)
df_customer = data_lake_builder.handle_missing_value(df_customer)
df_ticket = data_lake_builder.handle_missing_value(df_ticket)
df_transaction = data_lake_builder.handle_missing_value(df_transaction)
df_cus_feedback = data_lake_builder.handle_missing_value(df_cus_feedback)
print("Finish handling missing value")

# handle outlier
df_transaction = data_lake_builder.handle_outlier(df_transaction, "total_amount")
df_cus_feedback = data_lake_builder.handle_outlier(df_cus_feedback, "rating")
print("Finish handling outlier")

# save to parquet
data_lake_builder.save_to_parquet(df_event, "D:/Alterra Academy/tugas/data_ika-purwanti/Code_Competence_2/data_file_parquet/events.parquet")
data_lake_builder.save_to_parquet(df_customer, "D:/Alterra Academy/tugas/data_ika-purwanti/Code_Competence_2/data_file_parquet/customers.parquet")
data_lake_builder.save_to_parquet(df_ticket, "D:/Alterra Academy/tugas/data_ika-purwanti/Code_Competence_2/data_file_parquet/tickets.parquet")
data_lake_builder.save_to_parquet(df_transaction, "D:/Alterra Academy/tugas/data_ika-purwanti/Code_Competence_2/data_file_parquet/transactions.parquet")
data_lake_builder.save_to_parquet(df_cus_feedback, "D:/Alterra Academy/tugas/data_ika-purwanti/Code_Competence_2/data_file_parquet/customer_feedback.parquet")
print("Finish save to parquet file")

# validate parquet
print("\nData Event")
print(data_lake_builder.validate_data("D:/Alterra Academy/tugas/data_ika-purwanti/Code_Competence_2/data_file_parquet/events.parquet"))
print("\nData Customer")
print(data_lake_builder.validate_data("D:/Alterra Academy/tugas/data_ika-purwanti/Code_Competence_2/data_file_parquet/customers.parquet"))
print("\nData Ticket")
print(data_lake_builder.validate_data("D:/Alterra Academy/tugas/data_ika-purwanti/Code_Competence_2/data_file_parquet/tickets.parquet"))
print("\nData Transaction")
print(data_lake_builder.validate_data("D:/Alterra Academy/tugas/data_ika-purwanti/Code_Competence_2/data_file_parquet/transactions.parquet"))
print("\nData Customer Feedback")
print(data_lake_builder.validate_data("D:/Alterra Academy/tugas/data_ika-purwanti/Code_Competence_2/data_file_parquet/customer_feedback.parquet"))