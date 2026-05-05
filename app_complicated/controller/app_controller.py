from app.services.theme_manager import ThemeManager
from app.views.home_view import HomeView
from app.viewmodels.home_viewmodel import HomeViewModel
from app.viewmodels.table_viewmodel import TableViewModel
from app.viewmodels.canvas_viewmodel import CanvasViewModel
from app.viewmodels.analysis_viewmodel import AnalysisViewModel

from app.canvas_core.data_store import DataStore
from app.canvas_core.renderer import CanvasRenderer


class AppController:

    def __init__(self, app):
        self.app = app

        self._init_viewmodels()
        self._init_views()

        self.theme_manager = ThemeManager(app)
        self.theme_manager.apply("light")

        self._bind()

    # ---------------- INIT ----------------
    def _init_views(self):
        self.home_view = HomeView()

        self.table_view = self.home_view.get_table_view()
        self.table_view.set_visibility([])

        self.canvas_view = self.home_view.get_canvas_view()
        self.analysis_view = self.home_view.get_analysis_view()

        # renderer injection (clean)
        renderer = CanvasRenderer(
            self.canvas_view.get_axis(),
            self.store
        )
        self.canvas_view.set_renderer(renderer)

    def _init_viewmodels(self):
        self.home_vm = HomeViewModel()

        self.store = DataStore()

        self.table_vm = TableViewModel(self.store)
        self.canvas_vm = CanvasViewModel(self.store)

        self.analysis_vm = AnalysisViewModel()

    # ---------------- BINDINGS ----------------
    def _bind(self):

        # TABLE FLOW
        self.table_view.load_data_clicked.connect(self.table_vm.open_file_dialog)
        self.table_view.file_dropped.connect(self.table_vm.load_data)

        self.table_vm.data_loaded.connect(self.table_view.update_table)
        self.table_view.remove_data_clicked.connect(self.table_vm.remove_data)
        self.table_vm.data_removed.connect(self.table_view.update_table)

        self.table_view.reset_clicked.connect(self.table_vm.reset_table)
        self.table_vm.table_resetted.connect(self.table_view.reset_table)

        self.table_view.selected_row_changed.connect(self.table_vm.update_row_and_table)

        self.table_vm.model_ready.connect(self.table_view.set_model)

        # visibility sync
        self.table_vm.data_loaded.connect(self._sync_visibility)
        self.table_vm.data_removed.connect(self._sync_visibility)
        self.table_vm.table_resetted.connect(lambda: self._sync_visibility([]))
        self.table_vm.model_ready.connect(
            lambda _: self._sync_visibility(self.store.list())
        )

        # ---------------- PLOT FLOW ----------------

        # plot isteği → table
        self.canvas_view.plot_requested.connect(
            self.table_vm.data_requested_with_type
        )

        # table → controller
        self.table_vm.data_sended.connect(self._on_data_received)

        # canvas render
        self.canvas_vm.state_changed.connect(
            self.canvas_view.set_state
        )

        self.table_vm.selected_row_updated.connect(self._update_canvas_columns)

    def _update_canvas_columns(self, result):
        if result.headers:
            self.canvas_view.set_columns(result.headers)

    # ---------------- DATA → PLOT ----------------
    def _on_data_received(self, payload):
        result, payload = payload
        self.canvas_vm.create_plot(result, payload)

    # ---------------- WINDOW ----------------
    def bind_main_window(self, window):
        window.open_requested.connect(self.table_vm.open_file_dialog)
        window.exit_requested.connect(window.close)
        window.theme_toggled.connect(self.theme_manager.set_dark_mode)

    def start(self):
        return self.home_view

    def _sync_visibility(self, data_list):
        self.table_view.set_visibility(data_list)