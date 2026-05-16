from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QDragEnterEvent, QDropEvent


class DropLabel(QLabel):
    file_dropped = Signal(str)

    def __init__(self, text="Drag & Drop\nData File"):
        super().__init__(text)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event: QDropEvent):
        urls = event.mimeData().urls()

        if urls:
            file_path = urls[0].toLocalFile()
            self.file_dropped.emit(file_path)
            event.acceptProposedAction()