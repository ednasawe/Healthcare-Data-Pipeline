import pandas as pd

DATA_URL = "https://raw.githubusercontent.com/...csv"

def extract():
    df = pd.read_csv(DATA_URL)
    df.to_csv("data/raw/health.csv", index=False)
    print("Extract completed")


if __name__ == "__main__":
    extract()