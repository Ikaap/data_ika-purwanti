import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import pandas as pd

def extract_data(file):
    df = pd.read_csv(file)
    return df

def transform_data(df):
    # menghapus data duplikat
    df = df.drop_duplicates()
    
    # menghapus data tidak lengkap
    df = df.replace('-', pd.NA)
    df  = df.dropna(subset=['age', 'favorite_front_end', 'favorite_back_end', 'salary_per_year_in_USD'], how='any')
    
    df = df.reset_index(drop=True)
    
    return df

def load_data(df):
    cred = credentials.Certificate("D:/Alterra Academy/tugas/data_ika-purwanti/17_Data-Engineer-in-The-Cloud/accountKeyFirebase.json")
    firebase_admin.initialize_app(cred, {"storageBucket": "de-with-cloud-628cf.appspot.com"})
    
    bucket = storage.bucket()
    filename = "D:/Alterra Academy/tugas/data_ika-purwanti/17_Data-Engineer-in-The-Cloud/file/survey.csv"
    df.to_csv(filename)
    
    blob = bucket.blob(filename)
    blob.upload_from_filename(filename)
    
    print("Load Survey Data Success")


df = extract_data("D:/Alterra Academy/tugas/data_ika-purwanti/17_Data-Engineer-in-The-Cloud/praktikum/source/survey.csv")
df_result = transform_data(df)
load_data(df_result)