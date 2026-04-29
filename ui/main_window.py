import numpy as np

from PySide2.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout

from ui.left_panel import LeftPanel
from ui.right_panel import RightPanel
from ui.menu_bar import create_menu_bar
from ui.tool_bar import create_tool_bar

from plotting.plot_canvas import PlotCanvas
from analysis.fitting import gaussian, fit_gaussian
from analysis.peaks import detect_peaks


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Scientific Plot Tool")
        self.resize(1300, 800)

        # ======================
        # MENU + TOOLBAR
        # ======================
        create_menu_bar(self)
        create_tool_bar(self)

        # ======================
        # CENTRAL LAYOUT
        # ======================
        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout(central)

        body = QHBoxLayout()

        self.left = LeftPanel()
        self.canvas = PlotCanvas()
        self.right = RightPanel()

        body.addWidget(self.left, stretch=1)
        body.addWidget(self.canvas, stretch=3)
        body.addWidget(self.right, stretch=1)

        layout.addLayout(body)

        # ======================
        # DATA
        # ======================
        self.x = np.linspace(-5, 5, 400)
        self.y = (
            3 * np.exp(-(self.x - 1)**2 / (2 * 1.2**2))
            + 1.5 * np.exp(-(self.x + 2)**2 / (2 * 0.5**2))
            + 0.2 * np.random.randn(len(self.x))
        )

        # ======================
        # CONNECT SIGNALS
        # ======================
        self._connect_signals()

    def _connect_signals(self):
        # LEFT PANEL
        self.left.plot_clicked.connect(self.plot_data)
        self.left.fit_clicked.connect(self.fit_data)
        self.left.peaks_clicked.connect(self.find_peaks)
        self.left.clear_clicked.connect(self.clear)

        # TOOLBAR
        self.action_plot.triggered.connect(self.plot_data)
        self.action_fit.triggered.connect(self.fit_data)
        self.action_peaks.triggered.connect(self.find_peaks)
        self.action_clear.triggered.connect(self.clear)

    # ======================
    # ACTIONS
    # ======================
    def plot_data(self):
        self.canvas.plot_data(self.x, self.y)
        self.right.set_text("Data plotted")

    def fit_data(self):
        params = fit_gaussian(self.x, self.y)
        y_fit = gaussian(self.x, *params)

        self.canvas.plot_fit(self.x, y_fit)

        self.right.set_text(
            f"A={params[0]:.2f}\n"
            f"x0={params[1]:.2f}\n"
            f"sigma={params[2]:.2f}"
        )

    def find_peaks(self):
        peaks = detect_peaks(self.y, height=1)
        self.canvas.plot_peaks(self.x, self.y, peaks)
        self.right.set_text(f"Peaks: {len(peaks)}")

    def clear(self):
        self.canvas.ax.clear()
        self.canvas.draw()
        self.right.set_text("-")

    # status helper (çok önerilir)
    def set_status(self, text):
        self.statusBar().showMessage(text)