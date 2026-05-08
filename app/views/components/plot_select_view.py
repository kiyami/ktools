from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QComboBox,
    QGridLayout,
    QSizePolicy,
)


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
        combo_main = QComboBox()

        combo_main.addItems([
            "Histogram",
            "Line",
            "Scatter",
        ])

        # ---------------- ROW 2 ----------------
        label_a = QLabel("X")
        combo_a = QComboBox()

        label_b = QLabel("Y")
        combo_b = QComboBox()

        # ---------------- ROW 3 ----------------
        label_c = QLabel("Xerr")
        combo_c = QComboBox()

        label_d = QLabel("Yerr")
        combo_d = QComboBox()

        # ---------------- ROW 4 ----------------
        label_e = QLabel("Xerr2")
        combo_e = QComboBox()

        label_f = QLabel("Yerr2")
        combo_f = QComboBox()

        # örnek içerik
        for combo in [
            combo_a, combo_b,
            combo_c, combo_d,
            combo_e, combo_f
        ]:
            combo.addItems(["A", "B", "C"])

                        # minimum daralma
            combo.setMinimumWidth(80)

            # sola doğru daralabilsin
            combo.setSizePolicy(
                QSizePolicy.MinimumExpanding,
                QSizePolicy.Fixed
            )


        # minimum sıkışabilir yapı
        all_combos = [
            combo_main,
            combo_a, combo_b,
            combo_c, combo_d,
            combo_e, combo_f
        ]

        for combo in all_combos:
            combo.setSizePolicy(
                QSizePolicy.Expanding,
                QSizePolicy.Fixed
            )

        # ---------------- GRID ----------------

        # row 0
        layout.addWidget(label_main, 0, 0)
        layout.addWidget(combo_main, 0, 1, 1, 3)

        # row 1
        layout.addWidget(label_a, 1, 0)
        layout.addWidget(combo_a, 1, 1)

        layout.addWidget(label_b, 1, 2)
        layout.addWidget(combo_b, 1, 3)

        # row 2
        layout.addWidget(label_c, 2, 0)
        layout.addWidget(combo_c, 2, 1)

        layout.addWidget(label_d, 2, 2)
        layout.addWidget(combo_d, 2, 3)

        # row 3
        layout.addWidget(label_e, 3, 0)
        layout.addWidget(combo_e, 3, 1)

        layout.addWidget(label_f, 3, 2)
        layout.addWidget(combo_f, 3, 3)

        # stretch ayarları
        layout.setColumnStretch(0, 0)
        layout.setColumnStretch(1, 1)

        layout.setColumnStretch(2, 0)
        layout.setColumnStretch(3, 1)

        self.setLayout(layout)