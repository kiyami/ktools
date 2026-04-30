from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class Card(QWidget):
    def __init__(self, title, content):
        super().__init__()

        layout = QVBoxLayout()

        self.title_label = QLabel(title)
        self.content_label = QLabel(content)

        layout.addWidget(self.title_label)
        layout.addWidget(self.content_label)

        self.setLayout(layout)
        
