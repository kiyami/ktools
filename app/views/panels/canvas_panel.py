from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QLineEdit, QSizePolicy, QSplitter
)

from PySide6.QtCore import Signal, Qt

from app.views.components.canvas_view import CanvasView
from app.views.components.plot_select_view import PlotSelectView

class CanvasPanel(QWidget):

    plot_data_requested = Signal(object)
    remove_plot_requested = Signal(int)
    reset_requested = Signal()
    artist_plotted = Signal(object)

    settings_button_clicked = Signal()

    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()
        
        splitter = QSplitter(Qt.Vertical)

        self.canvas_view = CanvasView()
        self.canvas_view.setObjectName("canvasArea")

        bottom_widget = QWidget()
        layout_bottom = QHBoxLayout()

        layout_bottom_left = QHBoxLayout()
        self.plot_select = PlotSelectView()

        layout_bottom_left.addWidget(self.plot_select)

        layout_bottom_right = QVBoxLayout()
        self.add_plot_button = QPushButton("Add Plot")
        self.settings_button = QPushButton("Settings")
        self.plot_list = QListWidget()
        self.remove_plot_button = QPushButton("Remove Plot")
        self.reset_button = QPushButton("Reset")

        add_settings_layout = QHBoxLayout()
        add_settings_layout.addWidget(self.add_plot_button,1)
        add_settings_layout.addWidget(self.settings_button,1)
        add_settings_layout.setContentsMargins(0,0,0,0)
        add_settings_layout.setSpacing(5)

        remove_reset_layout = QHBoxLayout()
        remove_reset_layout.addWidget(self.remove_plot_button,1)
        remove_reset_layout.addWidget(self.reset_button,1)
        remove_reset_layout.setContentsMargins(0,0,0,0)
        remove_reset_layout.setSpacing(5)

        layout_bottom_right.addLayout(add_settings_layout,1)
        layout_bottom_right.addWidget(self.plot_list,3)
        layout_bottom_right.addLayout(remove_reset_layout,1)
        layout_bottom_right.setContentsMargins(0,0,0,0)
        layout_bottom_right.setSpacing(5)

        layout_bottom.addLayout(layout_bottom_left,3)
        layout_bottom.addLayout(layout_bottom_right,2)

        bottom_widget.setLayout(layout_bottom)

        splitter.addWidget(self.canvas_view)
        splitter.addWidget(bottom_widget)

        splitter.setSizes([500, 100])

        splitter.setStretchFactor(0, 5)  # top
        splitter.setStretchFactor(1, 1)  # bottom

        main_layout.addWidget(splitter)
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(5)

        self.setLayout(main_layout)

        # signals
        self.add_plot_button.clicked.connect(self.request_plot_data)
        self.settings_button.clicked.connect(self.request_settings)
        self.remove_plot_button.clicked.connect(self.request_remove_plot)
        self.reset_button.clicked.connect(self.reset_requested.emit)

        self.canvas_view.artist_plotted.connect(self.artist_plotted.emit)

        # fig objects from inner layer
        self.figure = self.canvas_view.figure
        self.canvas = self.canvas_view.canvas
        self.ax = self.canvas_view.ax

    def fill_headers(self, headers):
        self.plot_select.fill_headers(headers)

    def reset(self):
        self.plot_list.clear()
        self.plot_select.reset()
        self.canvas_view.reset()

    def get_selections(self):
        return self.plot_select.get_selections()

    def request_plot_data(self):
        selections = self.plot_select.get_selections()
        self.plot_data_requested.emit(selections)

    def request_remove_plot(self):
        index = self.get_row()
        self.remove_plot_requested.emit(index)

    def plot(self, plot_item):
        self.canvas_view.plot(plot_item)

    def get_row(self):
        return self.plot_list.currentRow()
    
    def set_row(self, row):
        self.plot_list.setCurrentRow(row)

    def update_list(self, artist_list):
        self.plot_list.clear()
        for artist_item in artist_list:
            label = artist_item.label
            self.plot_list.addItem(label)

    def redraw(self):
        self.canvas_view.redraw()

    def request_settings(self):
        if self.plot_list.count() != 0:
            self.settings_button_clicked.emit()


