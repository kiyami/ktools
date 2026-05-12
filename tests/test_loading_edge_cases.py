# tests/test_loading_edge_cases.py

from app.services.data_service import DataService


def test_empty_file():
    service = DataService()

    ds = service.load("tests/data/empty.csv")

    assert ds.error is not None or ds.row_count == 0


def test_missing_values_handling():
    service = DataService()

    ds = service.load("tests/data/missing_values.csv")

    # pandas NaN üretmeli
    assert ds.dataframe.isna().sum().sum() > 0


def test_bad_format_file():
    service = DataService()

    ds = service.load("tests/data/bad_format.png")

    # ya error olmalı ya da boş dataframe
    assert ds.error is not None or ds.row_count == 0


def test_mixed_types():
    service = DataService()

    ds = service.load("tests/data/mixed_types.csv")

    assert ds.dataframe.shape[0] > 0