
from app.views.panels.data_panel import DataPanelView
from app.viewmodels.data_panel_viewmodel import DataPanelViewModel


class DataPanelBinder:
    def __init__(self, view: DataPanelView, vm: DataPanelViewModel):
        self.view = view
        self.vm = vm

        self._bind()

    def _bind(self):
        self.view.load_btn_clicked.connect(
            self.vm.open_file_dialog
        )

        self.view.remove_btn_clicked.connect(
            self.vm.remove_data
        )

        self.view.reset_btn_clicked.connect(
            self.vm.reset_data
        )

        self.view.file_dropped.connect(
            self.vm.load_data
        )

        self.view.selected_row_changed.connect(
            self.vm.update_row_and_table
        )

        self.vm.data_length_sent.connect(
            self.view.set_visibility
        )