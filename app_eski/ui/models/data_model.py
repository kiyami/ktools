from PySide6.QtCore import Qt, QAbstractListModel, QModelIndex


class DataModel(QAbstractListModel):
    def __init__(self, data=None):
        super().__init__()
        self._data = data or []

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def data(self, index, role):
        if not index.isValid():
            return None

        item = self._data[index.row()]
        x, y = item

        if role == Qt.DisplayRole:
            return f"{index.row()} → x: {x}, y: {y}"

        if role == Qt.UserRole:
            return item  # (x, y)

        return None

    def set_data(self, data):
        self.beginResetModel()
        self._data = data
        self.endResetModel()

    def get_item(self, index):
        return self._data[index]