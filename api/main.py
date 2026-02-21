import os
from database.wait_for_db import wait_for_db
from fastapi import FastAPI
from sqlalchemy import create_engine, text
import pandas as pd
from core.logger import get_logger

logger = get_logger(__name__)

raw_url = os.getenv("DATABASE_URL")
if not raw_url:
    raise RuntimeError("DATABASE_URL is not set")

DB_URL = raw_url.strip()

print(f"API using DATABASE_URL: {DB_URL}")

engine = create_engine(DB_URL)

wait_for_db()

app = FastAPI()


@app.get("/health")
def get_data(limit: int = 10):
    try:
        logger.info(f"Fetching {limit} healthcare records")

        query = text("SELECT * FROM records LIMIT :limit")
        with engine.connect() as conn:
            df = pd.read_sql(query, conn, params={"limit": limit})

        return df.to_dict(orient="records")

    except Exception as e:
        logger.error(f"Error fetching data: {str(e)}")
        return {"error": str(e)}