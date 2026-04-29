from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class PlotCanvas(FigureCanvas):
    def __init__(self):
        self.figure = Figure()
        self.ax = self.figure.add_subplot(111)
        super().__init__(self.figure)

    def plot_data(self, x, y):
        self.ax.clear()
        self.ax.plot(x, y, label="Data")
        self.ax.legend()
        self.draw()

    def plot_fit(self, x, y_fit):
        self.ax.plot(x, y_fit, '--', label="Fit")
        self.ax.legend()
        self.draw()

    def plot_peaks(self, x, y, peaks):
        self.ax.plot(x[peaks], y[peaks], "ro", label="Peaks")
        self.ax.legend()
        self.draw()