from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

from app.views.panels.data_panel import DataPanelView
from app.views.panels.canvas_panel import CanvasPanelView
from app.views.panels.analysis_panel import AnalysisPanelView

from app.views.components.console_view import ConsoleView


class HomeView(QWidget):

    def __init__(self):
        super().__init__()

        # panels
        self.data_panel     = DataPanelView()
        self.canvas_panel   = CanvasPanelView()
        self.analysis_panel = AnalysisPanelView()
        self.console        = ConsoleView()

        # layout
        layout = QHBoxLayout()

        # right panel ------------------------
        right_panel = QWidget()
        _sub_layout = QVBoxLayout()

        _sub_layout.addWidget(self.analysis_panel,5)
        _sub_layout.addWidget(self.console,1)

        right_panel.setLayout(_sub_layout)
        #--------------------------------------

        layout.setContentsMargins(0, 0, 0, 0)
        
        layout.addWidget(self.data_panel,   1)
        layout.addWidget(self.canvas_panel, 2)
        layout.addWidget(right_panel,       1)

        self.setLayout(layout)

    def append_log(self, message: str):
        self.console.append_text(message)

