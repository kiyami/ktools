from PySide6.QtWidgets import QMainWindow, QToolBar, QToolButton, QWidget, QSizePolicy
from PySide6.QtCore import Signal, QSize
from PySide6.QtGui import QAction


class MainWindow(QMainWindow):

    open_requested  = Signal()
    exit_requested  = Signal()
    save_requested  = Signal()
    theme_toggled   = Signal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("k-Tools")
        self.resize(1000, 700)
        self.setMinimumSize(700, 500)
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

        menubar.addMenu("Edit")
        menubar.addMenu("Settings")
        menubar.addMenu("Help")

    # ---------------- TOOLBAR ----------------
    def _setup_toolbar(self):
        toolbar = QToolBar("Main Toolbar")
        self.addToolBar(toolbar)
        toolbar.setMinimumHeight(30)
        toolbar.setIconSize(QSize(18, 18))

        self.save_btn = QToolButton()
        self.save_btn.setText("Save")
        self.save_btn.setToolTip("Save Figure")
        self.save_btn.clicked.connect(self.save_requested.emit)
        toolbar.addWidget(self.save_btn)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        toolbar.addWidget(spacer)

        self.theme_btn = QToolButton()
        self.theme_btn.setCheckable(True)
        self.theme_btn.setToolTip("Toggle theme")
        self.theme_btn.clicked.connect(self.theme_toggled.emit)
        toolbar.addWidget(self.theme_btn)

    # ---------------- PUBLIC API ----------------
    def set_theme_label(self, text: str):
        self.theme_btn.setText(text)