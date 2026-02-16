from core.logger import get_logger
from etl.extract import extract
from etl.transform import transform
from etl.load import load

logger = get_logger(__name__)

def run():
    logger.info("Starting ETL pipeline")

    df = extract()
    logger.info(f"Extracted {len(df)} records")

    df = transform(df)
    logger.info("Transformation completed")

    load(df)
    logger.info("Data loaded into database")

if __name__ == "__main__":
    run()
