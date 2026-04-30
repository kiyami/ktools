from PySide6.QtWidgets import QWidget, QVBoxLayout, QScrollArea
from ui.components.list_item import ListItem


class ScrollableList(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)

        self.container = QWidget()
        self.container_layout = QVBoxLayout(self.container)

        self.scroll.setWidget(self.container)

        self.layout.addWidget(self.scroll)

        self.items = []

    def set_data(self, x_list, y_list):
        # temizle
        for item in self.items:
            item.deleteLater()

        self.items.clear()

        for i, (x, y) in enumerate(zip(x_list, y_list)):
            item = ListItem(x, y, i)

            self.container_layout.addWidget(item)
            self.items.append(item)

    def on_item_clicked(self, callback):
        for item in self.items:
            item.clicked.connect(callback)