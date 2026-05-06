from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QFileDialog

from app.models.dataset import LoadResult
from app.models.table_model import TableModel

from app.services.data_loader import DataLoader

import numpy as np
import os


class TableViewModel(QObject):
    
    data_loaded = Signal(object)
    data_removed = Signal(object)

    selected_row_updated = Signal(LoadResult)
    
    update_visibility = Signal(list)
    table_resetted = Signal()

    model_ready = Signal(object)

    data_sended = Signal(object)

    def __init__(self, store):
        super().__init__()
        self.model = TableModel()
        self.data_loader = DataLoader()
        self.store = store
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

            data_id = self.store.add(result)

            self.data_loaded.emit(self.store.list())

    def remove_data(self, index):
        try:
            self.store.remove(index)

            if self.store.count() > 0:
                last = self.store.list()[-1]
                self._set_data(last)
                self.data_removed.emit(self.store.list())
            else:
                self.reset_table()

        except Exception as e:
            print("can't remove data")

    def reset_table(self):
        self.store.clear()
        self.table_resetted.emit()

    def update_row_and_table(self, row):

        if self.store.count() == 0:
            self.reset_table()
            return

        if row == -1:
            row = self.store.count() - 1

        self.selected_row = row

        result = self.store.get(row)
        self._set_data(result)
        self.selected_row_updated.emit(result)

    def data_requested_with_type(self, payload: dict):

        if self.selected_row is None:
            return

        if self.selected_row >= self.store.count():
            return

        result = self.store.get(self.selected_row)

        self.data_sended.emit((result, payload))