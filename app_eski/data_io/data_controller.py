

class DataController:
    def __init__(self, service):
        self.service = service

        self.columns = None
        self.colnames = None

    def load_file(self, filename):
        self.columns, self.colnames = self.service.load(filename)

    def get_plot_data(self):
        # default: ilk iki sütun
        return self.columns[0], self.columns[1]

    def get_list_data(self):
        return self.columns, self.colnames