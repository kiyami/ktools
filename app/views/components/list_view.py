from PySide6.QtWidgets import QListWidget


class ListView(QListWidget):

    def __init__(self):
        super().__init__()

    def get_row(self) -> int:
        return self.currentRow()

    def set_row(self, row_idx):
        self.setCurrentRow(row_idx)
