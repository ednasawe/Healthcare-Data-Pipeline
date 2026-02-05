import pandas as pd


def extract():
    return pd.read_csv("etl/datasets/diabetes.csv")
    


#if __name__ == "__main__":
 #   extract()