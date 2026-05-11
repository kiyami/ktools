from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QFileDialog, QSizePolicy, QSplitter
)

from PySide6.QtCore import Signal, Qt

from app.views.components.console_view import ConsoleView

from app.views.panels.table_panel import TablePanel
from app.views.panels.canvas_panel import CanvasPanel
from app.views.panels.analysis_panel import AnalysisPanel



class HomeView(QWidget):

    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()

        splitter = QSplitter(Qt.Horizontal)

        # LEFT
        left_widget = QWidget()
        layout_left = QVBoxLayout()
        self.table_view = TablePanel()
        layout_left.addWidget(self.table_view)
        left_widget.setLayout(layout_left)

        # MIDDLE
        middle_widget = QWidget()
        layout_middle = QVBoxLayout()
        self.canvas_view = CanvasPanel()
        self.console = ConsoleView()
        layout_middle.addWidget(self.canvas_view,10)
        layout_middle.addWidget(self.console,1)
        middle_widget.setLayout(layout_middle)

        # RIGHT
        right_widget = QWidget()
        layout_right = QVBoxLayout()
        self.analysis_view = AnalysisPanel()
        layout_right.addWidget(self.analysis_view)
        right_widget.setLayout(layout_right)

        splitter.addWidget(left_widget)
        splitter.addWidget(middle_widget)
        splitter.addWidget(right_widget)

        splitter.setSizes([400, 900, 400])

        splitter.setStretchFactor(0, 4)  # right
        splitter.setStretchFactor(1, 9)  # middle
        splitter.setStretchFactor(2, 4)  # left

        layout.addWidget(splitter)

        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(5)

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
        self.console.setMinimumHeight(50)
        self.console.setMaximumHeight(100)

    def append_text(self, text: str):
        self.console.append_text(text)

    def get_table_view(self):
        return self.table_view
    
    def get_canvas_view(self):
        return self.canvas_view
    
    def get_analysis_view(self):
        return self.analysis_view
    