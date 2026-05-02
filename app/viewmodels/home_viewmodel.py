from PySide6.QtCore import QObject, Signal
from app.services.data_loader import DataLoader


class HomeViewModel(QObject):

    data_loaded = Signal(object)
    selected_changed = Signal(str)

    def __init__(self):
        super().__init__()
        self.loader = DataLoader()
        self.current_result = None

    def load_file(self, path):
        load_result = self.loader.load(path)
        self.current_result = load_result
        self.data_loaded.emit(load_result)

    def on_cell_selected(self, value):
        # business logic burada olur
        self.selected_changed.emit(value)

    def get_data(self):
        return self.current_result