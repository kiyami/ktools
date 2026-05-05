from PySide6.QtWidgets import (
    QMainWindow,
    QToolBar,
    QToolButton,
    QWidget,
    QSizePolicy
)
from PySide6.QtGui import QAction
from PySide6.QtCore import Signal

from app.services.theme_manager import ThemeManager as TM



class MainWindow(QMainWindow):
    # True = dark, False = light
    open_requested = Signal()
    exit_requested = Signal()
    theme_toggled = Signal(bool)

    def __init__(self):
        super().__init__()

        self.setWindowTitle("k-Tools")

        self._setup_menu()
        self._setup_toolbar()

    # ---------------- MENU ----------------
    def _setup_menu(self):
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        file_menu = menubar.addMenu("File")

        open_action = QAction("Open", self)
        exit_action = QAction("Exit", self)

        file_menu.addAction(open_action)
        file_menu.addAction(exit_action)

        open_action.triggered.connect(self.open_requested.emit)
        exit_action.triggered.connect(self.exit_requested.emit)

    # ---------------- TOOLBAR ----------------
    def _setup_toolbar(self):
        toolbar = QToolBar("Main Toolbar")
        self.addToolBar(toolbar)

        # sağa itmek için spacer
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        toolbar.addWidget(spacer)

        # theme toggle
        self.theme_btn = QToolButton()
        self.theme_btn.setText(TM.LIGHT_TEXT)
        self.theme_btn.setCheckable(True)
        self.theme_btn.setToolTip("Toggle theme")

        toolbar.addWidget(self.theme_btn)

        self.theme_btn.toggled.connect(self._on_theme_toggled)

    def _on_theme_toggled(self, checked: bool):
        self.theme_btn.setText(TM.DARK_TEXT if checked else TM.LIGHT_TEXT)
        self.theme_toggled.emit(checked)