import requests

from airflow.models.baseoperator import BaseOperator

def retrieve_products(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        if response.status_code == 200:
            products = response.json()
            print(products)
            print("Successfully collect data products")
            return products
        else:
            print(f"Unexpected status code : {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making the request : {e}")
    
    return None

class CollectDataProductsOperator(BaseOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def execute(self, context):
        api_url = f"https://fakestoreapi.com/products"
        return retrieve_products(api_url)