import numpy as np
import torch
import pandas as pd
import polars as pl
from datetime import datetime


def load_data(path):
    df = pl.read_csv(path)
    lf = df.lazy()
    return df


def save_unique_permnos(df, path):
    # 获取唯一的 permno 并保存为 txt 文件
    unique_permnos = df.select(pl.col("permno").unique()).to_series().to_list()
    with open(path, 'w') as f:
        for permno in unique_permnos:
            f.write(f"{permno}\n")


def data_info(df):
    print(df.shape)
    # 查看过滤后的 DATE 范围（以整数形式获取最小和最大值）
    min_date = df.select(pl.col("DATE").min()).to_series()[0]
    max_date = df.select(pl.col("DATE").max()).to_series()[0]
    print(f"\n过滤后的数据 DATE 范围（整数格式）：最小值 = {min_date}, 最大值 = {max_date}")

    # 如果希望将整数格式转换为 datetime 格式，可以使用如下函数
    def int_to_date(date_int):
        return datetime.strptime(str(date_int), "%Y%m%d")

    print(f"转换后：最小日期 = {int_to_date(min_date)}, 最大日期 = {int_to_date(max_date)}")

    # 统计唯一的 permno 数量
    permno_count = df.select(pl.col("permno").n_unique()).to_series()[0]
    print(f"\n唯一 permno 数量：{permno_count}")


def split_data(df):
    pass

if __name__ == "__main__":
    df = load_data("data/sub6_data.csv")
    data_info(df)