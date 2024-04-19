import os
import requests

from airflow.models.baseoperator import BaseOperator

def retrieve_fruits(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        if response.status_code == 200:
            fruits = response.json()
            return fruits
        else:
            print(f"Unexpected status code : {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making the request : {e}")
    
    return None

def write_sql(fruits, dirname, sql_filename):
    if fruits:
        os.makedirs(dirname, exist_ok=True)
        sql_file = os.path.join(dirname, sql_filename)
        
        with open(sql_file, 'w') as f:
            for fruit in fruits:
                insert_query = f"INSERT INTO fruits(name, calories, fat, sugar, carbohydrates, protein) VALUES('{fruit['name']}', {fruit['nutritions']['calories']}, {fruit['nutritions']['fat']}, {fruit['nutritions']['sugar']}, {fruit['nutritions']['carbohydrates']}, {fruit['nutritions']['protein']});\n"
                f.writelines(insert_query)
    else:
        print("Failed to write SQL insert file")
    
    print("SQL insert queries have been written")
    
class CollectDataFruitsOperator(BaseOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def execute(self, context):
        api_url = f"https://www.fruityvice.com/api/fruit/family/Rosaceaes"
        
        fruits = retrieve_fruits(api_url)
        write_sql(fruits, "dags/sql", "insert_data_fruits.sql")