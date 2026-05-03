from PySide6.QtCore import QObject, Signal
from app.models.plot_item import PlotItem


class CanvasViewModel(QObject):

    plots_changed = Signal(list)   # PlotItem list
    redraw = Signal(list)          # (x,y) list

    def __init__(self):
        super().__init__()

        self.data = None
        self.plots = []
        self._id = 0

    def set_data(self, result):
        self.data = result.numeric_data

    # ---------------- ADD ----------------
    def add_plot(self, x_idx, y_idx):

        if self.data is None:
            return

        x = self.data[:, x_idx]
        y = self.data[:, y_idx]

        plot = PlotItem(
            id=self._id,
            x_idx=x_idx,
            y_idx=y_idx,
            label=f"Plot {self._id+1}: Col{x_idx+1} vs Col{y_idx+1}"
        )

        self._id += 1

        self.plots.append((plot, x, y))
        self._refresh()

    # ---------------- REMOVE ----------------
    def remove_plot(self, plot_id):

        self.plots = [
            (p, x, y)
            for (p, x, y) in self.plots
            if p.id != plot_id
        ]

        self._refresh()

    # ---------------- INTERNAL ----------------
    def _refresh(self):

        plot_items = [p for (p, _, _) in self.plots]

        self.plots_changed.emit(plot_items)

        self.redraw.emit([
            (x, y) for (_, x, y) in self.plots
        ])
