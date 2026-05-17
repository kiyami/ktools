
from app.views.panels.data_panel import DataPanelView
from app.viewmodels.data_panel_viewmodel import DataPanelViewModel


class DataPanelBinder:
    def __init__(self, view: DataPanelView, vm: DataPanelViewModel):

        # view -> vm
        view.file_path_sent.connect(
            vm.load_data
        )

        view.remove_btn_clicked.connect(
            vm.remove_data
        )

        view.reset_btn_clicked.connect(
            vm.reset_data
        )

        view.selected_row_changed.connect(
            vm.update_row_and_table
        )

        # vm -> view
        vm.model_sent.connect(
            view.set_model
        )

        vm.data_length_sent.connect(
            view.set_visibility
        )

        vm.selected_row_updated.connect(
            view.set_row
        )

        vm.keys_sent.connect(
            view.update_list
        )

        vm.data_resetted.connect(
            view.reset_all
        )
