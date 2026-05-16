import sys
import matplotlib
matplotlib.use("QtAgg")

from PySide6.QtWidgets import QApplication

from app.controller.app_controller import AppController
from app.views.main_window import MainWindow


def main():
    app        = QApplication(sys.argv)
    window     = MainWindow()
    controller = AppController(app, window)

    window.setCentralWidget(controller.home_view)
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()