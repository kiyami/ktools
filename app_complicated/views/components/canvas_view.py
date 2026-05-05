from PySide6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from app.canvas_core.renderer import CanvasRenderer


class CanvasView(QWidget):

    def __init__(self):
        super().__init__()

        self.figure = Figure()
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self.figure)

        self.renderer = None
        self._state = None

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    # controller burayı kullanır
    def set_renderer(self, renderer: CanvasRenderer):
        self.renderer = renderer

    def get_axis(self):
        return self.ax

    def set_state(self, state):
        self._state = state

        if self.renderer:
            self.renderer.render(state)
            self.canvas.draw()