from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from ui.views.canvas_view import CanvasView
from ui.views.list_view import DataListView

from ui.views.data_view import DataView

import random


class HomeView(QWidget):
    def __init__(self, controller):
        super().__init__()

        self.controller = controller

        layout = QHBoxLayout()

        self.canvas_view = CanvasView()

        self.data_view = DataView()
        self.data_view.setFixedWidth(250)

        # self.list_view = DataListView()
        # self.list_view.setFixedWidth(200)

        # layout.addWidget(self.canvas_view)
        # layout.addWidget(self.list_view)

        layout.addWidget(self.canvas_view)
        layout.addWidget(self.data_view)
        self.setLayout(layout)

    #     # Event bağlantısı
    #     self.canvas_view.clicked.connect(self.on_click)
    #     self.list_view.item_selected.connect(self.on_item_selected)

    # def generate_data(self):
    #     x = list(range(10))
    #     y = [random.randint(0, 10) for _ in range(10)]

    #     return x,y

    # def on_click(self):
    #     self.x, self.y = self.generate_data()
    #     self.canvas_view.canvas.plot(self.x, self.y)
    #     self.canvas_view.card.content_label.setText("Butona tıklandı!")

    #     self.list_view.set_data(self.x, self.y)

    # def on_item_selected(self, x, y, index):
    #     self.canvas_view.canvas.ax.clear()
    #     self.canvas_view.canvas.ax.plot(self.x, self.y)
    #     self.canvas_view.canvas.ax.scatter([x], [y], color="red", s=100)
    #     self.canvas_view.canvas.canvas.draw()