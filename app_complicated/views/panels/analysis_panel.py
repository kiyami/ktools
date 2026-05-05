from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QListWidget, QLineEdit, QSizePolicy
)

from PySide6.QtCore import Signal

from app.views.components.analysis_view import AnalysisView


class AnalysisPanel(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        
        self.analyse_button = QPushButton("Analyse")
        self.analysis_view = AnalysisView()

        layout.addWidget(self.analyse_button, 0)
        layout.addWidget(self.analysis_view, 1)
        layout.setContentsMargins(0,0,0,0)

        self.setLayout(layout)

