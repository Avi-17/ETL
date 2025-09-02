# ETL Pipeline Project

A simple ETL (Extract, Transform, Load) pipeline built in Python to fetch, clean, and load COVID-19 data into a PostgreSQL database hosted on neonDB.

## Features
- **Extract**: Fetches the COVID-19 dataset from an open API.
- **Transform**: Cleans data and adds derived metrics such as death rates.
- **Load**: Stores the processed data into PostgreSQL for further analysis.

## Tech Stack
- Python (pandas, requests, SQLAlchemy)
- PostgreSQL (hosted on neonDB)
- dotenv for configuration management

## Project Structure
etl_pipeline/
├── extract.py
├── transform.py
├── load.py
├── config.py
└── init.py
main.py
.env.example
requirements.txt


## How to Run
1. Clone the repo  
   git clone https://github.com/Avi-17/ETL.git

2. Install dependencies
    pip install -r requirements.txt

3. Set up .env file with your DB credentials (see .env.example)

4. To run the pipeline: python3 main.py
