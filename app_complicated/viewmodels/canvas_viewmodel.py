from PySide6.QtCore import QObject, Signal

from app.canvas_core.state import CanvasState
from app.canvas_core.plot_entity import PlotEntity


class CanvasViewModel(QObject):

    state_changed = Signal(object)

    def __init__(self, store):
        super().__init__()
        self.state = CanvasState()
        self.store = store

    def add_plot(self, plot: PlotEntity):
        self.state.plots.append(plot)
        self.state_changed.emit(self.state)

    def toggle_plot(self, plot_id: int):
        for p in self.state.plots:
            if p.id == plot_id:
                p.visible = not p.visible

        self.state_changed.emit(self.state)

    def create_plot(self, result, payload: dict):

        plot_type = payload.get("plot_type")

        if result.numeric_data is None:
            return

        plot_id = len(self.state.plots)

        plot = PlotEntity(
            id=plot_id,
            data_id=getattr(result, "id", plot_id),
            label=result.label,
            plot_type=plot_type
        )

        # -----------------------
        # X / Y
        # -----------------------
        plot.x_col = payload.get("x")
        plot.y_col = payload.get("y")

        # -----------------------
        # SYMMETRIC ERRORBAR
        # -----------------------
        if plot_type == "errorbar_sym":
            plot.yerr_cols = (payload.get("yerr"),)
            plot.xerr_cols = (payload.get("xerr"),)

        # -----------------------
        # ASYMMETRIC ERRORBAR
        # -----------------------
        elif plot_type == "errorbar_asym":
            plot.yerr_cols = (
                payload.get("yerr_low"),
                payload.get("yerr_high")
            )

            plot.xerr_cols = (
                payload.get("xerr_low"),
                payload.get("xerr_high")
            )

        self.add_plot(plot)
