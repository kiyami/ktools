from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QComboBox, QListWidget, QListWidgetItem,
)

from app.models.plot_model import PlotType, ArtistItem

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class CanvasView(QWidget):

    artist_plotted = Signal(object)

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

        artist_item = ArtistItem()

        if not plot_item.is_valid():
            return

        if not plot_item.settings:
            settings = dict()
        else:
            settings = plot_item.settings

        if plot_item.plot_type == PlotType.LINE:
            artist = self.ax.plot(plot_item.x, plot_item.y, **settings)[0]

            artist_item.plot_type = PlotType.LINE
            artist_item.label = "Line Plot"
            artist_item.obj = artist
            artist_item.misc = None


        elif plot_item.plot_type == PlotType.SCATTER:
            artist = self.ax.scatter(x=plot_item.x, y=plot_item.y, **settings)

            artist_item.plot_type = PlotType.SCATTER
            artist_item.label = "Scatter Plot"
            artist_item.obj = artist
            artist_item.misc = None

        elif plot_item.plot_type == PlotType.HISTOGRAM:
            bin_values, bin_edges, artist = self.ax.hist(x=plot_item.x, **settings)

            artist_item.plot_type = PlotType.HISTOGRAM
            artist_item.label = "Histogram Plot"
            artist_item.obj = artist
            artist_item.misc = {
                "bin_values": bin_values,
                "bin_edges": bin_edges,
            }

        elif plot_item.plot_type == PlotType.ERRORBAR:
            artist = self.ax.errorbar(
                x=plot_item.x, 
                y=plot_item.y, 
                xerr=plot_item.xerr, 
                yerr=plot_item.yerr, 
                **settings
            )

            artist_item.plot_type = PlotType.ERRORBAR
            artist_item.label = "Errorbar Plot"
            artist_item.obj = artist
            artist_item.misc = None

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
            

            artist = self.ax.errorbar(
                x=plot_item.x, 
                y=plot_item.y, 
                xerr=xerr, 
                yerr=yerr, 
                **settings
            )

            artist_item.plot_type = PlotType.ERRORBAR_ASYM
            artist_item.label = "Errorbar (asym) Plot"
            artist_item.obj = artist
            artist_item.misc = None

        #self.ax.relim()
        #self.ax.autoscale_view()

        # label varsa legend aç, yoksa açma
        _, labels = self.ax.get_legend_handles_labels()
        if any(labels):
            self.ax.legend()

        self.figure.tight_layout()
        self.canvas.draw()

        self.artist_plotted.emit(artist_item)

    def redraw(self):
        # label varsa legend aç, yoksa açma
        _, labels = self.ax.get_legend_handles_labels()
        if any(labels):
            self.ax.legend()

        self.figure.tight_layout()
        self.canvas.draw_idle()

    def reset(self):
        self.figure.set_facecolor("white")
        self.ax.clear()
        self.redraw()

    def savefig(self, file_path, dpi=300, bbox_inches="tight"):
        self.figure.savefig(
            fname=file_path, 
            dpi=dpi, 
            bbox_inches=bbox_inches,
        )
        