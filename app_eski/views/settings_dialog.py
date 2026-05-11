# app/views/settings_dialog.py

from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QScrollArea,
    QWidget,
    QGroupBox,
)

from app.views.property_editor_view import PropertyEditorView


class SettingsDialog(QDialog):

    applied = Signal()

    # =====================================================
    # INIT
    # =====================================================

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Settings")

        self.resize(500, 700)

        self.sections = []

        self._build_ui()

    # =====================================================
    # UI
    # =====================================================

    def _build_ui(self):

        # -------------------------------------------------
        # ROOT
        # -------------------------------------------------

        root_layout = QVBoxLayout()

        self.setLayout(root_layout)

        # -------------------------------------------------
        # SCROLL AREA
        # -------------------------------------------------

        self.scroll = QScrollArea()

        self.scroll.setWidgetResizable(True)

        root_layout.addWidget(self.scroll)

        # -------------------------------------------------
        # CONTENT
        # -------------------------------------------------

        self.content = QWidget()

        self.content_layout = QVBoxLayout()

        self.content.setLayout(self.content_layout)

        self.scroll.setWidget(self.content)

    # =====================================================
    # CLEAR
    # =====================================================

    def clear(self):

        self.sections.clear()

        while self.content_layout.count():

            item = self.content_layout.takeAt(0)

            widget = item.widget()

            if widget is not None:
                widget.deleteLater()

    # =====================================================
    # ADD SECTION
    # =====================================================

    def add_section(
        self,
        title,
        target,
        config,
        adapter,
    ):

        # -------------------------------------------------
        # GROUP
        # -------------------------------------------------

        group = QGroupBox(title)

        group_layout = QVBoxLayout()

        group.setLayout(group_layout)

        # -------------------------------------------------
        # EDITOR
        # -------------------------------------------------

        editor = PropertyEditorView()

        editor.load(
            target=target,
            config=config,
            adapter=adapter,
        )

        group_layout.addWidget(editor)

        # -------------------------------------------------
        # SIGNALS
        # -------------------------------------------------

        editor.applied.connect(
            self.applied.emit
        )

        editor.canceled.connect(
            self.close
        )

        # -------------------------------------------------
        # STORE
        # -------------------------------------------------

        self.sections.append(editor)

        # -------------------------------------------------
        # UI
        # -------------------------------------------------

        self.content_layout.addWidget(group)

    # =====================================================
    # SHOW EVENT
    # =====================================================

    def showEvent(self, event):

        super().showEvent(event)

        self.raise_()

        self.activateWindow()