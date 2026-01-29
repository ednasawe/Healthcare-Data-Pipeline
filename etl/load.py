import os
from sqlalchemy import create_engine
import pandas as pd

DB_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/healthdb")

def load():
    engine = create_engine(DB_URL)
    df = pd.read_csv("data/processed/life_expectancy_clean.csv")
    df.to_sql("life_expectancy", engine, if_exists="replace", index=False)
    #print("Load completed")

if __name__ == "__main__":
    load()