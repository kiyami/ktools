from PySide6.QtCore import QAbstractTableModel, Qt


class TableModel(QAbstractTableModel):

    def __init__(self):
        super().__init__()
        self._data = None  # list[list[str]]
        self._headers = []

    # =========================
    # SIZE
    # =========================
    def rowCount(self, parent=None):
        return 0 if not self._data else len(self._data)

    def columnCount(self, parent=None):
        if not self._data:
            return 0
        return max(len(row) for row in self._data)

    # =========================
    # DATA
    # =========================
    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or not self._data:
            return None

        if role == Qt.DisplayRole:
            row = index.row()
            col = index.column()

            try:
                return str(self._data[row][col])
            except IndexError:
                return ""

        return None

    # =========================
    # HEADERS
    # =========================
    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None

        if not self._data:
            return None

        if orientation == Qt.Horizontal:
            if section < len(self._headers):
                return self._headers[section]
            return f"Col {section + 1}"

        if orientation == Qt.Vertical:
            return str(section + 1)

        return None

    # =========================
    # UPDATE
    # =========================
    def set_data(self, data, headers):
        self.beginResetModel()
        self._data = data
        self._headers = headers or []
        self.endResetModel()
