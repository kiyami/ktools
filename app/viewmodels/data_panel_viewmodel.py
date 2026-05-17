from PySide6.QtCore import QObject, Signal

from app.models.data_table_model import DatasetTableModel

from app.services.data_service import DataService


class DataPanelViewModel(QObject):

    message_sent         = Signal(str)
    data_length_sent     = Signal(int)
    model_sent           = Signal(object)

    # data_loaded          = Signal(object)
    # data_removed         = Signal(object)
    data_resetted        = Signal()

    keys_sent            = Signal(list)

    selected_row_updated = Signal(int)

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
    
    def set_dataset(self, dataset):
        if dataset.error:
            self.send_message(f"ERROR: set_dataset\n{dataset.error}")
            print("Error:", dataset.error)
            return

        self.model.set_dataset(dataset)

    def load_data(self, path):

        dataset = self.data_service.load(path)
            
        if not dataset.error:
            self.set_dataset(dataset)
            self.model_sent.emit(self.model)

            length = self.data_service.count()
            self.update_visibility()

            self.selected_row = length-1
            self.selected_row_updated.emit(length-1)

            new_keys = self.data_service.keys()
            self.keys_sent.emit(new_keys)

            message = "Data loaded.."
        else:
            message = f"ERROR: Couldn't load data!\n{dataset.error}"

        self.send_message(message)

    def remove_data(self, index):

        self.data_service.remove(index)

        length = self.data_service.count()
        new_index = min(index, length-1)

        if length > 0:

            dataset = self.data_service.get_by_index(new_index)
            self.set_dataset(dataset)
            self.model_sent.emit(self.model)

            self.update_visibility()

            self.selected_row = new_index
            self.selected_row_updated.emit(new_index)

            new_keys = self.data_service.keys()
            self.keys_sent.emit(new_keys)

        else:
            self.reset_data()

        self.send_message("Data removed..")

    def reset_data(self):
        self.data_service.clear()

        self.data_resetted.emit()
        self.update_visibility()

        self.model = DatasetTableModel()
        self.model_sent.emit(self.model)

        self.send_message("Reset..")

    def update_row_and_table(self, row):

        length = self.data_service.count()

        if length == 0:
            self.reset_data()
            return

        if row == -1:
            row = length - 1

        self.selected_row = row

        dataset = self.data_service.get_by_index(row)
        self.set_dataset(dataset)
        
        self.selected_row_updated.emit(self.selected_row)
