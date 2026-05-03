from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QComboBox, QListWidget, QListWidgetItem,
)

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class CanvasView(QWidget):

    def __init__(self):
        super().__init__()

        # ---------------- MATPLOTLIB ----------------
        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.ax = self.figure.add_subplot(111)

        # ---------------- UI ----------------
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.setContentsMargins(0,0,0,0)

        self.setLayout(layout)
