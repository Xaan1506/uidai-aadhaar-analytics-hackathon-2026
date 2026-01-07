import numpy as np
import pandas as pd


def simple_trend(df: pd.DataFrame, value_col: str = 'enrolments') -> float:
    """Return Pearson correlation between month index and a value column as a simple trend indicator."""
    if 'month' in df.columns:
        x = df['month'].astype(float)
    elif 'month_index' in df.columns:
        x = df['month_index'].astype(float)
    else:
        # fallback to row order
        x = np.arange(len(df), dtype=float)

    y = df[value_col].astype(float)
    if len(x) < 2:
        return 0.0
    # compute Pearson correlation
    vx = x - x.mean()
    vy = y - y.mean()
    denom = np.sqrt((vx ** 2).sum() * (vy ** 2).sum())
    if denom == 0:
        return 0.0
    corr = (vx * vy).sum() / denom
    return float(corr)
