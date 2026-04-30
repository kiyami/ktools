from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class DataPanel(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        self.title = QLabel("Data")
        self.output = QLabel("my data")
        self.output.setWordWrap(True)

        layout.addWidget(self.title)
        layout.addWidget(self.output)
        layout.addStretch()

    def set_text(self, text):
        self.output.setText(text)