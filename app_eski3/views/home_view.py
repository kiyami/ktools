from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QFileDialog
)
from PySide6.QtCore import Signal

from app.views.panels.table_panel import TablePanel
from app.views.components.canvas_view import CanvasView


class HomeView(QWidget):

    theme_clicked = Signal()
    load_clicked = Signal(str)

    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()

        # LEFT
        layout_left = QVBoxLayout()
        self.canvas_view = CanvasView()
        layout_left.addWidget(self.canvas_view)

        # RIGHT
        layout_right = QVBoxLayout()

        self.table_panel = TablePanel()

        # 🔥 IMPORTANT FIX: sadece file dialog burada
        self.table_panel.load_clicked.connect(self.open_file_dialog)

        self.theme_button = QPushButton("Toggle Theme")
        self.theme_button.setProperty("variant", "secondary")

        layout_right.addWidget(self.table_panel)
        layout_right.addWidget(self.theme_button)

        layout.addLayout(layout_left, 2)
        layout.addLayout(layout_right, 1)

        self.setLayout(layout)

        self.theme_button.clicked.connect(self.theme_clicked.emit)

    def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select File",
            "",
            "Data Files (*.txt *.csv *.tsv)"
        )

        if file_path:
            self.load_clicked.emit(file_path)

    def update_selected_value(self, value: str):
        """
        Seçilen hücre değeri burada görüntülenecek.
        """
        if hasattr(self.table_panel, 'selected_value'):
            self.table_panel.update_selected_value(value)