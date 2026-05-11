from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QComboBox, QListWidget, QListWidgetItem, QLabel
)


class AnalysisView(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Analysis View"))
        layout.setContentsMargins(0,0,0,0)

        self.setLayout(layout)
