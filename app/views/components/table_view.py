from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableView
from PySide6.QtCore import Signal


class TableView(QWidget):

    cell_selected = Signal(str)

    def __init__(self):
        super().__init__()

        self.table = QTableView()

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)

    def _on_selection_changed(self, selected, _deselected):
        indexes = selected.indexes()

        if not indexes:
            return

        index = indexes[0]  # ilk seçili hücre
        value = index.data()

        self.cell_selected.emit(str(value))

    def set_model(self, model):
        self.table.setModel(model)

        # 🔥 SELECTION LISTENER (kritik kısım)
        self.table.selectionModel().selectionChanged.connect(self._on_selection_changed)