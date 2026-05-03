from PySide6.QtCore import QObject, Signal
from app.services.data_loader import DataLoader


class HomeViewModel(QObject):

    data_loaded = Signal(object)          # LoadResult
    selected_changed = Signal(str)
    error_occurred = Signal(str)          # 🔥 ekledik
    cleared = Signal()                    # 🔥 ekledik

    def __init__(self):
        super().__init__()
        self.loader = DataLoader()
        self.current_result = None

    # =========================
    # 🔹 LOAD FILE
    # =========================
    def load_file(self, path: str):
        result = self.loader.load(path)

        # 🔥 hata kontrolü
        if result is None or getattr(result, "error", None):
            self.error_occurred.emit(getattr(result, "error", "Unknown error"))
            return

        self.current_result = result
        self.data_loaded.emit(result)

    # =========================
    # 🔹 CELL SELECTION
    # =========================
    def on_cell_selected(self, value):
        # burada business logic genişletilebilir
        self.selected_changed.emit(str(value))

    # =========================
    # 🔹 CLEAR STATE
    # =========================
    def clear_data(self):
        self.current_result = None
        self.cleared.emit()

    # =========================
    # 🔹 GET DATA
    # =========================
    def get_data(self):
        return self.current_result