from fixtures.dataset_factory import DatasetFactory
from fixtures.csv_factory import create_temp_csv


def test_remove_updates_state(service):
    df = DatasetFactory.simple()
    path = create_temp_csv(df)

    ds = service.load(path)
    service.remove(ds.label)

    assert service.count() == 0
    assert service.keys() == []


def test_clear_resets_everything(service):
    df = DatasetFactory.simple()
    path = create_temp_csv(df)

    service.load(path)
    service.load(path)

    service.clear()

    assert service.count() == 0
    assert len(service.keys()) == 0


def test_order_persists_after_operations(service):
    df = DatasetFactory.simple()
    path = create_temp_csv(df)

    a = service.load(path)
    b = service.load(path)
    c = service.load(path)

    service.remove(b.label)

    assert service.keys() == [a.label, c.label]