from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QComboBox, QListWidget, QListWidgetItem,
)

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class CanvasView(QWidget):

    add_plot_clicked = Signal(int, int)
    remove_plot_clicked = Signal(int)

    def __init__(self):
        super().__init__()

        # ---------------- MATPLOTLIB ----------------
        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.ax = self.figure.add_subplot(111)

        # ---------------- UI ----------------
        layout = QVBoxLayout()

        controls = QHBoxLayout()

        self.x_combo = QComboBox()
        self.y_combo = QComboBox()
        self.add_btn = QPushButton("Add Plot")

        controls.addWidget(self.x_combo)
        controls.addWidget(self.y_combo)
        controls.addWidget(self.add_btn)

        self.plot_list = QListWidget()
        self.remove_btn = QPushButton("Remove Plot")

        layout.addLayout(controls)
        layout.addWidget(self.canvas)
        layout.addWidget(self.plot_list)
        layout.addWidget(self.remove_btn)

        self.setLayout(layout)

        # ---------------- SIGNALS ----------------
        self.add_btn.clicked.connect(self._emit_add)
        self.remove_btn.clicked.connect(self._emit_remove)

    # ---------------- EVENTS ----------------
    def _emit_add(self):
        self.add_plot_clicked.emit(
            self.x_combo.currentIndex(),
            self.y_combo.currentIndex()
        )

    def _emit_remove(self):
        item = self.plot_list.currentItem()
        if not item:
            return

        plot_id = item.data(Qt.UserRole)
        self.remove_plot_clicked.emit(plot_id)

    # ---------------- VIEW UPDATE ----------------
    def set_columns(self, headers):
        self.x_combo.clear()
        self.y_combo.clear()
        self.x_combo.addItems(headers)
        self.y_combo.addItems(headers)

    def update_plot_list(self, plots):
        self.plot_list.clear()

        for p in plots:
            item = QListWidgetItem(p.label)
            item.setData(Qt.UserRole, p.id)
            self.plot_list.addItem(item)

    def draw(self, plot_data):

        self.ax.clear()

        for x, y in plot_data:
            self.ax.plot(x, y)

        self.canvas.draw()