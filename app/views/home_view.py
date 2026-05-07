from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QFileDialog, QSizePolicy
)

from PySide6.QtCore import Signal

from app.views.components.console_view import ConsoleView

from app.views.panels.table_panel import TablePanel
from app.views.panels.canvas_panel import CanvasPanel
from app.views.panels.analysis_panel import AnalysisPanel


class HomeView(QWidget):

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
        self.console = ConsoleView()
        layout_middle.addWidget(self.canvas_view,10)
        layout_middle.addWidget(self.console,1)

        # RIGHT
        layout_right = QVBoxLayout()
        self.analysis_view = AnalysisPanel()
        layout_right.addWidget(self.analysis_view)

        layout.addLayout(layout_left,1)
        layout.addLayout(layout_middle,3)
        layout.addLayout(layout_right,1)

        self.setLayout(layout)

        self._setup_console_ui()

    # ---------------- UI ----------------
    def _setup_console_ui(self):
        self.console.setObjectName("consoleView")

        # size policy
        self.console.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Fixed
        )

        # yükseklik
        self.console.setMinimumHeight(40)
        self.console.setMaximumHeight(100)


    def append_text(self, text: str):
        self.console.append_text(text)

    def get_table_view(self):
        return self.table_view
    
    def get_canvas_view(self):
        return self.canvas_view
    
    def get_analysis_view(self):
        return self.analysis_view
