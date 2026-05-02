from PySide6.QtCore import QObject, Signal
from app.models.table_model import TableModel


class TableViewModel(QObject):

    model_ready = Signal(object)

    def __init__(self):
        super().__init__()
        self.model = TableModel()

    def get_model(self):
        return self.model

    def set_data(self, result):
        if result.error:
            print("Error:", result.error)
            return

        self.model.set_data(result.data, result.headers)
        self.model_ready.emit(self.model)