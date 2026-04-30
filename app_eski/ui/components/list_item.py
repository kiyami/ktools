from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel
from PySide6.QtCore import Signal


class ListItem(QWidget):
    clicked = Signal(float, float, int)

    def __init__(self, x, y, index):
        super().__init__()

        self.x = x
        self.y = y
        self.index = index

        layout = QHBoxLayout()

        self.label = QLabel(f"{index} → x: {x}, y: {y}")
        layout.addWidget(self.label)

        self.setLayout(layout)

        self.setStyleSheet("""
            QWidget {
                padding: 5px;
            }
            QWidget:hover {
                background-color: #e0e0e0;
            }
        """)

    def mousePressEvent(self, event):
        self.clicked.emit(self.x, self.y, self.index)