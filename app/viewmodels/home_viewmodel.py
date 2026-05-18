from PySide6.QtCore import QObject

from app.viewmodels.data_panel_viewmodel import DataPanelViewModel
from app.viewmodels.canvas_panel_viewmodel import CanvasPanelViewModel
from app.viewmodels.analysis_panel_viewmodel import AnalysisPanelViewModel

from app.binders.data_panel_binder import DataPanelBinder
from app.binders.canvas_panel_binder import CanvasPanelBinder
from app.binders.analysis_panel_binder import AnalysisPanelBinder

from app.views.home_view import HomeView

from app.services.data_service import DataService



class HomeViewModel(QObject):

    def __init__(self, home_view: HomeView):
        super().__init__()

        self.data_service = DataService()

        # ── Child ViewModels ──────────────────────────────

        self.data_panel_vm     = DataPanelViewModel(self.data_service)
        self.canvas_panel_vm   = CanvasPanelViewModel()
        self.analysis_panel_vm = AnalysisPanelViewModel()

        # ── Binders: each view ↔ its own VM ──────────────
        # Keep references — GC will break signals if dropped
        self._binders = [
            DataPanelBinder(
                home_view.data_panel, self.data_panel_vm
            ),
            CanvasPanelBinder(
                home_view.canvas_panel, self.canvas_panel_vm
            ),
            AnalysisPanelBinder(
                home_view.analysis_panel, self.analysis_panel_vm
            ),
        ]

        # ── Cross-panel + console wiring ──────────────────
        self._connect_vms(home_view)

        self._set_initial_states()
    
    def _connect_vms(self, home_view: HomeView):
        # # data → canvas
        # self.data_panel_vm.dataset_loaded.connect(
        #     self.canvas_panel_vm.on_dataset_loaded
        # )
        # self.data_panel_vm.headers_changed.connect(
        #     self.canvas_panel_vm.on_headers_changed
        # )

        # # data → analysis
        # self.data_panel_vm.dataset_loaded.connect(
        #     self.analysis_panel_vm.on_dataset_loaded
        # )

        # all panels → console
        self.data_panel_vm.message_sent.connect(home_view.append_log)
        self.canvas_panel_vm.message_sent.connect(home_view.append_log)
        self.analysis_panel_vm.message_sent.connect(home_view.append_log)
 
    def _set_initial_states(self):
        self.data_panel_vm.set_initial_state()
        # self.canvas_panel_vm.set_initial_state()
        # self.canvas_panel_vm.set_initial_state()