from app.views.home_view import HomeView
from app.viewmodels.home_viewmodel import HomeViewModel
from app.viewmodels.table_viewmodel import TableViewModel
from app.viewmodels.canvas_viewmodel import CanvasViewModel
from app.viewmodels.analysis_viewmodel import AnalysisViewModel

from app.models.load_result import LoadResult


class AppController:

    def __init__(self):
        self.theme = None

    def _init_views(self):
        self.home_view = HomeView()
        self.table_view = self.home_view.get_table_view()
        self.canvas_view = self.home_view.get_canvas_view()
        self.analysis_view = self.home_view.get_analysis_view()

    def _init_viewmodels(self):
        self.home_vm = HomeViewModel()
        self.table_vm = TableViewModel()
        self.canvas_vm = CanvasViewModel()
        self.analysis_vm = AnalysisViewModel()

    def _handle_load_result(self, result: LoadResult):
        if result.error:
            self.table_view.show_error(result.error)
        else:
            self.table_view.update_table(result)

    def _bind(self):

        # load data v->vm
        self.table_view.load_data_clicked.connect(
            self.table_vm.load_data
        )
        # load data vm->v
        self.table_vm.data_loaded.connect(
            self.table_view.update_table
        )
        self.table_vm.update_visibility.connect(
            self.table_view.set_visibility
        )

        # remove data v->vm
        self.table_view.remove_data_clicked.connect(
            self.table_vm.remove_data
        )
        # remove data vm->v
        self.table_vm.data_removed.connect(
            self.table_view.update_table
        )
        self.table_vm.data_removed.connect(
            self.table_view.set_visibility
        )

        # reset data v->vm
        self.table_view.reset_clicked.connect(
            self.table_vm.reset_table
        )
        # reset data vm->v
        self.table_vm.table_resetted.connect(
            self.table_view.reset_table
        )

    def start(self):
        self._init_views()
        self._init_viewmodels()
        self._bind()

        self.table_view.set_visibility(len(self.table_vm.data_list))

        return self.home_view