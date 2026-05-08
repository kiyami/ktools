from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QComboBox, QListWidget, QListWidgetItem,
)

from app.models.plot_model import PlotType

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class CanvasView(QWidget):

    def __init__(self):
        super().__init__()

        # ---------------- MATPLOTLIB ----------------
        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.ax = self.figure.add_subplot(111)

        # ---------------- UI ----------------
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.setContentsMargins(2,2,2,2)

        self.setLayout(layout)

    def plot(self, plot_item):

        if not plot_item.is_valid():
            return

        if not plot_item.settings:
            settings = dict()

        if plot_item.plot_type == PlotType.LINE:
            self.ax.plot(plot_item.x, plot_item.y, **settings)

        elif plot_item.plot_type == PlotType.SCATTER:
            self.ax.scatter(x=plot_item.x, y=plot_item.y, **settings)

        elif plot_item.plot_type == PlotType.HISTOGRAM:
            self.ax.hist(x=plot_item.x, **settings)

        elif plot_item.plot_type == PlotType.ERRORBAR:
            self.ax.errorbar(
                x=plot_item.x, 
                y=plot_item.y, 
                xerr=plot_item.xerr, 
                yerr=plot_item.yerr, 
                **settings
            )

        elif plot_item.plot_type == PlotType.ERRORBAR_ASYM:

            if (plot_item.xerr is None) and (plot_item.xerr2 is None):
                xerr = None
                
            elif (plot_item.xerr is None) and (plot_item.xerr2 is not None):
                xerr = plot_item.xerr2

            elif (plot_item.xerr is not None) and (plot_item.xerr2 is None):
                xerr = plot_item.xerr

            else:
                xerr = [plot_item.xerr,plot_item.xerr2]


            if (plot_item.yerr is None) and (plot_item.yerr2 is None):
                yerr = None
                
            elif (plot_item.yerr is None) and (plot_item.yerr2 is not None):
                yerr = plot_item.yerr2

            elif (plot_item.yerr is not None) and (plot_item.yerr2 is None):
                yerr = plot_item.yerr

            else:
                yerr = [plot_item.yerr,plot_item.yerr2]
            

            self.ax.errorbar(
                x=plot_item.x, 
                y=plot_item.y, 
                xerr=xerr, 
                yerr=yerr, 
                **settings
            )

        #self.ax.relim()
        #self.ax.autoscale_view()

        self.canvas.draw()

