from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, 
    QLineEdit, QSizePolicy, QTextEdit
)

from PySide6.QtCore import Signal, Qt

from app.views.components.table_view import TableView


class TablePanel(QWidget):

    toggle_button_clicked = Signal()

    def __init__(self):
        super().__init__()

        self.load_button = QPushButton("Load Data")
        self.toggle_button = QPushButton("Toggle Table")

        self.table_view = TableView()

        self.table_list = QTextEdit()
        self.table_list.setReadOnly(True)

        self.remove_button = QPushButton("Remove Data")

        # HEADER LAYOUT
        header = QWidget()
        header_layout = QHBoxLayout()

        header_layout.addWidget(self.load_button, 0)
        header_layout.addWidget(self.toggle_button, 0)

        header_layout.setContentsMargins(0,0,0,0)

        header.setLayout(header_layout)

        header.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Fixed
        )
        header.setMinimumHeight(30)
        header.setMaximumHeight(30)

        # CONTENT LAYOUT
        self.content = QWidget()
        content_layout = QVBoxLayout()

        content_layout.addWidget(self.table_view, 5)
        content_layout.addWidget(self.table_list, 1)
        content_layout.addWidget(self.remove_button, 0)

        content_layout.setContentsMargins(0,0,0,0)

        self.content.setLayout(content_layout)

        self.content.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )

        # MAIN LAYOUT
        main_layout = QVBoxLayout()

        main_layout.addWidget(header, 0)   # sabit alan
        main_layout.addWidget(self.content, 1)  # büyüyen alan
        #main_layout.addStretch(1)
        
        main_layout.setAlignment(Qt.AlignTop)
        main_layout.setContentsMargins(0,0,0,0)

        self.setLayout(main_layout)

        # signals
        self.toggle_button.clicked.connect(self.toggle_button_clicked.emit)


    def toggle_table(self):
        self.content.setVisible(not self.content.isVisible())