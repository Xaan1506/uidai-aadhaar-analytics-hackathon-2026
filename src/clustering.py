import pandas as pd


def basic_groupby_mean(df: pd.DataFrame, by: str, col: str) -> pd.DataFrame:
    return df.groupby(by)[col].mean().reset_index()
