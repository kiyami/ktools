from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QFileDialog

from app.models.data_table_model import DatasetTableModel

from app.services.data_service import DataService


class DataPanelViewModel(QObject):

    message_sent      = Signal(str)
    data_length_sent  = Signal(int)

    data_loaded       = Signal(object)
    data_removed      = Signal(object)

    def __init__(self, data_service: DataService):
        super().__init__()
        self.model = DatasetTableModel()
        self.data_service = data_service
        self.selected_row: None | int = None

    def send_message(self, message: str):
        self.message_sent.emit(message)

    def update_visibility(self):
        n_data = self.data_service.count()
        self.data_length_sent.emit(n_data)

    def get_model(self):
        return self.model
    
    def _set_data(self, dataset):
        if dataset.error:
            print("Error:", dataset.error)
            return

        self.model.set_dataset(dataset)
    
    def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(
            None,
            "Select File",
            "",
            "Data Files (*.txt *.csv *.tsv)"
        )

        if file_path:
            self.load_data(file_path)

    def load_data(self, path):

        dataset = self.data_service.load(path)
            
        if not dataset.error:
            self._set_data(dataset)

            self.data_loaded.emit(self.data_service.get_all())

            length = self.data_service.count()
            self.update_visibility()

            self.selected_row = length-1
            self.update_selected_row.emit(length-1)

            message = "File loaded.."
        else:
            message = "ERROR: Couldn't load file!"

        self.send_message(message)

    def remove_data(self, index):

        self.data_service.remove(index)
        length = self.data_service.count()

        if length > 0:

            dataset = self.data_service.get(length-1)
            self._set_data(dataset)
            self.data_removed.emit(self.data_service.get_all())
            self.update_visibility()

            self.selected_row = length-1
            self.update_selected_row.emit(length-1)

        else:
            self.reset_table()

    def reset_data(self):
        self.data_service.clear()

        self.table_resetted.emit()
        self.update_visibility()

        self.model = DatasetTableModel()
        self.model_sent.emit(self.model)

    def update_row_and_table(self, row):

        length = self.data_service.count()

        if length == 0:
            self.reset_data()
            return

        if row == -1:
            row = length - 1

        self.selected_row = row

        dataset = self.data_service.get(row)
        self._set_data(dataset)
        
        # self.selected_row_updated.emit(dataset)
        # self.headers_sent.emit(dataset.headers)