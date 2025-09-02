import requests
import pandas as pd
from .config import API_URL

def extract_data():
    response = requests.get(API_URL)
    response.raise_for_status
    data = response.json()
    return pd.DataFrame(data)

