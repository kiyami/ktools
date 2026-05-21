import pandas as pd
import numpy as np

from PySide6.QtCore import (
    QAbstractTableModel,
    QModelIndex,
    Qt,
)


class DatasetTableModel(QAbstractTableModel):

    def __init__(self, dataset=None):
        super().__init__()

        self._dataset = dataset

    # =====================================================
    # INTERNAL
    # =====================================================

    @property
    def dataframe(self) -> pd.DataFrame:

        if self._dataset is None:
            return pd.DataFrame()

        return self._dataset.dataframe

    # =====================================================
    # SIZE
    # =====================================================

    def rowCount(self, parent=QModelIndex()):

        if parent.isValid():
            return 0

        return len(self.dataframe.index)

    def columnCount(self, parent=QModelIndex()):

        if parent.isValid():
            return 0

        return len(self.dataframe.columns)

    # =====================================================
    # DATA
    # =====================================================

    def data(self, index, role=Qt.DisplayRole):

        if not index.isValid():
            return None

        row = index.row()
        col = index.column()

        value = self.dataframe.iat[row, col]

        # -------------------------
        # DISPLAY
        # -------------------------
        if role == Qt.DisplayRole:

            if pd.isna(value):
                return ""

            if isinstance(value, float):
                return f"{value:.4f}"

            return str(value)

        # -------------------------
        # ALIGNMENT
        # -------------------------
        if role == Qt.TextAlignmentRole:

            if isinstance(value, (int, float)):
                return Qt.AlignRight | Qt.AlignVCenter

            return Qt.AlignLeft | Qt.AlignVCenter

        # -------------------------
        # TOOLTIP
        # -------------------------
        if role == Qt.ToolTipRole:
            return str(value)

        return None

    # =====================================================
    # HEADERS
    # =====================================================

    def header_data(self, section, orientation, role):

        if role != Qt.DisplayRole:
            return None

        if orientation == Qt.Horizontal:
            return str(self.dataframe.columns[section])

        if orientation == Qt.Vertical:
            return str(self.dataframe.index[section])

        return None

    # =====================================================
    # FLAGS
    # =====================================================

    def flags(self, index):

        if not index.isValid():
            return Qt.NoItemFlags

        return (
            Qt.ItemIsEnabled
            | Qt.ItemIsSelectable
            | Qt.ItemIsEditable
        )

    # =====================================================
    # EDITING
    # =====================================================

    def setData(self, index, value_str, role=Qt.EditRole):

        if role != Qt.EditRole:
            return False
        
        print(type(index))

        row = index.row()
        col = index.column()

        try:

            if value_str == "":
                _value = np.nan
            else:
                _value = float(value_str)

            self.dataframe.iat[row, col] = _value

            self.dataChanged.emit(
                index,
                index,
                [Qt.DisplayRole]
            )

            self._dataset.add_history(_value, index)

            return True

        except Exception as e:
            print("exception")
            print(e)
            return False

    # =====================================================
    # SORTING
    # =====================================================

    def sort(self, column, order):

        col_name = self.dataframe.columns[column]

        ascending = order == Qt.AscendingOrder

        self.layoutAboutToBeChanged.emit()

        self._dataset.dataframe = (
            self.dataframe
            .sort_values(
                by=col_name,
                ascending=ascending,
                kind="mergesort"
            )
            .reset_index(drop=True)
        )

        self.layoutChanged.emit()

    # =====================================================
    # UPDATE
    # =====================================================

    def set_dataset(self, dataset):

        self.beginResetModel()

        self._dataset = dataset

        self.endResetModel()

    def clear(self):

        self.beginResetModel()

        self._dataset = None

        self.endResetModel()