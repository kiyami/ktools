# app/viewmodels/data_viewmodel.py

from PySide6.QtCore import QObject, Signal
from app.services.file_service import read_data_txt


class DataViewModel(QObject):

    data_loaded = Signal(list, list)

    def __init__(self):
        super().__init__()
        self.columns = []
        self.colnames = []

    def load_file(self, path):
        cols, names = read_data_txt(path)

        self.columns = cols
        self.colnames = names

        self.data_loaded.emit(self.columns, self.colnames)