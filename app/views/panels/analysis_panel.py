from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class AnalysisPanelView(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        main_widget = QLabel("AnalysisPanel")

        layout.addWidget(main_widget)

        self.setLayout(layout)

