from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

#import numpy as np
import pandas as pd

from PySide6.QtCore import QModelIndex


class _Commit:

    def __init__(
        self,
        value: Any,
        index: QModelIndex | None
    ):

        self.value = value
        self.index = index

        self.prev_commit: _Commit | None = None
        self.next_commit: _Commit | None = None

    def add_next(
        self,
        value: Any,
        index: QModelIndex
    ) -> _Commit:

        new_commit = _Commit(value, index)

        new_commit.prev_commit = self

        # redo geçmişi burada koparılır
        self.next_commit = new_commit

        return new_commit


class History:

    head = _Commit(None, None)

    current: _Commit = head

    @classmethod
    def make_commit(
        cls,
        value: Any,
        index: QModelIndex
    ):

        cls.current = cls.current.add_next(
            value,
            index
        )

    @classmethod
    def undo(cls):

        # head'e kadar geri git
        if cls.current is cls.head:
            return None

        commit = cls.current

        cls.current = commit.prev_commit

        return (
            commit.value,
            commit.index
        )

    @classmethod
    def redo(cls):

        if cls.current.next_commit is None:
            return None

        cls.current = cls.current.next_commit

        return (
            cls.current.value,
            cls.current.index
        )


@dataclass(slots=True)
class Dataset:

    label: str
    dataframe: pd.DataFrame

    path: Path | None = None
    error: str | None = None

    metadata: dict = field(default_factory=dict)

    history: History = History()

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
    # HISTORY
    # -------------------------
    def add_history(self, value, index):
        self.history.make_commit(value, index)
        print("added to history")
        print(self.history.current)

    def undo_history(self):
        value, index = self.history.undo()
        return value, index

    def redo_history(self):
        value, index = self.history.redo()
        return value, index
    
    # -------------------------
    # EXPORT
    # -------------------------
    def to_csv(self, path: str):
        self.dataframe.to_csv(path, index=False)