from PySide6.QtCore import QObject, Signal
from app.services.data_service import DataService


class AnalysisViewModel(QObject):

    message_sended = Signal(str)
    
    def __init__(self, data_service: DataService):
        super().__init__()
        self.data_service = data_service

