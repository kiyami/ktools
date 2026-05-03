from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QFileDialog
from PySide6.QtCore import Signal

from app.views.components.table_view import TableView
from app.views.components.canvas_view import CanvasView


class HomeView(QWidget):

    theme_clicked = Signal()
    load_clicked = Signal(str)

    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()

        # canvas layout
        layout_left = QVBoxLayout()
        
        self.canvas_view = CanvasView()

        layout_left.addWidget(self.canvas_view)

        # table layout
        layout_right = QVBoxLayout()

        self.theme_button = QPushButton("Toggle Theme")
        self.theme_button.setProperty

        self.load_button = QPushButton("Load Data")
        self.table_view = TableView()
        
        self.selected_value = QLineEdit()
        self.selected_value.setReadOnly(True)
        self.selected_value.setPlaceholderText("Selected cell value...")

        layout_right.addWidget(self.load_button)
        layout_right.addWidget(self.table_view)
        layout_right.addWidget(self.selected_value)
        layout_right.addWidget(self.theme_button)

        # merge layout
        layout.addLayout(layout_left,2)
        layout.addLayout(layout_right,1)

        self.setLayout(layout)

        self.theme_button.clicked.connect(self.theme_clicked.emit)
        self.load_button.clicked.connect(self.open_file_dialog)

    def update_selected_value(self, value: str):
        self.selected_value.setText(f"Selected: {value}")

    def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select File",
            "",
            "Data Files (*.txt *.csv *.tsv)"
        )

        if file_path:
            self.load_clicked.emit(file_path)