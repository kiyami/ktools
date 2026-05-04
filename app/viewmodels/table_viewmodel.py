from PySide6.QtCore import QObject, Signal
from app.models.load_result import LoadResult
import numpy as np
import os


class TableViewModel(QObject):
    
    data_loaded = Signal(object)
    data_removed = Signal(object)
    
    update_visibility = Signal(int)
    table_resetted = Signal()

    def __init__(self):
        super().__init__()
        self.data_list = []

    def load_data(self, path):
        print(f"data loaded from {path}")

        try:
            # örnek veri
            label = os.path.split(path)[-1]
            raw_data = [["1", "2"], ["3", "4"]]
            numeric_data = np.array([[1, 2], [3, 4]])
            headers = ["A", "B"]

            result = LoadResult(
                label=label,
                raw_data=raw_data,
                numeric_data=numeric_data,
                headers=headers,
                error=None
            )

            self.data_list.append(result)
            self.data_loaded.emit(self.data_list)
            self.update_visibility.emit(len(self.data_list))

        except Exception as e:
            result = LoadResult(
                label=None,
                raw_data=None,
                numeric_data=None,
                headers=None,
                error=str(e)
            )

        print(self.data_list)

    def remove_data(self, index):
        try:
            del self.data_list[index]
            print("data removed")
            print(f"current data length is {len(self.data_list)}")

            if len(self.data_list) > 0:
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