import os
from sqlalchemy import create_engine
import pandas as pd

raw_url = os.getenv("DATABASE_URL")
if not raw_url:
    raise RuntimeError("DATABASE_URL is not set")

DB_URL = raw_url.strip()

def load():
    engine = create_engine(DB_URL)
    df = pd.read_csv("etl/datasets/diabetes.csv")
    df.to_sql("diabetes_data", engine, if_exists="replace", index=False)
    print("Load completed")

if __name__ == "__main__":
    load()