import pytest
import pandas as pd
from app.services.data_service import DataService


@pytest.fixture
def service():
    return DataService()


@pytest.fixture
def simple_df():
    return pd.DataFrame({
        "x": [1, 2, 3],
        "y": [4, 5, 6]
    })