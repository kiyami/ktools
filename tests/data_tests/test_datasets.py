import pandas as pd
from app.models.dataset import Dataset


def test_headers():
    df = pd.DataFrame({"a": [1], "b": [2]})
    d = Dataset("test", df)

    assert d.headers == ["a", "b"]


def test_shape():
    df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    d = Dataset("test", df)

    assert d.shape == (2, 2)


def test_row_and_column_count():
    df = pd.DataFrame({"x": [1, 2, 3]})
    d = Dataset("test", df)

    assert d.row_count == 3
    assert d.column_count == 1


def test_get_column():
    df = pd.DataFrame({"x": [10, 20, 30]})
    d = Dataset("test", df)

    assert d.get_column("x").tolist() == [10, 20, 30]