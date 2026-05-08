from PySide6.QtWidgets import (
    QMainWindow,
    QToolBar,
    QToolButton,
    QWidget,
    QSizePolicy,
)
from PySide6.QtGui import QAction

from PySide6.QtCore import Signal, QSize

from app.services.theme_manager import Theme


class MainWindow(QMainWindow):
    # True = dark, False = light
    open_requested = Signal()
    exit_requested = Signal()
    theme_toggled = Signal(bool)

    def __init__(self):
        super().__init__()

        self.setWindowTitle("k-Tools")
        self.resize(900, 600)
        self.setMinimumSize(600, 400)

        self._setup_menu()
        self._setup_toolbar()

    # ---------------- MENU ----------------
    def _setup_menu(self):
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        menubar.setMinimumHeight(30)

        file_menu = menubar.addMenu("File")

        open_action = QAction("Open", self)
        exit_action = QAction("Exit", self)

        file_menu.addAction(open_action)
        file_menu.addAction(exit_action)

        open_action.triggered.connect(self.open_requested.emit)
        exit_action.triggered.connect(self.exit_requested.emit)


        edit_menu = menubar.addMenu("Edit")
        settings_menu = menubar.addMenu("Settings")
        help_menu = menubar.addMenu("Help")

    # ---------------- TOOLBAR ----------------
    def _setup_toolbar(self):
        toolbar = QToolBar("Main Toolbar")
        self.addToolBar(toolbar)

        toolbar.setMinimumHeight(30)
        toolbar.setIconSize(QSize(18, 18))

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        toolbar.addWidget(spacer)

        self.theme_btn = QToolButton()
        self.theme_btn.setCheckable(True)
        self.theme_btn.setToolTip("Toggle theme")

        toolbar.addWidget(self.theme_btn)

        # ✔ sadece signal emit
        self.theme_btn.toggled.connect(self.theme_toggled.emit)

    def _on_theme_toggled(self, checked: bool):
        theme = Theme.DARK if checked else Theme.LIGHT

        self.theme_manager.apply(theme)

        config = self.theme_manager.get_config()
        self.theme_btn.setText(config.text)

        self.theme_toggled.emit(checked)

    def set_theme_manager(self, theme_manager):
        self.theme_manager = theme_manager

        config = self.theme_manager.get_config()

        self.theme_btn.setText(config.text)

        is_dark = self.theme_manager.get_current() == Theme.DARK
        self.theme_btn.setChecked(is_dark)