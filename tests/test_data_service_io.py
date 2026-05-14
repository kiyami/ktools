import os
from fixtures.dataset_factory import DatasetFactory
from fixtures.csv_factory import create_temp_csv


def test_save_csv(service):
    df = DatasetFactory.simple()
    path = create_temp_csv(df)

    ds = service.load(path)

    out_path = path.replace(".csv", "_out.csv")

    service.save_csv(ds.label, out_path)

    assert os.path.exists(out_path)


def test_load_and_save_roundtrip(service):
    df = DatasetFactory.simple()
    path = create_temp_csv(df)

    ds = service.load(path)

    out = path.replace(".csv", "_copy.csv")
    service.save_csv(ds.label, out)

    ds2 = service.load(out)

    assert ds2.row_count == ds.row_count