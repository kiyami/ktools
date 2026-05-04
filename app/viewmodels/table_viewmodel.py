from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QFileDialog

from app.models.load_result import LoadResult
from app.models.table_model import TableModel

from app.services.data_loader import DataLoader

import numpy as np
import os


class TableViewModel(QObject):
    
    data_loaded = Signal(object)
    data_removed = Signal(object)

    selected_row_updated = Signal(LoadResult)
    
    update_visibility = Signal(int)
    table_resetted = Signal()

    model_ready = Signal(object)

    def __init__(self):
        super().__init__()
        self.model = TableModel()
        self.data_loader = DataLoader()
        self.data_list = []
        self.selected_row = None

    def get_model(self):
        return self.model

    def _set_data(self, result):
        if result.error:
            print("Error:", result.error)
            return

        self.model.set_data(result.raw_data, result.headers)
        self.model_ready.emit(self.model)

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

        try:
            result = self.data_loader.load(path)

        except Exception as e:
            result = LoadResult(
                label=None,
                raw_data=None,
                numeric_data=None,
                headers=None,
                error=str(e)
            )

            print(e)
            
        if not result.error:
            self._set_data(result)

            self.data_list.append(result)
            self.data_loaded.emit(self.data_list)

            self.update_visibility.emit(len(self.data_list))

    def remove_data(self, index):
        try:
            del self.data_list[index]

            if len(self.data_list) > 0:

                # set the last data into view
                self._set_data(self.data_list[-1])

                self.data_removed.emit(self.data_list)
            else:
                self.reset_table()

        except Exception as e:
            print("can't remove data")
            print(f"current data length is {len(self.data_list)}")

    def reset_table(self):
        self.data_list = []
        self.table_resetted.emit()
        self.update_visibility.emit(0)

    def update_row_and_table(self, row):

        if len(self.data_list) == 0:
            self.reset_table()
            return

        if row == -1:
            row = len(self.data_list) - 1

        self.selected_row = row

        self._set_data(self.data_list[row])
        self.selected_row_updated.emit(self.data_list[row])
