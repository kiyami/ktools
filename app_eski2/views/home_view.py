# app/views/home_view.py

from PySide6.QtWidgets import QWidget, QHBoxLayout

from app.views.canvas_panel_view import CanvasPanelView
from app.views.data_panel_view import DataPanelView


class HomeView(QWidget):

    def __init__(self, vm):
        super().__init__()

        self.vm = vm

        self.canvas_panel_view = CanvasPanelView()
        self.data_panel_view = DataPanelView()

        layout = QHBoxLayout()
        layout.addWidget(self.canvas_panel_view)
        layout.addWidget(self.data_panel_view)

        self.setLayout(layout)

        self.vm.data_loaded.connect(self.on_data_loaded)
        self.vm.data_loaded.connect(self.on_data_loaded)

    def on_data_loaded(self, cols, names):
        self.data_panel_view.set_data(cols, names)

    def load_data(self):
        self.vm.load_file("./data/sample_1.txt")