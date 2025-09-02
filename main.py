from etl_pipeline.extract import extract_data
from etl_pipeline.transform import transform_data
from etl_pipeline.load import load_data

def run_etl_pipeline():
    df = extract_data()
    df = transform_data(df)
    load_data(df)
    return

if __name__=="__main__":
    run_etl_pipeline()