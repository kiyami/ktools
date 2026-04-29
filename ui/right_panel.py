from PySide2.QtWidgets import QWidget, QVBoxLayout, QLabel


class RightPanel(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        self.title = QLabel("Results")
        self.output = QLabel("-")
        self.output.setWordWrap(True)

        layout.addWidget(self.title)
        layout.addWidget(self.output)
        layout.addStretch()

    def set_text(self, text):
        self.output.setText(text)