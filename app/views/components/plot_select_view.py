from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QComboBox,
    QGridLayout,
    QSizePolicy,
)


plot_types_info = [
    {
        "key": "line",
        "label": "Line",
        "cols": ["X", "Y"],
    },
    {
        "key": "scatter",
        "label": "Scatter",
        "cols": ["X", "Y"],
    },
    {
        "key": "histogram",
        "label": "Histogram",
        "cols": ["X"],
    },
    {
        "key": "errorbar",
        "label": "Errorbar",
        "cols": ["X", "Y", "Xerr", "Yerr"],
    },
    {
        "key": "errorbar_asym",
        "label": "Errorbar (asym)",
        "cols": ["X", "Y", "Xerr", "Yerr", "Xerr2", "Yerr2"],
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

        self.selection_combo.addItems(
            item["label"] for item in plot_types_info
        )

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
        self.header_combos = [
            combo_x, combo_y,
            combo_xerr, combo_yerr,
            combo_xerr2, combo_yerr2
        ]

        self.header_labels = [
            label_x, label_y,
            label_xerr, label_yerr,
            label_xerr2, label_yerr2,
        ]

        for combo in self.header_combos + [self.selection_combo]:
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
        for i,combo in enumerate(self.header_combos):
            combo.clear()

            # error sütunları boş seçilebilir
            if i >=2:
                combo.addItems(["None"])

            combo.addItems(headers)

    def set_visibility(self,index):

        if index < 0:
            index = 0

        item = plot_types_info[index]

        mask = [
            "X" in item["cols"],
            "Y" in item["cols"],

            "Xerr" in item["cols"],
            "Yerr" in item["cols"],

            "Xerr2" in item["cols"],
            "Yerr2" in item["cols"],
        ]

        for m,label,combo in zip(mask, self.header_labels, self.header_combos):
            if m:
                label.setEnabled(True)
                combo.setEnabled(True)
            else:
                label.setEnabled(False)
                combo.setEnabled(False)
                combo.setCurrentIndex(0)

    def reset(self):
        self.selection_combo.setCurrentIndex(0)
        self.set_visibility(0)
        for combo in self.header_combos:
            combo.clear()