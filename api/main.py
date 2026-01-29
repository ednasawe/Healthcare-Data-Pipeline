import os
from fastapi import FastAPI
from sqlalchemy import create_engine
import pandas as pd

app = FastAPI()
DB_URL =os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/healthdb")
engine = create_engine("DB_URL")


@app.get("/health")
def get_data(limit: int = 10):
    df = pd.read_sql("SELECT * FROM health_data LIMIT %s", engine, params=[limit])
    return df.to_dict(orient="records")