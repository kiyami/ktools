from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QTextEdit,
    QPushButton, QComboBox, QListWidget, QListWidgetItem, QLabel
)


class TableView(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.table = QTextEdit()
        self.table.setReadOnly(True)
        
        layout.addWidget(self.table,1)
        layout.setContentsMargins(0,0,0,0)
        
        self.setLayout(layout)

    def clear(self):
        self.table.clear()
