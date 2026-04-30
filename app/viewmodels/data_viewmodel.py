# app/viewmodels/data_viewmodel.py

from PySide6.QtCore import QObject, Signal
from app.services.file_service import read_data_txt


class DataViewModel(QObject):

    # 🔥 artık tuple emit ediyoruz
    data_loaded = Signal(object)

    def __init__(self):
        super().__init__()

        self.columns = []     # list[np.array]
        self.colnames = []    # list[str]

    def load_file(self, path, info=None):
        cols, names = read_data_txt(path)  # 🔥 doğru sıra

        print("SHAPES:", cols,names)

        self.columns = cols
        self.colnames = names

        # 🔥 payload: (columns, names)
        self.data_loaded.emit((self.columns, self.colnames))

    # 🎯 plot için
    def get_plot_data(self, x_col_idx=0, y_col_idx=1):
        if not self.columns or len(self.columns) < 2:
            return [], []

        return self.columns[x_col_idx], self.columns[y_col_idx]

    # 🎯 list/table için
    def get_all_data(self):
        return self.columns, self.colnames