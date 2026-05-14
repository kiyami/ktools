import pandas as pd
import numpy as np


def add_missing_values(df: pd.DataFrame, rate: float = 0.1, seed: int | None = None) -> pd.DataFrame:
    """
    DataFrame içine kontrollü missing value ekler.
    Sadece test amaçlı kullanılır.
    """

    df = df.copy()

    if seed is not None:
        np.random.seed(seed)

    mask = np.random.rand(*df.shape) < rate
    df[mask] = None

    return df