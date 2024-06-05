import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import pandas as pd
import requests


def extract_data(api_url):
    response = requests.get(api_url)
    response.raise_for_status()
    if response.status_code == 200:
        products = response.json()
        df_product = pd.DataFrame(products)
        print("Successfully collect products data")
        return df_product
    else:
        print(f"Unexpected status code : {response.status_code}")
    return None

def transform_data(df):
    # get data berdasarkan price
    df["price"] = df["price"].astype(float)
    
    df = df[df["price"] > 100.00]
    df = df[["title", "price", "description", "category"]]
    
    return df

def load_data(df):
    df.to_parquet("products.parquet", index=False)
    
    cred = credentials.Certificate("D:/Alterra Academy/tugas/data_ika-purwanti/17_Data-Engineer-in-The-Cloud/accountKey.json")
    firebase_admin.initialize_app(cred, {"storageBucket": "de-with-cloud-628cf.appspot.com"})
    
    bucket = storage.bucket()
    filename = "products.parquet"
    blob = bucket.blob(filename)
    blob.upload_from_filename(filename)
    
    print("Load Products Data Success")