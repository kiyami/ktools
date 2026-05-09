from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QGridLayout,
    QPushButton,
    QLineEdit,
    QComboBox,
    QDoubleSpinBox,
    QSpinBox,
    QCheckBox,
    QColorDialog,
    QHBoxLayout,
)

from app.models.plot_model import PlotType, ArtistItem

from app.config.plot_settings_config import (
    PLOT_SETTINGS_CONFIG,
    FieldType,
    SettingField,
)


class PlotSettingsView(QWidget):

    applied = Signal(object)
    canceled = Signal()

    # =====================================================
    # INIT
    # =====================================================

    def __init__(self, parent=None):
        super().__init__(parent)

        self.artist_item = None

        self.field_widgets = {}
        self.field_labels = {}

        self._build_ui()

    # =====================================================
    # UI
    # =====================================================

    def _build_ui(self):

        self.layout = QGridLayout()

        row = 0

        # -------------------------------------------------
        # Plot type
        # -------------------------------------------------

        self.combo_type = QComboBox()

        for pt in PlotType:
            self.combo_type.addItem(pt.value, pt)

        self.layout.addWidget(QLabel("Plot Type"), row, 0)
        self.layout.addWidget(self.combo_type, row, 1)

        row += 1

        # -------------------------------------------------
        # Dynamic fields
        # -------------------------------------------------

        self.all_fields = self._collect_fields()

        for field in self.all_fields:

            label = QLabel(field.label)

            widget = self._create_widget(field)

            self.field_labels[field.key] = label
            self.field_widgets[field.key] = widget

            self.layout.addWidget(label, row, 0)
            self.layout.addWidget(widget, row, 1)

            row += 1

        # -------------------------------------------------
        # Buttons
        # -------------------------------------------------

        btn_layout = QHBoxLayout()

        self.apply_btn = QPushButton("Apply")
        self.cancel_btn = QPushButton("Cancel")

        btn_layout.addWidget(self.apply_btn)
        btn_layout.addWidget(self.cancel_btn)

        self.layout.addLayout(btn_layout, row, 0, 1, 2)

        self.setLayout(self.layout)

        # -------------------------------------------------
        # Signals
        # -------------------------------------------------

        self.combo_type.currentIndexChanged.connect(
            self._update_visibility
        )

        self.apply_btn.clicked.connect(self._apply)
        self.cancel_btn.clicked.connect(self._cancel)

    # =====================================================
    # FIELD COLLECTION
    # =====================================================

    def _collect_fields(self):

        fields = {}

        for field_list in PLOT_SETTINGS_CONFIG.values():

            for field in field_list:
                fields[field.key] = field

        return list(fields.values())

    # =====================================================
    # CREATE WIDGET
    # =====================================================

    def _create_widget(self, field: SettingField):

        t = field.field_type

        # -------------------------------------------------
        # TEXT
        # -------------------------------------------------

        if t == FieldType.TEXT:

            w = QLineEdit()

            if field.default is not None:
                w.setText(str(field.default))

            return w

        # -------------------------------------------------
        # FLOAT
        # -------------------------------------------------

        elif t == FieldType.FLOAT:

            w = QDoubleSpinBox()

            w.setDecimals(4)

            if field.min is not None:
                w.setMinimum(field.min)

            if field.max is not None:
                w.setMaximum(field.max)

            if field.step is not None:
                w.setSingleStep(field.step)

            if field.default is not None:
                w.setValue(float(field.default))

            return w

        # -------------------------------------------------
        # INT
        # -------------------------------------------------

        elif t == FieldType.INT:

            w = QSpinBox()

            if field.min is not None:
                w.setMinimum(int(field.min))

            if field.max is not None:
                w.setMaximum(int(field.max))

            if field.default is not None:
                w.setValue(int(field.default))

            return w

        # -------------------------------------------------
        # BOOL
        # -------------------------------------------------

        elif t == FieldType.BOOL:

            w = QCheckBox()

            if field.default is not None:
                w.setChecked(bool(field.default))

            return w

        # -------------------------------------------------
        # COMBO
        # -------------------------------------------------

        elif t == FieldType.COMBO:

            w = QComboBox()

            if field.options:
                for opt in field.options:
                    w.addItem(str(opt), opt)

            if field.default is not None:

                idx = w.findData(field.default)

                if idx >= 0:
                    w.setCurrentIndex(idx)

            return w

        # -------------------------------------------------
        # COLOR
        # -------------------------------------------------

        elif t == FieldType.COLOR:

            w = QPushButton()

            color = field.default or "#ffffff"

            w.setText(color)

            self._set_button_color(w, color)

            w.clicked.connect(
                lambda _, btn=w: self._pick_color(btn)
            )

            return w

        # fallback
        return QLineEdit()

    # =====================================================
    # LOAD
    # =====================================================

    def load(self, artist_item: ArtistItem):

        self.artist_item = artist_item

        # set plot type
        idx = self.combo_type.findData(artist_item.plot_type)

        if idx >= 0:
            self.combo_type.setCurrentIndex(idx)

        settings = artist_item.settings or {}

        # load values
        for field in self.all_fields:

            key = field.key

            if key not in settings:
                continue

            value = settings[key]

            widget = self.field_widgets[key]

            self._set_widget_value(widget, field, value)

        self._update_visibility()

    # =====================================================
    # VISIBILITY
    # =====================================================

    def _update_visibility(self):

        plot_type = self.combo_type.currentData()

        allowed = {
            field.key
            for field in PLOT_SETTINGS_CONFIG.get(plot_type, [])
        }

        for field in self.all_fields:

            visible = field.key in allowed

            self.field_labels[field.key].setVisible(visible)
            self.field_widgets[field.key].setVisible(visible)

    # =====================================================
    # APPLY
    # =====================================================

    def _apply(self):

        if self.artist_item is None:
            return

        self.artist_item.plot_type = self.combo_type.currentData()

        settings = {}

        for field in self.all_fields:

            if not self.field_widgets[field.key].isVisible():
                continue

            settings[field.key] = self._get_widget_value(
                self.field_widgets[field.key],
                field,
            )

        self.artist_item.settings = settings

        self.applied.emit(self.artist_item)

    # =====================================================
    # CANCEL
    # =====================================================

    def _cancel(self):

        self.hide()

        self.canceled.emit()

    # =====================================================
    # GET VALUE
    # =====================================================

    def _get_widget_value(self, widget, field):

        t = field.field_type

        if t == FieldType.TEXT:
            return widget.text()

        elif t == FieldType.FLOAT:
            return widget.value()

        elif t == FieldType.INT:
            return widget.value()

        elif t == FieldType.BOOL:
            return widget.isChecked()

        elif t == FieldType.COMBO:
            return widget.currentData()

        elif t == FieldType.COLOR:
            return widget.text()

        return None

    # =====================================================
    # SET VALUE
    # =====================================================

    def _set_widget_value(self, widget, field, value):

        t = field.field_type

        if value is None:
            return

        if t == FieldType.TEXT:

            widget.setText(str(value))

        elif t == FieldType.FLOAT:

            widget.setValue(float(value))

        elif t == FieldType.INT:

            widget.setValue(int(value))

        elif t == FieldType.BOOL:

            widget.setChecked(bool(value))

        elif t == FieldType.COMBO:

            idx = widget.findData(value)

            if idx >= 0:
                widget.setCurrentIndex(idx)

        elif t == FieldType.COLOR:

            widget.setText(str(value))
            self._set_button_color(widget, str(value))

    # =====================================================
    # COLOR
    # =====================================================

    def _pick_color(self, button):

        color = QColorDialog.getColor()

        if not color.isValid():
            return

        hex_color = color.name()

        button.setText(hex_color)

        self._set_button_color(button, hex_color)

    def _set_button_color(self, button, color):

        button.setStyleSheet(f"""
            QPushButton {{
                background-color: {color};
                border: 1px solid #666;
                min-height: 24px;
            }}
        """)