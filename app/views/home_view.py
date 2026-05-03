from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QFileDialog
)
from PySide6.QtCore import Signal

from app.views.panels.table_panel import TablePanel
from app.views.panels.canvas_panel import CanvasPanel
from app.views.panels.analysis_panel import AnalysisPanel


class HomeView(QWidget):

    toggle_button_clicked = Signal()

    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()

        # LEFT
        layout_left = QVBoxLayout()
        self.table_view = TablePanel()
        layout_left.addWidget(self.table_view)

        # MIDDLE
        layout_middle = QVBoxLayout()
        self.canvas_view = CanvasPanel()
        layout_middle.addWidget(self.canvas_view)

        # RIGHT
        layout_right = QVBoxLayout()
        self.analysis_view = AnalysisPanel()
        layout_right.addWidget(self.analysis_view)

        layout.addLayout(layout_left,1)
        layout.addLayout(layout_middle,3)
        layout.addLayout(layout_right,1)

        self.setLayout(layout)

        self.table_view.toggle_button_clicked.connect(self.toggle_button_clicked.emit)

    def toggle_table(self):
        self.table_view.toggle_table()