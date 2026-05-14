import pytest
import pandas as pd
from fixtures.dataset_factory import DatasetFactory
from fixtures.data_mutation import add_missing_values
from fixtures.csv_factory import create_temp_csv


def test_empty_dataset(service):
    df = DatasetFactory.empty()
    path = create_temp_csv(df)

    ds = service.load(path)

    assert ds.error is not None or ds.row_count == 0


def test_missing_values(service):
    df = DatasetFactory.simple()
    df = add_missing_values(df, rate=0.5, seed=42)

    path = create_temp_csv(df)

    ds = service.load(path)

    assert ds.dataframe.isna().sum().sum() > 0


def test_duplicate_keys(service):
    df = DatasetFactory.simple()
    path = create_temp_csv(df)

    a = service.load(path)
    b = service.load(path)

    assert a.label != b.label
    assert b.label.endswith("_1")


def test_invalid_index(service):
    df = DatasetFactory.simple()
    path = create_temp_csv(df)

    service.load(path)

    with pytest.raises(IndexError):
        service.get_by_index(999)