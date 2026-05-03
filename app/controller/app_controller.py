from app.views.home_view import HomeView
from app.viewmodels.home_viewmodel import HomeViewModel
from app.viewmodels.table_viewmodel import TableViewModel
from app.viewmodels.canvas_viewmodel import CanvasViewModel


class AppController:

    def __init__(self):
        self.theme = None

        self.view = None
        self.home_vm = None
        self.table_vm = None
        self.canvas_vm = None

    def set_theme_manager(self, theme_manager):
        self.theme = theme_manager
        self.view.theme_clicked.connect(self._toggle_theme)

    def _toggle_theme(self):
        self.theme.toggle()

    def start(self):
        self.view = HomeView()

        self.home_vm = HomeViewModel()
        self.canvas_vm = CanvasViewModel()
        self.table_vm = TableViewModel()

        # =========================
        # LOAD FLOW (single source)
        # =========================
        self.view.load_clicked.connect(self.home_vm.load_file)

        self.home_vm.data_loaded.connect(self.table_vm.set_data)
        self.home_vm.data_loaded.connect(self.canvas_vm.set_data)

        # headers → UI (ONLY ONCE)
        self.home_vm.data_loaded.connect(
            lambda r: self.view.canvas_view.set_columns(r.headers)
        )

        # =========================
        # TABLE BIND
        # =========================
        self.table_vm.model_ready.connect(self.view.table_view.set_model)
        self.view.table_view.set_model(self.table_vm.get_model())

        self.view.table_view.cell_selected.connect(
            self.home_vm.on_cell_selected
        )

        self.home_vm.selected_changed.connect(
            self.view.update_selected_value
        )

        # =========================
        # PLOT FLOW
        # =========================
        self.view.canvas_view.add_plot_clicked.connect(
            self.canvas_vm.add_plot
        )

        self.view.canvas_view.remove_plot_clicked.connect(
            self.canvas_vm.remove_plot
        )

        self.canvas_vm.plots_changed.connect(
            self.view.canvas_view.update_plot_list
        )

        self.canvas_vm.redraw.connect(
            self.view.canvas_view.draw
        )

        return self.view