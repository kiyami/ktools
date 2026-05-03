from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QListWidget, QLineEdit, QSizePolicy
)

from PySide6.QtCore import Signal

from app.views.components.table_view import TableView

from enum import Enum


class TableState(Enum):
    EMPTY = 0
    READY = 1


class TablePanel(QWidget):

    load_clicked = Signal()
    cell_selected = Signal(str)
    remove_clicked = Signal()
    file_dropped = Signal(str)

    def __init__(self):
        super().__init__()

        self.setObjectName("tableContainer")
        self.setAcceptDrops(True)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(8)

        # LOAD
        self.load_button = QPushButton("Load Data")
        self.load_button.setProperty("variant", "primary")

        self.load_button.setFixedHeight(25)

        # SELECTED
        self.selected_value = QLineEdit()
        self.selected_value.setReadOnly(True)
        self.selected_value.setPlaceholderText("Selected cell value...")

        # DATA CONTAINER
        self.data_container = QWidget()

        data_layout = QVBoxLayout()

        self.table_view = TableView()
        self.data_list = QListWidget()

        self.remove_button = QPushButton("Remove Data")
        self.remove_button.setProperty("variant", "danger")

        data_layout.addWidget(self.table_view, 10)
        data_layout.addWidget(self.selected_value, 1)
        data_layout.addWidget(self.data_list, 2)
        data_layout.addWidget(self.remove_button, 1)

        self.data_container.setLayout(data_layout)
        self.data_container.setVisible(False)

        # MAIN
        main_layout.addWidget(self.load_button, 0)
        main_layout.addWidget(self.data_container, 1)

        self.setLayout(main_layout)

        # SIGNALS
        self.load_button.clicked.connect(self.load_clicked.emit)
        self.table_view.cell_selected.connect(self.cell_selected.emit)
        self.remove_button.clicked.connect(self.remove_clicked.emit)

        self.set_state(TableState.EMPTY)

        self.load_button.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Fixed
        )

        self.data_container.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )

    def set_state(self, state: TableState):
        self._state = state

        if state == TableState.EMPTY:
            self.data_container.setVisible(False)

        elif state == TableState.READY:
            self.data_container.setVisible(True)

        elif state == TableState.LOADING:
            self.data_container.setVisible(False)

    # API
    def set_model(self, model):
        self.table_view.set_model(model)
        self.set_state(TableState.READY)

    def clear(self):
        self.table_view.set_model(None)
        self.data_list.clear()
        self.set_state(TableState.EMPTY)

    def update_selected_value(self, value: str):
        self.selected_value.setText(f"Selected: {value}")

    # drag & drop
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        file_path = event.mimeData().urls()[0].toLocalFile()
        self.file_dropped.emit(file_path)