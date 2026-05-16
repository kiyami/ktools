from PySide6.QtCore import QObject, Signal


class CanvasPanelViewModel(QObject):

    message_sent = Signal(str)

    def __init__(self):
        super().__init__()

    def send_message(self, message: str):
        self.message_sent.emit(message)
