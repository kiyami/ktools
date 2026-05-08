from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QLineEdit, QSizePolicy, QSplitter
)

from PySide6.QtCore import Signal, Qt

from app.views.components.canvas_view import CanvasView
from app.views.components.plot_select_view import PlotSelectView

class CanvasPanel(QWidget):

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

        add_settings_layout = QHBoxLayout()
        add_settings_layout.addWidget(self.add_plot_button)
        add_settings_layout.addWidget(self.settings_button)
        add_settings_layout.setContentsMargins(0,0,0,0)
        add_settings_layout.setSpacing(5)

        layout_bottom_right.addLayout(add_settings_layout,1)
        layout_bottom_right.addWidget(self.plot_list,3)
        layout_bottom_right.addWidget(self.remove_plot_button,1)
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



