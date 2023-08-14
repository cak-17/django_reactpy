import requests

BASE_URL = "http://fracat-think.local:8080/api/products/"

def get_products(url: str=BASE_URL):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Request Status [{response.status_code} - ERROR]")
    return response.json()