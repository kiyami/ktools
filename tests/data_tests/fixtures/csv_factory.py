from __future__ import annotations

import pandas as pd
import tempfile


def create_temp_csv(df: pd.DataFrame) -> str:
    """
    DataFrame'i geçici CSV dosyasına çevirir ve path döner.
    Testlerde IO izolasyonu sağlar.
    """

    tmp = tempfile.NamedTemporaryFile(suffix=".csv", delete=False)
    df.to_csv(tmp.name, index=False)

    return tmp.name