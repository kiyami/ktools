from PySide2.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PySide2.QtCore import Signal


class LeftPanel(QWidget):
    plot_clicked = Signal()
    fit_clicked = Signal()
    peaks_clicked = Signal()
    clear_clicked = Signal()

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        self.btn_plot = QPushButton("Plot Data")
        self.btn_fit = QPushButton("Gaussian Fit")
        self.btn_peaks = QPushButton("Find Peaks")
        self.btn_clear = QPushButton("Clear")

        layout.addWidget(self.btn_plot)
        layout.addWidget(self.btn_fit)
        layout.addWidget(self.btn_peaks)
        layout.addWidget(self.btn_clear)
        layout.addStretch()

        # signals
        self.btn_plot.clicked.connect(self.plot_clicked)
        self.btn_fit.clicked.connect(self.fit_clicked)
        self.btn_peaks.clicked.connect(self.peaks_clicked)
        self.btn_clear.clicked.connect(self.clear_clicked)