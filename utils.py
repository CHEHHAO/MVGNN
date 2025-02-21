import numpy as np
import torch
import pandas as pd
import polars as pl


def load_data(path):
    df = pl.read_csv(path)
    lf = df.lazy()
    return df

def split_data(df):
    pass

if __name__ == "__main__":
    df = load_data("data/datashare.csv")
    print(df)