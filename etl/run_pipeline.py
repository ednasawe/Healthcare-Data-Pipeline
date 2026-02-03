from extract import extract
from transform import transform
from load import load
import logging

logging.basicConfig(level=logging.INFO)

def run():
    logging.info("Starting ETL")
    df = extract()
    df = transform(df)
    load(df)
    logging.info("ETL completed")

#if __name__ == " __main__":
#run()