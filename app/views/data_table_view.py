# app/views/data_table_view.py

from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableView
from app.models.data_table_model import DataTableModel


class DataTableView(QWidget):

    def __init__(self):
        super().__init__()

        self.table = QTableView()
        self.model = DataTableModel()

        self.table.setModel(self.model)

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)

    def set_data(self, cols, names):
        self.model.set_data(cols, names)