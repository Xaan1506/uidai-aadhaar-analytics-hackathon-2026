import pandas as pd


def load_csv(path: str) -> pd.DataFrame:
    """Load a CSV file into a pandas DataFrame."""
    return pd.read_csv(path)


def load_enrollment(path: str = "data/sample/enrollment_sample_100rows.csv") -> pd.DataFrame:
    return load_csv(path)


def load_demographic_update(path: str = "data/sample/demographic_update_sample_100rows.csv") -> pd.DataFrame:
    return load_csv(path)


def load_biometric_update(path: str = "data/sample/biometric_update_sample_100rows.csv") -> pd.DataFrame:
    return load_csv(path)
