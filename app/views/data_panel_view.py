from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

from app.views.data_table_view import DataTableView
from app.views.styles.general_styles import Styles

class DataPanelView(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.buttons = QWidget()
        self.data_table = DataTableView()
        self.screen = QWidget()

        self.buttons.setStyleSheet(Styles.debug_styles)
        #self.data_table.setStyleSheet(Styles.debug_styles)
        self.screen.setStyleSheet(Styles.debug_styles)

        layout.addWidget(self.buttons, 1)
        layout.addWidget(self.data_table, 10)
        layout.addWidget(self.screen, 3)

        self.setLayout(layout)
