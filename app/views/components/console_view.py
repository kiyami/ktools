from PySide6.QtWidgets import QPlainTextEdit
from PySide6.QtCore import Slot
from PySide6.QtGui import QFont


class ConsoleView(QPlainTextEdit):

    def __init__(self):
        super().__init__()
        self._setup_ui()

    def _setup_ui(self):
        self.setReadOnly(True)

        # font
        font = QFont("Menlo", 11)
        font.setStyleHint(QFont.Monospace)
        self.setFont(font)

        # line wrap
        self.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)
        
        # internal margins
        self.setViewportMargins(1,1,1,1)

    # ---------------- PUBLIC API ----------------
    @Slot(str)
    def append_text(self, text: str):

        self.appendPlainText(text)

        scrollbar = self.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())

    @Slot()
    def clear_output(self):
        self.clear()