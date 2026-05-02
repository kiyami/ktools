from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Signal

from app.views.data_table_view import DataTableView
from app.views.components.button import PrimaryButton
from app.views.styles.general_styles import Styles


class DataPanelView(QWidget):

    add_clicked = Signal()
    remove_clicked = Signal()

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        button_layout = QHBoxLayout()

        self.add_data_button = PrimaryButton("Add Data")
        self.remove_data_button = PrimaryButton(
            "Remove Data", style=Styles.primary_button_style_2
        )

        button_layout.addWidget(self.add_data_button)
        button_layout.addWidget(self.remove_data_button)

        self.data_table = DataTableView()
        self.screen = QWidget()

        layout.addLayout(button_layout, 1)
        layout.addWidget(self.data_table, 10)
        layout.addWidget(self.screen, 3)

        self.setLayout(layout)

        # 🔥 sadece event yay
        self.add_data_button.clicked.connect(self.add_clicked)
        self.remove_data_button.clicked.connect(self.remove_clicked)