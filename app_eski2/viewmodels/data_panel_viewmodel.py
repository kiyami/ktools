from PySide6.QtCore import QObject

from app.models.data_table_model import DataTableModel
from app.views.data_panel_view import DataPanelView


class DataPanelViewModel(QObject):

    def __init__(self, data_vm):
        super().__init__()
        self.data_vm = data_vm
        self.view = None

    def bind(self, view):
        self.view = view

        # View → VM
        view.add_clicked.connect(self.add_data)

        # Data VM → Panel VM
        self.data_vm.data_loaded.connect(self.on_data_loaded)

    def add_data(self):
        # 🔥 burada dosya seçtirebilirsin
        path = "data.txt"
        self.data_vm.load_file(path)

    def on_data_loaded(self, cols, names):
        self.view.data_table.set_data(cols, names)