import sys
import matplotlib
matplotlib.use("QtAgg")

from PySide6.QtWidgets import QApplication

from app.controller.app_controller import AppController
from app.main_window import MainWindow

from pathlib import Path


def load_theme(app, theme):
    base_path = Path(__file__).resolve().parent
    qss_path = base_path / "app" / "views" / "styles" / "themes" / f"{theme}.qss"

    with open(qss_path, "r", encoding="utf-8") as f:
        app.setStyleSheet(f.read())


def main():
    app = QApplication(sys.argv)

    controller = AppController()
    view = controller.start()

    load_theme(app, "main")

    window = MainWindow()
    window.setCentralWidget(view)

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()