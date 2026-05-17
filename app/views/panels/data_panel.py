from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QSizePolicy, QFileDialog

from PySide6.QtCore import Signal, Qt

from app.views.components.data_table_view import DataTableView
from app.views.components.list_view import ListView
from app.views.components.drag_and_drop_view import DropLabel

from app.utils.helpers import hbox, vbox


class DataPanelView(QWidget):

    load_btn_clicked     = Signal()
    remove_btn_clicked   = Signal(int)
    reset_btn_clicked    = Signal()

    file_path_sent       = Signal(object)
    selected_row_changed = Signal(int)

    message_sended       = Signal(str)

    def __init__(self):
        super().__init__()

        # ---------------------------------------
        # items
        # ---------------------------------------
        self.load_btn   = QPushButton("Load Data")
        self.remove_btn = QPushButton("Remove")
        self.reset_btn  = QPushButton("Reset")

        self.data_table     = DataTableView()
        self.data_list      = ListView()
        self.drag_drop_area = DropLabel("Drag & Drop\nData File")

        # ---------------------------------------
        # layout
        # ---------------------------------------

        # header layout -------------------------
        header = QWidget()
        header_layout = QHBoxLayout()

        header_layout.addWidget(self.load_btn, 0)
        header_layout.setContentsMargins(4,4,4,4)

        header.setLayout(header_layout)

        header.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Fixed
        )
        header.setMinimumHeight(30)
        header.setMaximumHeight(30)

        # content layout -------------------------
        self.content = QWidget()
        content_layout = QVBoxLayout()

        content_layout.addWidget(self.data_table, 5)
        content_layout.addWidget(self.data_list, 1)

        bottom_btns = hbox(
            self.remove_btn, 
            self.reset_btn, 
            spacing=5, 
            margins=(0,0,0,0),
            ratios=(1,1)
        )
        content_layout.addWidget(bottom_btns, 0)

        content_layout.setContentsMargins(4,4,4,4)

        self.content.setLayout(content_layout)

        self.content.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )

        # main layout ---------------------------
        main_layout = QVBoxLayout()

        main_layout.addWidget(header, 0)   # sabit alan
        main_layout.addWidget(self.content, 15)  # büyüyen alan
        main_layout.addWidget(self.drag_drop_area, 1)
        
        main_layout.setAlignment(Qt.AlignTop)
        main_layout.setContentsMargins(4,4,4,4)

        self.setLayout(main_layout)

        # binding -------------------------------
        self._bind()

    def _bind(self):
        self.load_btn.clicked.connect(self.open_file_dialog)
        self.remove_btn.clicked.connect(self.remove_data_by_index)
        self.reset_btn.clicked.connect(self.reset_btn_clicked.emit)

        self.drag_drop_area.file_dropped.connect(self.file_path_sent.emit)

        self.data_list.currentRowChanged.connect(self.on_row_changed)

    def send_message(self, message: str):
        self.message_sended.emit(message)
        
    def set_model(self, model):
        self.data_table.set_model(model)

    def get_row(self):
        return self.data_list.get_row()
    
    def set_row(self, row_idx):
        self.data_list.set_row(row_idx)

    def on_row_changed(self):
        self.selected_row_changed.emit(self.get_row())

    def remove_data_by_index(self):
        row_idx = self.get_row()
        self.remove_btn_clicked.emit(row_idx)

    def update_list(self, keys: list):
        self.data_list.clear()
        self.data_list.addItems(keys)

    def reset_all(self):
        self.data_table.clear()
        self.data_list.clear()

    def set_visibility(self, n_data: int):
        if n_data == 0:
            self.content.setVisible(False)
        else:
            self.content.setVisible(True)

    def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(
            None,
            "Select File",
            "",
            "Data Files (*.txt *.csv *.tsv)"
        )

        if file_path:
            self.file_path_sent.emit(file_path)
