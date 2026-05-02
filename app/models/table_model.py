from PySide6.QtCore import QAbstractTableModel, Qt


class TableModel(QAbstractTableModel):

    def __init__(self):
        super().__init__()
        self._data = None
        self._headers = []

    def rowCount(self, parent=None):
        return 0 if self._data is None else self._data.shape[0]

    def columnCount(self, parent=None):
        return 0 if self._data is None else self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return str(self._data[index.row(), index.column()])
        return None

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None

        if orientation == Qt.Horizontal:
            return self._headers[section] if section < len(self._headers) else str(section)

        if orientation == Qt.Vertical:
            return str(section + 1)

    def set_data(self, data, headers):
        self.beginResetModel()
        self._data = data
        self._headers = headers
        self.endResetModel()