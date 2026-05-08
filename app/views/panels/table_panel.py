from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, 
    QLineEdit, QSizePolicy, QTextEdit, QLabel
)

from PySide6.QtCore import Signal, Qt

from app.views.components.table_view import TableView
from app.views.components.drag_drop_view import DropLabel



class TablePanel(QWidget):

    load_data_clicked = Signal()

    file_dropped = Signal(str)

    remove_data_clicked = Signal(int)

    reset_clicked = Signal()

    selected_row_changed = Signal(int)

    def __init__(self):
        super().__init__()

        self.load_button = QPushButton("Load Data")

        self.table_view = TableView()

        self.table_list = QListWidget()
        self.table_list.setMinimumHeight(60)
        self.table_list.setMinimumHeight(40)

        self.remove_button = QPushButton("Remove Data")

        self.reset_button = QPushButton("Reset")

        self.drag_drop_area = DropLabel("Drag & Drop\nData File")
        self.drag_drop_area.setObjectName("dropArea")
        self.drag_drop_area.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.drag_drop_area.setMinimumHeight(30)

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
        main_layout.addWidget(self.content, 15)  # büyüyen alan
        main_layout.addWidget(self.drag_drop_area, 1)
        
        main_layout.setAlignment(Qt.AlignTop)
        main_layout.setContentsMargins(0,0,0,0)

        self.setLayout(main_layout)

        # signals
        self.load_button.clicked.connect(self.load_data_clicked.emit)
        self.drag_drop_area.file_dropped.connect(self.file_dropped)
        self.remove_button.clicked.connect(self._remove_data_by_index)
        self.reset_button.clicked.connect(self.reset_clicked)

        self.table_list.currentRowChanged.connect(self.on_row_changed)

    def _remove_data_by_index(self):
        index = self.table_list.currentRow()
        self.remove_data_clicked.emit(index)

    def on_row_changed(self):
        self.selected_row_changed.emit(self.get_row())

    def get_row(self):
        return self.table_list.currentRow()
    
    def set_row(self, row):
        self.table_list.setCurrentRow(row)

    def set_model(self, model):
        self.table_view.set_model(model)

    def update_table(self, data_list: list):
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

    def set_visibility(self, length: int):
        if length == 0:
            self.content.setVisible(False)
            self.drag_drop_area.setText("Drag & Drop\nData File")
        else:
            self.content.setVisible(True)
            self.drag_drop_area.setText("Drag & Drop")


