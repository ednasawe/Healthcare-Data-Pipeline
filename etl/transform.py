
import pandas as pd

def transform(df):
    # Example transformations
    df.columns = df.columns.str.lower()
    df = df.drop_duplicates()
    return df