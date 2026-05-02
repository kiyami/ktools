from PySide6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class Canvas(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        self.ax = self.figure.add_subplot(111)

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def plot(self, x, y):
        self.ax.clear()
        self.ax.plot(x, y)
        self.ax.set_title("Örnek Grafik")
        self.canvas.draw()

    def scatter(self, x, y):
        self.ax.clear()
        self.ax.scatter(x, y)
        self.canvas.draw()