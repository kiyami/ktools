from PySide6.QtWidgets import QMainWindow, QWidget


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("MVVM App")
        self.menuBar().setNativeMenuBar(False)

        # sadece boş shell
        self.setCentralWidget(QWidget())