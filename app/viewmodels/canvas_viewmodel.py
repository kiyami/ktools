from PySide6.QtCore import QObject, Signal
from app.services.data_service import DataService


class CanvasViewModel(QObject):

    message_sended = Signal(str)

    selected_row_requested = Signal()

    plot_data_sended = Signal(object)

    artist_added = Signal(object)

    artist_removed = Signal(object)

    reset_done = Signal()

    settings_panel_requested = Signal(object)

    def __init__(self, data_service: DataService):
        super().__init__()
        self.data_service = data_service
        self.current_selections = None
        self.artist_list = []

    def request_selected_row(self, selections):
        self.current_selections = selections
        self.selected_row_requested.emit() 

    def get_plot_data(self, selected_row):

        if selected_row < self.data_service.get_length():

            data = self.data_service.get_numeric(selected_row)
            data_headers = self.data_service.get_headers(selected_row)
            
            plot_settings = self.current_selections.get_settings()
            plot_headers = self.current_selections.get_headers()
            Constructor = self.current_selections.get_constructor()

            selected_data = dict()

            for identifier,plot_header in plot_headers.items():
                if plot_header:
                    header_index = data_headers.index(plot_header)
                    selected_data[identifier] = data[:,header_index]

            plot_item = Constructor(**selected_data)
            plot_item.settings = plot_settings

            self.plot_data_sended.emit(plot_item)

        else:
            self.message_sended.emit("Invalid data to plot..")

    def add_artist(self, artist_item):
        self.artist_list.append(artist_item)
        self.artist_added.emit(self.artist_list)

    def remove_artist(self, index):
        artist_item = self.artist_list[index]
        artist_item.remove()
        del self.artist_list[index]
        self.artist_removed.emit(self.artist_list)

    def reset(self):
        for artist_item in self.artist_list:
            artist_item.remove()

        self.artist_list = []

        self.reset_done.emit()

    def request_settings_panel(self, index):
        artist_item = self.artist_list[index]
        self.settings_panel_requested.emit(artist_item)
