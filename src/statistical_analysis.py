import numpy as np
import pandas as pd


def rolling_mean(df: pd.DataFrame, col: str, window: int = 3) -> pd.Series:
    return df[col].rolling(window=window, min_periods=1).mean()
