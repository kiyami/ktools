from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QFileDialog

from app.models.dataset import Dataset
from app.models.table_model import TableModel

from app.services.data_service import DataService

import numpy as np
import os


class TableViewModel(QObject):
    
    data_loaded = Signal(object)
    data_removed = Signal(object)

    selected_row_updated = Signal(object)
    update_selected_row = Signal(int)
    
    update_visibility = Signal(int)
    table_resetted = Signal()

    model_sended = Signal(object)

    def __init__(self, data_service: DataService):
        super().__init__()
        self.model = TableModel()
        self.data_service = data_service
        self.selected_row = None

    def get_model(self):
        return self.model     

    def send_model(self):
        self.model_sended.emit(self.model)

    def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(
            None,
            "Select File",
            "",
            "Data Files (*.txt *.csv *.tsv)"
        )

        if file_path:
            self.load_data(file_path)

    def _set_data(self, dataset):
        if dataset.error:
            print("Error:", dataset.error)
            return

        self.model.set_data(dataset.raw_data, dataset.headers)

    def load_data(self, path):

        dataset = self.data_service.load(path)
            
        if not dataset.error:
            self._set_data(dataset)

            self.data_loaded.emit(self.data_service.get_all())

            length = self.data_service.get_length()
            self.update_visibility.emit(length)

            self.selected_row = length-1
            self.update_selected_row.emit(length-1)

    def remove_data(self, index):

        self.data_service.remove(index)
        length = self.data_service.get_length()

        if length > 0:

            dataset = self.data_service.get(length-1)
            self._set_data(dataset)
            self.data_removed.emit(self.data_service.get_all())
            self.update_visibility.emit(length)

            self.selected_row = length-1
            self.update_selected_row.emit(length-1)

        else:
            self.reset_table()

    def reset_table(self):
        self.data_service.clear()
        self.table_resetted.emit()
        self.update_visibility.emit(0)

    def update_row_and_table(self, row):

        length = self.data_service.get_length()

        if length == 0:
            self.reset_table()
            return

        if row == -1:
            row = length - 1

        self.selected_row = row

        dataset = self.data_service.get(row)
        self._set_data(dataset)
        self.selected_row_updated.emit(dataset)
