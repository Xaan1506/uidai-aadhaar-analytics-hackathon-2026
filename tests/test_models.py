from src import data_loader, models


def test_simple_trend():
    df = data_loader.load_enrollment()
    val = models.simple_trend(df)
    assert isinstance(val, float)
    assert -1.0 <= val <= 1.0
