from fixtures.dataset_factory import DatasetFactory
from fixtures.csv_factory import create_temp_csv


def test_load_single_dataset(service):
    df = DatasetFactory.simple()
    path = create_temp_csv(df)

    ds = service.load(path)

    assert service.count() == 1
    assert ds.row_count == 3
    assert ds.column_count == 2


def test_get_by_key(service):
    df = DatasetFactory.simple()
    path = create_temp_csv(df)

    ds = service.load(path)

    fetched = service.get(ds.label)

    assert fetched.row_count == ds.row_count


def test_get_all_returns_ordered(service):
    df = DatasetFactory.simple()
    path = create_temp_csv(df)

    a = service.load(path)
    b = service.load(path)

    all_data = service.get_all()

    assert all_data[0].label == a.label
    assert all_data[1].label == b.label