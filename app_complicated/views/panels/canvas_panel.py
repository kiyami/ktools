from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QPushButton, QComboBox, QLabel
)
from PySide6.QtCore import Signal

from app.views.components.canvas_view import CanvasView
from app.canvas_core.renderer import CanvasRenderer


class CanvasPanel(QWidget):

    plot_requested = Signal(dict)

    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()

        # ---------------- TOP ----------------
        top_bar = QHBoxLayout()

        self.plot_type_combo = QComboBox()
        self.plot_type_combo.addItems([
            "line",
            "scatter",
            "hist",
            "errorbar_sym",
            "errorbar_asym"
        ])

        top_bar.addWidget(QLabel("Plot"))
        top_bar.addWidget(self.plot_type_combo)

        # ---------------- GRID ----------------
        self.grid = QGridLayout()

        self.fields = {
            "x": self._create_field("X"),
            "y": self._create_field("Y"),

            "xerr": self._create_field("X Err"),
            "yerr": self._create_field("Y Err"),

            "xerr_low": self._create_field("X Err Low"),
            "xerr_high": self._create_field("X Err High"),
            "yerr_low": self._create_field("Y Err Low"),
            "yerr_high": self._create_field("Y Err High"),
        }

        layout_map = [
            ("x", 0, 0), ("y", 0, 1),

            ("xerr", 1, 0), ("yerr", 1, 1),

            ("xerr_low", 2, 0), ("yerr_low", 2, 1),
            ("xerr_high", 3, 0), ("yerr_high", 3, 1),
        ]

        for key, r, c in layout_map:
            label, combo = self.fields[key]
            self.grid.addWidget(label, r, c * 2)
            self.grid.addWidget(combo, r, c * 2 + 1)

        # ---------------- BUTTON + CANVAS ----------------
        self.plot_button = QPushButton("Plot")
        self.canvas_view = CanvasView()

        main_layout.addLayout(top_bar)
        main_layout.addLayout(self.grid)
        main_layout.addWidget(self.plot_button)
        main_layout.addWidget(self.canvas_view)

        self.setLayout(main_layout)

        # ---------------- SIGNALS ----------------
        self.plot_button.clicked.connect(self._emit_plot)
        self.plot_type_combo.currentTextChanged.connect(self._update_ui)

        self._update_ui(self.plot_type_combo.currentText())

    # ---------------- FIELD ----------------
    def _create_field(self, text):
        label = QLabel(text)
        combo = QComboBox()
        combo.setMinimumWidth(120)
        return label, combo

    def _set_visible(self, key, visible):
        label, combo = self.fields[key]
        label.setVisible(visible)
        combo.setVisible(visible)

    # ---------------- UI STATE ----------------
    def _update_ui(self, plot_type):

        for key in self.fields:
            self._set_visible(key, False)

        self._set_visible("x", True)
        self._set_visible("y", True)

        if plot_type == "errorbar_sym":
            self._set_visible("xerr", True)
            self._set_visible("yerr", True)

        elif plot_type == "errorbar_asym":
            self._set_visible("xerr_low", True)
            self._set_visible("xerr_high", True)
            self._set_visible("yerr_low", True)
            self._set_visible("yerr_high", True)

    # ---------------- DATA ----------------
    def set_columns(self, headers: list[str]):

        for _, combo in self.fields.values():
            combo.clear()
            combo.addItem("None", None)
            for i, h in enumerate(headers):
                combo.addItem(h, i)

    # ---------------- EMIT ----------------
    def _emit_plot(self):

        payload = {
            "plot_type": self.plot_type_combo.currentText(),
        }

        for key, (_, combo) in self.fields.items():
            payload[key] = combo.currentData()

        self.plot_requested.emit(payload)

    # ---------------- EXTERNAL ----------------
    def get_axis(self):
        return self.canvas_view.get_axis()

    def set_renderer(self, renderer: CanvasRenderer):
        self.canvas_view.set_renderer(renderer)

    def set_state(self, state):
        self.canvas_view.set_state(state)
