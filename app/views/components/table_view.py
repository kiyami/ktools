from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QTextEdit, QTableView,
    QPushButton, QComboBox, QListWidget, QListWidgetItem, QLabel, QHeaderView
)


class TableView(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.table = QTableView()
        
        layout.addWidget(self.table,1)
        layout.setContentsMargins(0,0,0,0)
        
        self.setLayout(layout)

    def set_model(self, model):
        self.table.setModel(model)
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

    def clear(self):
        self.table.setModel(None)
