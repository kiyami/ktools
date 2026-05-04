from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, 
    QLineEdit, QSizePolicy, QTextEdit
)

from PySide6.QtCore import Signal, Qt

from app.views.components.table_view import TableView
from app.models.load_result import LoadResult


class TablePanel(QWidget):

    load_data_clicked = Signal(str)
    remove_data_clicked = Signal(int)
    reset_clicked = Signal()

    def __init__(self):
        super().__init__()

        self.load_button = QPushButton("Load Data")

        self.table_view = TableView()

        self.table_list = QListWidget()

        self.remove_button = QPushButton("Remove Data")

        self.reset_button = QPushButton("Reset")

        # HEADER LAYOUT
        header = QWidget()
        header_layout = QHBoxLayout()

        header_layout.addWidget(self.load_button, 0)

        header_layout.setContentsMargins(0,0,0,0)

        header.setLayout(header_layout)

        header.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Fixed
        )
        header.setMinimumHeight(30)
        header.setMaximumHeight(30)

        # CONTENT LAYOUT
        self.content = QWidget()
        content_layout = QVBoxLayout()

        content_layout.addWidget(self.table_view, 5)
        content_layout.addWidget(self.table_list, 1)
        content_layout.addWidget(self.remove_button, 0)
        content_layout.addWidget(self.reset_button, 0)

        content_layout.setContentsMargins(0,0,0,0)

        self.content.setLayout(content_layout)

        self.content.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )

        # MAIN LAYOUT
        main_layout = QVBoxLayout()

        main_layout.addWidget(header, 0)   # sabit alan
        main_layout.addWidget(self.content, 1)  # büyüyen alan
        #main_layout.addStretch(1)
        
        main_layout.setAlignment(Qt.AlignTop)
        main_layout.setContentsMargins(0,0,0,0)

        self.setLayout(main_layout)

        # signals
        self.load_button.clicked.connect(self._send_load_path)
        self.remove_button.clicked.connect(self._remove_data_by_index)
        self.reset_button.clicked.connect(self.reset_clicked)

    def update_table(self, data_list: list):
        print("raw data")
        print(data_list[0].raw_data)

        self.table_list.clear()
        self.table_list.addItems(
            item.label for item in data_list
        )

    def reset_table(self):
        self.table_view.clear()
        self.table_list.clear()

    def show_error(self, message):
        print("ERROR")
        print(message)

    def _send_load_path(self):
        path = "data path"
        self.load_data_clicked.emit(path)

    def _remove_data_by_index(self):
        index = self.table_list.currentRow()
        self.remove_data_clicked.emit(index)

    def set_visibility(self, length: int):
        if length == 0:
            self.content.setVisible(False)
        else:
            self.content.setVisible(True)
