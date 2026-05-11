from PySide6.QtCore import QObject

from app.viewmodels.data_panel_viewmodel import DataPanelViewModel
from app.viewmodels.canvas_panel_viewmodel import CanvasPanelViewModel
from app.viewmodels.analysis_panel_viewmodel import AnalysisPanelViewModel



class HomeViewModel(QObject):

    def __init__(self):
        super().__init__()

        self.data_panel_vm = DataPanelViewModel()
        self.canvas_panel_vm = CanvasPanelViewModel()
        self.analysis_panel_vm = AnalysisPanelViewModel()

        