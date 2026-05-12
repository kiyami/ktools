# tests/test_data_service.py

from app.services.data_service import DataService
import pytest


def test_add_and_get():
    service = DataService()

    ds = service.load("tests/data/valid_simple.csv")

    assert service.count() == 1
    assert service.get(ds.label).row_count == 3


def test_remove():
    service = DataService()

    ds = service.load("tests/data/valid_simple.csv")
    service.remove(ds.label)

    assert service.count() == 0


def test_order_consistency():
    service = DataService()

    a = service.load("tests/data/valid_simple.csv")
    b = service.load("tests/data/valid_simple.csv")

    assert service.keys() == [a.label, b.label]


def test_duplicate_keys():
    service = DataService()

    a = service.load("tests/data/valid_simple.csv")
    b = service.load("tests/data/valid_simple.csv")

    assert a.label != b.label
    assert a.label == "valid_simple"
    assert b.label == "valid_simple_1"


def test_order_after_remove():
    service = DataService()

    a = service.load("tests/data/valid_simple.csv")
    b = service.load("tests/data/valid_simple.csv")
    c = service.load("tests/data/valid_simple.csv")

    service.remove(b.label)

    assert service.keys() == [a.label, c.label]


def test_get_by_index():
    service = DataService()

    a = service.load("tests/data/valid_simple.csv")
    b = service.load("tests/data/valid_simple.csv")

    assert service.get_by_index(0).label == a.label
    assert service.get_by_index(1).label == b.label


def test_get_by_index_out_of_range():
    service = DataService()

    service.load("tests/data/valid_simple.csv")

    with pytest.raises(IndexError):
        service.get_by_index(10)


def test_clear_resets_state():
    service = DataService()

    service.load("tests/data/valid_simple.csv")
    service.load("tests/data/valid_simple.csv")

    service.clear()

    assert service.count() == 0
    assert service.keys() == []