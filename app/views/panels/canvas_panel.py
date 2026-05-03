from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QListWidget, QLineEdit, QSizePolicy
)

from PySide6.QtCore import Signal

from app.views.components.canvas_view import CanvasView


class CanvasPanel(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        
        self.canvas_view = CanvasView()
        self.plot_button = QPushButton("Plot Data")

        layout.addWidget(self.canvas_view, 1)
        layout.addWidget(self.plot_button, 0)

        layout.setContentsMargins(0,0,0,0)

        self.setLayout(layout)

