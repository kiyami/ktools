import sys
import matplotlib
matplotlib.use("QtAgg")

from PySide6.QtWidgets import QApplication

from app.controller.app_controller import AppController
from app.services.theme_manager import ThemeManager
from app.main_window import MainWindow


def main():
    app = QApplication(sys.argv)

    controller = AppController()
    view = controller.start()

    theme = ThemeManager(app)
    controller.set_theme_manager(theme)
    theme.apply("light")

    window = MainWindow()
    window.setCentralWidget(view)

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()