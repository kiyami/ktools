# app/views/property_editor_view.py

from PySide6.QtCore import Signal
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

from app.config.plot_settings_config import (
    FieldType,
    SettingField,
)


class PropertyEditorView(QWidget):

    applied = Signal()
    canceled = Signal()

    # =====================================================
    # INIT
    # =====================================================

    def __init__(self, parent=None):
        super().__init__(parent)

        self.target = None
        self.config = []
        self.adapter = None

        self.field_widgets = {}
        self.field_labels = {}

        self._build_ui()

    # =====================================================
    # UI
    # =====================================================

    def _build_ui(self):

        self.layout = QGridLayout()

        self.setLayout(self.layout)

    # =====================================================
    # LOAD
    # =====================================================

    def load(
        self,
        target,
        config,
        adapter,
    ):

        self.target = target
        self.config = config
        self.adapter = adapter

        self._rebuild()

    # =====================================================
    # REBUILD
    # =====================================================

    def _rebuild(self):

        self._clear_layout()

        self.field_widgets.clear()
        self.field_labels.clear()

        row = 0

        # -------------------------------------------------
        # FIELDS
        # -------------------------------------------------

        for field in self.config:

            label = QLabel(field.label)

            widget = self._create_widget(field)

            # existing value
            value = self.adapter.get(
                self.target,
                field.key,
            )

            # fallback to default
            if value is None:
                value = field.default

            self._set_widget_value(
                widget,
                field,
                value,
            )

            self.field_labels[field.key] = label
            self.field_widgets[field.key] = widget

            self.layout.addWidget(label, row, 0)
            self.layout.addWidget(widget, row, 1)

            row += 1

        # -------------------------------------------------
        # BUTTONS
        # -------------------------------------------------

        btn_layout = QHBoxLayout()

        self.apply_btn = QPushButton("Apply")
        self.cancel_btn = QPushButton("Cancel")

        btn_layout.addWidget(self.apply_btn)
        btn_layout.addWidget(self.cancel_btn)

        self.layout.addLayout(btn_layout, row, 0, 1, 2)

        # -------------------------------------------------
        # SIGNALS
        # -------------------------------------------------

        self.apply_btn.clicked.connect(self._apply)
        self.cancel_btn.clicked.connect(self._cancel)

    # =====================================================
    # CREATE WIDGET
    # =====================================================

    def _create_widget(self, field: SettingField):

        t = field.field_type

        # -------------------------------------------------
        # TEXT
        # -------------------------------------------------

        if t == FieldType.TEXT:

            return QLineEdit()

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

            return w

        # -------------------------------------------------
        # BOOL
        # -------------------------------------------------

        elif t == FieldType.BOOL:

            return QCheckBox()

        # -------------------------------------------------
        # COMBO
        # -------------------------------------------------

        elif t == FieldType.COMBO:

            w = QComboBox()

            if field.options:
                for opt in field.options:
                    w.addItem(str(opt), opt)

            return w

        # -------------------------------------------------
        # COLOR
        # -------------------------------------------------

        elif t == FieldType.COLOR:

            w = QPushButton()

            w.clicked.connect(
                lambda _, btn=w: self._pick_color(btn)
            )

            return w

        # -------------------------------------------------
        # FALLBACK
        # -------------------------------------------------

        return QLineEdit()

    # =====================================================
    # APPLY
    # =====================================================

    def _apply(self):

        if self.target is None:
            return

        for field in self.config:

            widget = self.field_widgets[field.key]

            value = self._get_widget_value(
                widget,
                field,
            )

            self.adapter.set(
                self.target,
                field.key,
                value,
            )

        self.applied.emit()

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

        # -------------------------------------------------
        # TEXT
        # -------------------------------------------------

        if t == FieldType.TEXT:

            return widget.text()

        # -------------------------------------------------
        # FLOAT
        # -------------------------------------------------

        elif t == FieldType.FLOAT:

            return widget.value()

        # -------------------------------------------------
        # INT
        # -------------------------------------------------

        elif t == FieldType.INT:

            return widget.value()

        # -------------------------------------------------
        # BOOL
        # -------------------------------------------------

        elif t == FieldType.BOOL:

            return widget.isChecked()

        # -------------------------------------------------
        # COMBO
        # -------------------------------------------------

        elif t == FieldType.COMBO:

            return widget.currentData()

        # -------------------------------------------------
        # COLOR
        # -------------------------------------------------

        elif t == FieldType.COLOR:

            return widget.text()

        return None

    # =====================================================
    # SET VALUE
    # =====================================================

    def _set_widget_value(
        self,
        widget,
        field,
        value,
    ):

        if value is None:
            return

        t = field.field_type

        # -------------------------------------------------
        # TEXT
        # -------------------------------------------------

        if t == FieldType.TEXT:

            widget.setText(str(value))

        # -------------------------------------------------
        # FLOAT
        # -------------------------------------------------

        elif t == FieldType.FLOAT:

            widget.setValue(float(value))

        # -------------------------------------------------
        # INT
        # -------------------------------------------------

        elif t == FieldType.INT:

            widget.setValue(int(value))

        # -------------------------------------------------
        # BOOL
        # -------------------------------------------------

        elif t == FieldType.BOOL:

            widget.setChecked(bool(value))

        # -------------------------------------------------
        # COMBO
        # -------------------------------------------------

        elif t == FieldType.COMBO:

            idx = widget.findData(value)

            if idx >= 0:
                widget.setCurrentIndex(idx)

        # -------------------------------------------------
        # COLOR
        # -------------------------------------------------

        elif t == FieldType.COLOR:

            widget.setText(str(value))

            self._set_button_color(
                widget,
                str(value),
            )

    # =====================================================
    # COLOR PICKER
    # =====================================================

    def _pick_color(self, button):

        color = QColorDialog.getColor()

        if not color.isValid():
            return

        hex_color = color.name()

        button.setText(hex_color)

        self._set_button_color(
            button,
            hex_color,
        )

    def _set_button_color(
        self,
        button,
        color,
    ):

        button.setStyleSheet(f"""
            QPushButton {{
                background-color: {color};
                border: 1px solid #666;
                min-height: 24px;
            }}
        """)

    # =====================================================
    # CLEAR
    # =====================================================

    def _clear_layout(self):

        while self.layout.count():

            item = self.layout.takeAt(0)

            widget = item.widget()

            if widget is not None:
                widget.deleteLater()

            child_layout = item.layout()

            if child_layout is not None:

                while child_layout.count():

                    child_item = child_layout.takeAt(0)

                    child_widget = child_item.widget()

                    if child_widget is not None:
                        child_widget.deleteLater()