from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Signal

from ui.components.button import PrimaryButton
from ui.components.card import Card
from ui.components.canvas import Canvas

from ui.styles.general_styles import Styles


class CanvasView(QWidget):
    clicked = Signal()

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.canvas = Canvas()

        # -------------------------------------
        top_layout = QHBoxLayout()

        self.button1 = PrimaryButton("Tıkla")
        self.button2 = PrimaryButton("Tıkla")
        self.button3 = PrimaryButton("Tıkla")
        self.button4 = PrimaryButton("Tıkla")
        self.button5 = PrimaryButton("Tıkla")
        self.button6 = PrimaryButton("Tıkla")

        top_layout.addWidget(self.button1)
        top_layout.addWidget(self.button2)
        top_layout.addWidget(self.button3)
        top_layout.addWidget(self.button4)
        top_layout.addWidget(self.button5)
        top_layout.addWidget(self.button6)

        # -------------------------------------
        bottom_layout = QHBoxLayout()

        self.button7 = PrimaryButton("Tıkla")
        self.button8 = PrimaryButton("Tıkla")
        self.button9 = PrimaryButton("Tıkla")

        bottom_layout.addWidget(self.button7,5)
        bottom_layout.addWidget(self.button8,1)
        bottom_layout.addWidget(self.button9,1)

        # -------------------------------------
        layout.addLayout(top_layout, 1)
        layout.addWidget(self.canvas, 12)
        layout.addLayout(bottom_layout, 1)

        self.setLayout(layout)

        self.button1.clicked.connect(self.clicked.emit)