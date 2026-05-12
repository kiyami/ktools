# tests/test_dataset.py

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


def test_column_access():
    df = pd.DataFrame({"x": [10, 20, 30]})
    d = Dataset("test", df)

    col = d.get_column("x")

    assert col.tolist() == [10, 20, 30]