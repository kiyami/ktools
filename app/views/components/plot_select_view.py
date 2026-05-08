from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QComboBox,
    QGridLayout,
    QSizePolicy,
)

from app.models.plot_model import PlotType, PlotSelections


plot_types_info = [
    {
        "label": "Line",
        "plot_type": PlotType.LINE,
        "cols": ["x", "y"],
    },
    {
        "label": "Scatter",
        "plot_type": PlotType.SCATTER,
        "cols": ["x", "y"],
    },
    {
        "label": "Histogram",
        "plot_type": PlotType.HISTOGRAM,
        "cols": ["x"],
    },
    {
        "label": "Errorbar",
        "plot_type": PlotType.ERRORBAR,
        "cols": ["x", "y", "xerr", "yerr"],
    },
    {
        "label": "Errorbar (asym)",
        "plot_type": PlotType.ERRORBAR_ASYM,
        "cols": ["x", "y", "xerr", "yerr", "xerr2", "yerr2"],
    },
]

class PlotSelectView(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.build_ui()

    def build_ui(self):

        layout = QGridLayout()

        # sıkı spacing
        layout.setHorizontalSpacing(8)
        layout.setVerticalSpacing(6)

        # dış margin
        layout.setContentsMargins(4, 4, 4, 4)

        # ---------------- ROW 1 ----------------
        label_main = QLabel("Plot Type")
        self.selection_combo = QComboBox()

        for info in plot_types_info:
            label = info["label"]
            item  = info["plot_type"]
            self.selection_combo.addItem(label, item)

        # ---------------- ROW 2 ----------------
        label_x = QLabel("X")
        combo_x = QComboBox()

        label_y = QLabel("Y")
        combo_y = QComboBox()

        # ---------------- ROW 3 ----------------
        label_xerr = QLabel("Xerr")
        combo_xerr = QComboBox()

        label_yerr = QLabel("Yerr")
        combo_yerr = QComboBox()

        # ---------------- ROW 4 ----------------
        label_xerr2 = QLabel("Xerr2")
        combo_xerr2 = QComboBox()

        label_yerr2 = QLabel("Yerr2")
        combo_yerr2 = QComboBox()

        # minimum sıkışabilir yapı
        self.header_combos = {
            "x":     combo_x,     "y":     combo_y,
            "xerr":  combo_xerr,  "yerr":  combo_yerr,
            "xerr2": combo_xerr2, "yerr2": combo_yerr2
        }

        self.header_labels = {
            "x":     label_x,     "y":     label_y,
            "xerr":  label_xerr,  "yerr":  label_yerr,
            "xerr2": label_xerr2, "yerr2": label_yerr2
        }

        self.selection_combo.setMinimumWidth(80)
        self.selection_combo.setSizePolicy(
            QSizePolicy.MinimumExpanding,
            QSizePolicy.Fixed
        )

        for _,combo in self.header_combos.items():
            combo.setMinimumWidth(80)

            # sola doğru daralabilsin
            combo.setSizePolicy(
                QSizePolicy.MinimumExpanding,
                QSizePolicy.Fixed
            )

        # ---------------- GRID ----------------

        # row 0
        layout.addWidget(label_main, 0, 0)
        layout.addWidget(self.selection_combo, 0, 1, 1, 3)

        # row 1
        layout.addWidget(label_x, 1, 0)
        layout.addWidget(combo_x, 1, 1)

        layout.addWidget(label_y, 1, 2)
        layout.addWidget(combo_y, 1, 3)

        # row 2
        layout.addWidget(label_xerr, 2, 0)
        layout.addWidget(combo_xerr, 2, 1)

        layout.addWidget(label_yerr, 2, 2)
        layout.addWidget(combo_yerr, 2, 3)

        # row 3
        layout.addWidget(label_xerr2, 3, 0)
        layout.addWidget(combo_xerr2, 3, 1)

        layout.addWidget(label_yerr2, 3, 2)
        layout.addWidget(combo_yerr2, 3, 3)

        # stretch ayarları
        layout.setColumnStretch(0, 0)
        layout.setColumnStretch(1, 1)

        layout.setColumnStretch(2, 0)
        layout.setColumnStretch(3, 1)

        self.setLayout(layout)

        # initialize
        self.selection_combo.setCurrentIndex(0)
        self.set_visibility(0)

        # signals
        self.selection_combo.currentIndexChanged.connect(self.set_visibility)

    def fill_headers(self, headers):
        self.headers = headers
        for label,combo in self.header_combos.items():
            combo.clear()

            if "err" in label:
                combo.addItem("None")

            combo.addItems(headers)

    def set_visibility(self,index):

        if index < 0:
            index = 0

        selected_plot_info = plot_types_info[index]

        for (key, label), (_, combo) in zip(
                self.header_labels.items(), self.header_combos.items()
            ):
            if key in selected_plot_info["cols"]:
                label.setEnabled(True)
                combo.setEnabled(True)
            else:
                label.setEnabled(False)
                combo.setEnabled(False)
                #combo.setCurrentIndex(0)

    def reset(self):
        self.headers = []
        self.selection_combo.setCurrentIndex(0)
        self.set_visibility(0)
        for combo in self.header_combos.values():
            combo.clear()

    def get_selections(self):

        selections = PlotSelections()
        selections.plot_type = self.selection_combo.currentData()

        plot_type_index = self.selection_combo.currentIndex()
        selected_plot_info = plot_types_info[plot_type_index]

        for col in selected_plot_info["cols"]:
            value = self.header_combos[col].currentText()

            # error sütunlarında "None" seçeneği var, onu None'a çeviriyorum.
            if value == "None":
                value = None

            setattr(selections, col, value)

        return selections
