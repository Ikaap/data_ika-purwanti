import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import pandas as pd
import requests

def extract_data(api_url):
    response = requests.get(api_url)
    response.raise_for_status()
    if response.status_code == 200:
        transactions = response.json()
        df_transaction = pd.DataFrame(transactions)
        print("Successfully collect transaction data")
        return df_transaction
    else:
        print(f"Unexpected status code : {response.status_code}")
    return None

def transform_data(df):
    # get data berdasarkan kondisi
    df = df[(df["payment_method"] == "credit card") & (df["status"] == "success")]
    
    return df

def load_data(df):
    df.to_csv("D:/Alterra Academy/tugas/data_ika-purwanti/17_Data-Engineer-in-The-Cloud/file/transactions.csv", index=False)
    
    cred = credentials.Certificate("D:/Alterra Academy/tugas/data_ika-purwanti/17_Data-Engineer-in-The-Cloud/accountKeyFirebase.json")
    firebase_admin.initialize_app(cred, {"storageBucket": "de-with-cloud-628cf.appspot.com"})
    
    bucket = storage.bucket()
    filename = "D:/Alterra Academy/tugas/data_ika-purwanti/17_Data-Engineer-in-The-Cloud/file/transactions.csv"
    blob = bucket.blob(filename)
    blob.upload_from_filename(filename)
    
    print("Load Transactions Data Success")


df = extract_data("https://gist.githubusercontent.com/nadirbslmh/8fc9cc6cd5cbaaf5cbff63b090fb497e/raw/a7bf3e1edab88b04314a40a9de3ed744bc86d0e9/ecommerce.json")
df_result = transform_data(df)
load_data(df_result)