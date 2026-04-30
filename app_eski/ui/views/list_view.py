from PySide6.QtWidgets import QWidget, QVBoxLayout, QListView
from PySide6.QtCore import Signal
from ui.models.data_model import DataModel


class DataListView(QWidget):
    item_selected = Signal(float, float, int)

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.view = QListView()
        self.model = DataModel()

        self.view.setModel(self.model)

        layout.addWidget(self.view)
        self.setLayout(layout)

        # seçim eventi
        self.view.clicked.connect(self.on_item_clicked)

    def set_data(self, x_list, y_list):
        data = list(zip(x_list, y_list))
        self.model.set_data(data)

    def on_item_clicked(self, index):
        x, y = self.model.data(index, role=256)  # Qt.UserRole = 256
        self.item_selected.emit(x, y, index.row())