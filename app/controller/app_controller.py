from app.views.home_view import HomeView
from app.viewmodels.home_viewmodel import HomeViewModel
from app.viewmodels.table_viewmodel import TableViewModel
from app.viewmodels.canvas_viewmodel import CanvasViewModel


class AppController:

    def __init__(self):
        self.view = None
        
        self.home_vm = None
        self.table_vm = None

    def start(self):
        self.view = HomeView()

        self.home_vm = HomeViewModel()
        self.canvas_vm = CanvasViewModel()
        self.table_vm = TableViewModel()

        # LOAD FLOW
        self.view.load_clicked.connect(self.home_vm.load_file)

        self.home_vm.data_loaded.connect(self.table_vm.set_data)
        self.home_vm.data_loaded.connect(self.canvas_vm.set_data)  # 🔥 FIX

        # TABLE BIND
        self.table_vm.model_ready.connect(self.view.table_view.set_model)
        self.view.table_view.set_model(self.table_vm.get_model())

        # CELL SELECT
        self.view.table_view.cell_selected.connect(
            self.home_vm.on_cell_selected
        )

        self.home_vm.selected_changed.connect(
            self.view.update_selected_value
        )

        # PLOT FLOW
        self.view.plot_clicked.connect(self.canvas_vm.generate_plot)
        self.canvas_vm.plot_ready.connect(self.view.canvas_view.plot)

        return self.view
