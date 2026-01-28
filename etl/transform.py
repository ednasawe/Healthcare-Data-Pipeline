python

import pandas as pd

def transform():
    df = pd.read_csv("data/raw/health.csv")
    df.dropna(inplace=True)
    df.columns = [c.lower().replace(" ", "_") for c in df.columns]
    df.to_csv("data/processed/health_clean.csv", index=False)
    print("Transform completed")

if __name__ == "__main__":
    transform()