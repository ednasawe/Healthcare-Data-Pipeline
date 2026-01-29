import os
import logging
from fastapi import FastAPI
from sqlalchemy import create_engine
import pandas as pd

logging.basicConfig(level=logging.INFO)

DB_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/healthdb")

engine = create_engine(DB_URL)
app = FastAPI()


@app.get("/health")
def get_data(limit: int = 10):
    df = pd.read_sql(f"SELECT * FROM life_expectancy {LIMIT}", engine,)
    return df.to_dict(orient="records")