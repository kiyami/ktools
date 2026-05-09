from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QListWidget,
    QLabel,
)

from app.views.property_editor_view import PropertyEditorView

from app.adapters.artist_adapter import ArtistAdapter
from app.adapters.axis_adapter import AxisAdapter
from app.adapters.figure_adapter import FigureAdapter

from app.config.axis_settings_config import AXIS_SETTINGS_CONFIG
from app.config.figure_settings_config import FIGURE_SETTINGS_CONFIG
from app.config.plot_settings_config import PLOT_SETTINGS_CONFIG


class PlotSettingsView(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()

        self.figure_editor = PropertyEditorView()
        self.axis_editor = PropertyEditorView()

        self.artist_list = QListWidget()

        self.artist_editor = PropertyEditorView()

        layout.addWidget(QLabel("Figure"))
        layout.addWidget(self.figure_editor)

        layout.addWidget(QLabel("Axis"))
        layout.addWidget(self.axis_editor)

        layout.addWidget(QLabel("Artists"))
        layout.addWidget(self.artist_list)

        layout.addWidget(QLabel("Artist Settings"))
        layout.addWidget(self.artist_editor)

        self.setLayout(layout)

        self.artist_list.currentRowChanged.connect(
            self._artist_changed
        )

    def load(self, context):

        self.context = context

        # figure
        self.figure_editor.load(
            target=context.figure,
            config=FIGURE_SETTINGS_CONFIG,
            adapter=FigureAdapter,
        )

        # axis
        self.axis_editor.load(
            target=context.axes,
            config=AXIS_SETTINGS_CONFIG,
            adapter=AxisAdapter,
        )

        # artists
        self.artist_list.clear()

        for artist in context.artists:
            self.artist_list.addItem(artist.label)

    def _artist_changed(self, row):

        if row < 0:
            return

        artist = self.context.artists[row]

        self.artist_editor.load(
            target=artist,
            config=PLOT_SETTINGS_CONFIG[artist.plot_type],
            adapter=ArtistAdapter,
        )