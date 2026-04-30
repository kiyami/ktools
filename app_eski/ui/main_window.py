from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QAction

from ui.views.home_view import HomeView

from data_io.data_services import DataService
from data_io.data_controller import DataController


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        service = DataService()
        controller = DataController(service)

        self.setWindowTitle("Component Based App")

        menu_bar = self.menuBar()
        self.menuBar().setNativeMenuBar(False)

        # File menüsü
        file_menu = menu_bar.addMenu("File")

        # Action
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)

        file_menu.addAction(exit_action)

        # View menüsü
        view_menu = menu_bar.addMenu("View")

        toggle_action = QAction("Toggle", self)
        toggle_action.triggered.connect(self.on_toggle)

        view_menu.addAction(toggle_action)

        self.home_view = HomeView(controller)
        self.setCentralWidget(self.home_view)

    def on_toggle(self):
        print("View toggle")