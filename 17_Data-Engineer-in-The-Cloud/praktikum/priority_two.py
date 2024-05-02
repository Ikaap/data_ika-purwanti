import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import pandas as pd
import requests

def extract_data(api_url):
    response = requests.get(api_url)
    response.raise_for_status()
    if response.status_code == 200:
        stock_transactions = response.json()
        df_stock_transaction = pd.DataFrame(stock_transactions)
        print("Successfully collect stock transaction data")
        return df_stock_transaction
    else:
        print(f"Unexpected status code : {response.status_code}")
    return None

def transform_data(df):
    # get data berdasarkan stock_symbol dan trade_price
    df = df[(df["stock_symbol"].isin(["GOOGL", "AMZN", "MSFT", "AAPL"])) & (df["trade_price"] > 500.00)]
    
    return df

def load_data(df):
    df.to_parquet("stock_transactions.parquet", index=False)
    
    cred = credentials.Certificate("D:/Alterra Academy/tugas/data_ika-purwanti/17_Data-Engineer-in-The-Cloud/accountKey.json")
    firebase_admin.initialize_app(cred, {"storageBucket": "de-with-cloud-628cf.appspot.com"})
    
    bucket = storage.bucket()
    filename = "stock_transactions.parquet"
    blob = bucket.blob(filename)
    blob.upload_from_filename(filename)
    
    print("Load Stock Transactions Data Success")


df = extract_data("https://gist.githubusercontent.com/nadirbslmh/93b62fdcfa694d4ec07bed9b3c94e401/raw/c07971341361e23fd4f3a880437c4d8e4ebcfafc/stock_trades.json")
df_result = transform_data(df)
load_data(df_result)