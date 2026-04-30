from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from ui.styles.general_styles import Styles

class DataView(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.button_panel = QWidget()
        self.data_panel = QWidget()
        self.screen_panel = QWidget()

        self.button_panel.setStyleSheet(Styles.debug_styles)
        self.data_panel.setStyleSheet(Styles.debug_styles)
        self.screen_panel.setStyleSheet(Styles.debug_styles)

        layout.addWidget(self.button_panel, 1)
        layout.addWidget(self.data_panel, 10)
        layout.addWidget(self.screen_panel, 3)

        self.setLayout(layout)
