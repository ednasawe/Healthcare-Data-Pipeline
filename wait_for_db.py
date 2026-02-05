import time
import os
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

raw_url = os.getenv("DATABASE_URL")

if not raw_url:
    raise RuntimeError("DATABASE_URL is not set")

DB_URL = raw_url.strip()

print(f"Using DATABASE_URL: {DB_URL}")

def wait_for_db(retries=10, delay=3):
    engine = create_engine(DB_URL)

    for i in range(retries):
        try:
            with engine.connect() as conn:
                conn.execute("SELECT 1")

            print("Database is ready")
            return
        except OperationalError:
            print(f"Database not ready, retrying ({i+1}/{retries})...")
            time.sleep(delay)

    raise RuntimeError("Database never became available")

if __name__ == "__main__":
    wait_for_db()