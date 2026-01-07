import pandas as pd


def compute_enrolment_rate(df: pd.DataFrame, population_col: str = 'total_population', enrol_col: str = 'enrolments') -> pd.DataFrame:
    """Compute enrolment rate per 1000 population and return dataframe with new column."""
    df = df.copy()
    if population_col not in df.columns or enrol_col not in df.columns:
        raise ValueError('Expected columns not found in dataframe')
    df['enrolment_rate_per_1000'] = (df[enrol_col] / df[population_col]) * 1000
    return df
