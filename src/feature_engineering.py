import pandas as pd


def add_month_index(df: pd.DataFrame) -> pd.DataFrame:
    """Add a simple month index useful for trend analysis."""
    df = df.copy()
    df['month_index'] = (df['year'] - df['year'].min()) * 12 + df['month']
    return df
