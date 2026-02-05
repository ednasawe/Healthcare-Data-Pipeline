from core.logger import get_logger
from extract import extract
from transform import transform
from load import load

logger = get_logger(__name__)

def run():
    logger.info("Starting ETL pipeline")

    df = extract()
    logger.info(f"Ectracted {len(df)} records")

    df = transform(df)
    logger.info("Transformation completed")

    load(df)
    logger.info("Data loaded into database")

if __name__ == " __main__":
    run()