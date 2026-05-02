from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QFileDialog
from PySide6.QtCore import Signal

from app.views.components.table_view import TableView
from app.views.components.canvas_view import CanvasView


class HomeView(QWidget):

    load_clicked = Signal(str)
    plot_clicked = Signal()

    def __init__(self):
        super().__init__()


        layout = QHBoxLayout()

        # canvas layout
        layout_right = QVBoxLayout()
        
        self.canvas_view = CanvasView()
        self.plot_button = QPushButton("Plot Data")

        layout_right.addWidget(self.canvas_view)
        layout_right.addWidget(self.plot_button)

        # table layout
        layout_left = QVBoxLayout()

        self.load_button = QPushButton("Load Data")
        self.table_view = TableView()
        
        self.selected_value = QLineEdit()
        self.selected_value.setReadOnly(True)
        self.selected_value.setPlaceholderText("Selected cell value...")

        layout_left.addWidget(self.load_button)
        layout_left.addWidget(self.table_view)
        layout_left.addWidget(self.selected_value)

        # merge layout
        layout.addLayout(layout_right,2)
        layout.addLayout(layout_left,1)

        self.setLayout(layout)

        self.load_button.clicked.connect(self.open_file_dialog)
        self.plot_button.clicked.connect(self.plot_clicked.emit)

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