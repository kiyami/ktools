import numpy as np

from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout

from ui.control_panel import ControlPanel
from ui.results_panel import ResultsPanel
from ui.data_panel import DataPanel
from ui.menu_bar import create_menu_bar
from ui.tool_bar import create_tool_bar

from plotting.plot_canvas import PlotCanvas
from analysis.fitting import gaussian, fit_gaussian
from analysis.peaks import detect_peaks


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("k-Tools")
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

        self.control = ControlPanel()
        self.results = ResultsPanel()
        self.canvas  = PlotCanvas()

        self.left = QVBoxLayout()
        self.left.addWidget(self.control, stretch=1)
        self.left.addWidget(self.results, stretch=1)

        self.data = DataPanel()
        self.right = QVBoxLayout()
        self.right.addWidget(self.data, stretch=1)

        body.addLayout(self.left, stretch=1)
        body.addWidget(self.canvas, stretch=3)
        body.addWidget(self.data, stretch=1)

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
        self.control.plot_clicked.connect(self.plot_data)
        self.control.fit_clicked.connect(self.fit_data)
        self.control.peaks_clicked.connect(self.find_peaks)
        self.control.clear_clicked.connect(self.clear)

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
        self.results.set_text("Data plotted")

    def fit_data(self):
        params = fit_gaussian(self.x, self.y)
        y_fit = gaussian(self.x, *params)

        self.canvas.plot_fit(self.x, y_fit)

        self.results.set_text(
            f"A={params[0]:.2f}\n"
            f"x0={params[1]:.2f}\n"
            f"sigma={params[2]:.2f}"
        )

    def find_peaks(self):
        peaks = detect_peaks(self.y, height=1)
        self.canvas.plot_peaks(self.x, self.y, peaks)
        self.results.set_text(f"Peaks: {len(peaks)}")

    def clear(self):
        self.canvas.ax.clear()
        self.canvas.draw()
        self.results.set_text("-")

    # status helper (çok önerilir)
    def set_status(self, text):
        self.statusBar().showMessage(text)