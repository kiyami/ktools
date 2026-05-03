from PySide6.QtCore import QObject, Signal


class HomeViewModel(QObject):

    toggle = Signal()

    def __init__(self):
        super().__init__()

    def make_toggle(self):
        self.toggle.emit()
        