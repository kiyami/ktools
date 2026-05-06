import sys
import matplotlib
matplotlib.use("QtAgg")

from PySide6.QtWidgets import QApplication

from app.controller.app_controller import AppController
from app.services.theme_manager import ThemeManager, Theme
from app.main_window import MainWindow


def main():
    app = QApplication(sys.argv)

    controller = AppController(app)
    view = controller.start()

    window = MainWindow()
    window.setCentralWidget(view)

    controller.bind_main_window(window)

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()