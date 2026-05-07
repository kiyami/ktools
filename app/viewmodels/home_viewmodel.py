from PySide6.QtCore import QObject, Signal


class HomeViewModel(QObject):

    message_sended = Signal(str)

    def __init__(self):
        super().__init__()

    def log(self, text: str):
        self.message_sended.emit(text)
        