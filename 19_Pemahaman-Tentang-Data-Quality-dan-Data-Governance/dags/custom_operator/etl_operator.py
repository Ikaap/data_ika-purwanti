import pandas as pd
import requests


def extract_data(api_url):
    response = requests.get(api_url)
    response.raise_for_status()
    if response.status_code == 200:
        transactions = response.json()
        df_transaction = pd.DataFrame(transactions)
        
        print(df_transaction.info())
        print(df_transaction['phone_number'])
        
        print("Successfully collect products data")
        return df_transaction
    else:
        print(f"Unexpected status code : {response.status_code}")
    return None

def number_phone_format(x):
    x = str(x)
    x = '+62' + x
    return x

def transaction_amount_format(x):
    x = "Rp {:,.0f}".format(x)
    x = x.replace(",",".")
    return x

def transform_data(df):
    # format nomor telepon
    
    # df["phone_number"] = df["phone_number"].astype(int)
    # df["phone_number"] = df["phone_number"].apply(lambda x: number_phone_format(x))
    
    # df['phone_number'] = df['phone_number'].astype(str) 
    # df['phone_number'] = df['phone_number'].apply(lambda x: '+62' + x)
    
    # print(df.info())
    # print(df['phone_number'])
    
    df["phone_number"] = df["phone_number"].apply(lambda x: "+62" + str(x))
    
    # print(df.info())
    # print(df['phone_number'])
    
    # format transaction amount
    df["transaction_amount"] = df["transaction_amount"].apply(lambda x: transaction_amount_format(x))
    
    # get data
    df = df[df["transaction_status"] == "success"]
    
    df = df.reset_index(drop=True)
    return df