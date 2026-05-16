
from app.views.panels.canvas_panel import CanvasPanelView
from app.viewmodels.canvas_panel_viewmodel import CanvasPanelViewModel


class CanvasPanelBinder:
    def __init__(self, view: CanvasPanelView, vm: CanvasPanelViewModel):
        self.view = view
        self.vm = vm
