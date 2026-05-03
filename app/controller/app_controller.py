from app.views.home_view import HomeView
from app.viewmodels.home_viewmodel import HomeViewModel
from app.viewmodels.table_viewmodel import TableViewModel
from app.viewmodels.canvas_viewmodel import CanvasViewModel
from app.viewmodels.analysis_viewmodel import AnalysisViewModel


class AppController:

    def __init__(self):
        self.theme = None

        self.view = None

        self.home_vm = None
        self.table_vm = None
        self.canvas_vm = None
        self.analysis_vm = None

    def start(self):
        self.view = HomeView()

        self.home_vm = HomeViewModel()
        self.table_vm = TableViewModel()
        self.canvas_vm = CanvasViewModel()
        self.analysis_vm = AnalysisViewModel()

        self.view.toggle_button_clicked.connect(
            self.home_vm.make_toggle
        )

        self.home_vm.toggle.connect(
            self.view.toggle_table
        )

        return self.view