from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class DataPanelView(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        main_widget = QLabel("DataPanel")

        layout.addWidget(main_widget)

        self.setLayout(layout)

