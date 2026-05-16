
from app.views.panels.analysis_panel import AnalysisPanelView
from app.viewmodels.analysis_panel_viewmodel import AnalysisPanelViewModel


class AnalysisPanelBinder:
    def __init__(self, view: AnalysisPanelView, vm: AnalysisPanelViewModel):
        self.view = view
        self.vm = vm
