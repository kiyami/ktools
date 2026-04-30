from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QAction

from app.viewmodels.data_viewmodel import DataViewModel
from app.views.home_view import HomeView


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("MVVM App")

        # 🔥 IMPORTANT
        self.menuBar().setNativeMenuBar(False)

        # VM
        self.vm = DataViewModel()

        # VIEW
        self.home = HomeView(self.vm)
        self.setCentralWidget(self.home)

        # MENU
        file_menu = self.menuBar().addMenu("File")

        load_action = QAction("Load sample", self)
        load_action.triggered.connect(self.load_data)

        file_menu.addAction(load_action)

    def load_data(self):
        self.vm.load_file("./data/sample_1.txt")