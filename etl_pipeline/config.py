import os
from dotenv import load_dotenv

load_dotenv()

DB_URI=os.getenv("DB_URI")
API_URL="https://disease.sh/v3/covid-19/countries"
TABLE_NAME="covid_data"