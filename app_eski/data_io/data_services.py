from data_io.data_reader import read_data_txt


class DataService:
    def load(self, filename):
        return read_data_txt(filename)