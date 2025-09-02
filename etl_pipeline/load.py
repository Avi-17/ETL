from sqlalchemy import create_engine
from .config import DB_URI, TABLE_NAME

def load_data(df):
    engine = create_engine(DB_URI)
    df.to_sql(TABLE_NAME, engine, index=False, if_exists="replace")
    print(f"Latest Covid Data loaded into {TABLE_NAME}")