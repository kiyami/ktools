# app/views/property_editor_view.py

from PySide6.QtCore import Signal, Qt
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

    def load(self, target, config, adapter):
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

        for field in self.config:

            label = QLabel(field.label)
            widget = self._create_widget(field)

            value = self.adapter.get(self.target, field.key)

            if value is None:
                value = field.default

            self._set_widget_value(widget, field, value)

            self.field_labels[field.key] = label
            self.field_widgets[field.key] = widget

            self.layout.addWidget(label, row, 0)
            self.layout.addWidget(widget, row, 1)

            row += 1

        # buttons
        btn_layout = QHBoxLayout()

        self.apply_btn = QPushButton("Apply")
        self.cancel_btn = QPushButton("Cancel")

        btn_layout.addWidget(self.apply_btn)
        btn_layout.addWidget(self.cancel_btn)

        self.layout.addLayout(btn_layout, row, 0, 1, 2)

        self.apply_btn.clicked.connect(self._apply)
        self.cancel_btn.clicked.connect(self._cancel)

    # =====================================================
    # CREATE WIDGET
    # =====================================================

    def _create_widget(self, field: SettingField):

        t = field.field_type

        if t == FieldType.TEXT:
            return QLineEdit()

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

        elif t == FieldType.INT:
            w = QSpinBox()

            if field.min is not None:
                w.setMinimum(int(field.min))
            if field.max is not None:
                w.setMaximum(int(field.max))

            return w

        elif t == FieldType.BOOL:
            return QCheckBox()

        elif t == FieldType.COMBO:
            w = QComboBox()

            if field.options:
                for opt in field.options:
                    w.addItem(str(opt), opt)

            return w

        # =====================================================
        # COLOR (NEW STRUCTURE)
        # =====================================================

        elif t == FieldType.COLOR:

            container = QWidget()
            layout = QHBoxLayout()
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(8)

            button = QPushButton()
            button.setFixedWidth(50)
            button.setMinimumHeight(24)

            label = QLabel()
            label.setTextInteractionFlags(Qt.TextSelectableByMouse)
            #label.setStyleSheet("font-family: monospace;")

            button.clicked.connect(
                lambda _, btn=button, lbl=label:
                self._pick_color(btn, lbl)
            )

            layout.addWidget(button)
            layout.addWidget(label)
            layout.addStretch()

            container.setLayout(layout)

            container.button = button
            container.label = label

            return container

        return QLineEdit()

    # =====================================================
    # APPLY
    # =====================================================

    def _apply(self):

        if self.target is None:
            return

        for field in self.config:

            widget = self.field_widgets[field.key]
            value = self._get_widget_value(widget, field)

            self.adapter.set(self.target, field.key, value)

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
            return widget.label.text()

        return None

    # =====================================================
    # SET VALUE
    # =====================================================

    def _set_widget_value(self, widget, field, value):

        if value is None:
            return

        t = field.field_type

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

            widget.label.setText(str(value))
            self._set_button_color(widget.button, widget.label, str(value))

    # =====================================================
    # COLOR PICKER
    # =====================================================

    def _pick_color(self, button, label):

        color = QColorDialog.getColor()
        if not color.isValid():
            return

        hex_color = color.name()

        self._set_button_color(button, label, hex_color)

    # =====================================================
    # COLOR STYLE
    # =====================================================

    def _set_button_color(self, button, label, color):

        button.setStyleSheet(f"""
            QPushButton {{
                background-color: {color};
                border: 1px solid #666;
                min-height: 24px;
            }}
        """)

        label.setText(color)

    # =====================================================
    # CLEAR
    # =====================================================

    def _clear_layout(self):

        while self.layout.count():

            item = self.layout.takeAt(0)

            widget = item.widget()
            if widget:
                widget.deleteLater()

            layout = item.layout()
            if layout:
                while layout.count():
                    sub = layout.takeAt(0)
                    w = sub.widget()
                    if w:
                        w.deleteLater()