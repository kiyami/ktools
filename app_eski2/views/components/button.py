from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Signal

from app.views.styles.general_styles import Styles

class PrimaryButton(QPushButton):
    clicked_custom = Signal()

    def __init__(self, text, style=None):
        super().__init__(text)

        if not style:
            style = Styles.primary_button_style

        self.setStyleSheet(style)

        self.clicked.connect(self.emit_custom)

    def emit_custom(self):
        self.clicked_custom.emit()