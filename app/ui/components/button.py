from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Signal

class PrimaryButton(QPushButton):
    clicked_custom = Signal()

    def __init__(self, text):
        super().__init__(text)

        self.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 10px;
                border-radius: 5px;
            }
        """)

        self.clicked.connect(self.emit_custom)

    def emit_custom(self):
        self.clicked_custom.emit()