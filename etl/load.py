from sqlalchemy import create_engine
import pandas as pd

DB_URL = "postgresql://user:password@localhost:5432/healthdb"

def load():
    engine = create_engine(DB_URL)
    df = pd.read_csv("data/processed/health_clean.csv")
    df.to_sql("health_data", engine, if_exists="replace", index=False)
    print("Load completed")

if __name__ == "__main__":
    load()