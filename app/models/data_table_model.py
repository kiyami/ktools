# app/models/data_table_model.py

from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex


class DataTableModel(QAbstractTableModel):

    def __init__(self, columns=None, colnames=None):
        super().__init__()
        self._columns = columns or []
        self._colnames = colnames or []

    def rowCount(self, parent=QModelIndex()):
        if not self._columns:
            return 0
        return len(self._columns[0])

    def columnCount(self, parent=QModelIndex()):
        return len(self._columns)

    def data(self, index, role):
        if not index.isValid():
            return None

        row = index.row()
        col = index.column()

        value = self._columns[col][row]

        # numpy scalar fix
        if hasattr(value, "item"):
            value = value.item()

        if role == Qt.DisplayRole:
            return value

        return None

    # 🔥 HEADER (colname_1 colname_2)
    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None

        if orientation == Qt.Horizontal:
            return self._colnames[section]

        if orientation == Qt.Vertical:
            return str(section)

        return None

    def set_data(self, columns, colnames):
        self.beginResetModel()
        self._columns = columns
        self._colnames = colnames
        self.endResetModel()