from src import data_loader


def test_load_enrollment():
    df = data_loader.load_enrollment()
    assert df is not None
    assert len(df) == 100
    expected_cols = {'district_code', 'state', 'pincode', 'year', 'month', 'enrolments'}
    assert expected_cols.issubset(set(df.columns))
