from PySide6.QtCore import QObject, Signal


class CanvasViewModel(QObject):

    plot_ready = Signal(object, object)  # x, y

    def __init__(self):
        super().__init__()
        self.result = None

    def set_data(self, result):
        self.result = result

    def generate_plot(self):
        if not self.result or not self.result.data.any():
            return

        data = self.result.data

        if data.shape[1] < 2:
            return

        x = data[:, 0]
        y = data[:, 1]

        self.plot_ready.emit(x, y)