from dataclasses import dataclass, field
from pathlib import Path

#import numpy as np
import pandas as pd


@dataclass(slots=True)
class Dataset:

    label: str
    dataframe: pd.DataFrame

    path: Path | None = None
    error: str | None = None

    metadata: dict = field(default_factory=dict)

    # -------------------------
    # BASIC INFO
    # -------------------------
    @property
    def headers(self) -> list[str]:
        return self.dataframe.columns.tolist()

    @property
    def shape(self) -> tuple[int, int]:
        return self.dataframe.shape

    @property
    def row_count(self) -> int:
        return len(self.dataframe)

    @property
    def column_count(self) -> int:
        return len(self.dataframe.columns)


    def get_column(self, column: str) -> pd.Series:
        return self.dataframe[column]

    # -------------------------
    # EXPORT
    # -------------------------
    def to_csv(self, path: str):
        self.dataframe.to_csv(path, index=False)