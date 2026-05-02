# app/views/data_table_view.py

from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableView
from app.models.data_table_model import DataTableModel


class DataTableView(QWidget):

    def __init__(self):
        super().__init__()

        self.table = QTableView()

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)

    def set_model(self, model):
        self.table.setModel(model)
