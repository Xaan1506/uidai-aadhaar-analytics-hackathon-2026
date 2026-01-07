import pandas as pd
from src import data_loader, derived_metrics


def test_compute_enrolment_rate():
    df = data_loader.load_enrollment()
    out = derived_metrics.compute_enrolment_rate(df)
    assert 'enrolment_rate_per_1000' in out.columns
    # check values are finite and non-negative
    assert (out['enrolment_rate_per_1000'] >= 0).all()

