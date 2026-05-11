import sys
import matplotlib
matplotlib.use("QtAgg")

from PySide6.QtWidgets import QApplication

from app.controller.app_controller import AppController
from app.services.theme_manager import ThemeManager, Theme
from app.main_window import MainWindow

# from app.utils.resource_utils import resource_path


# def load_styles(app):

#     light_path = resource_path(
#         "app/views/styles/themes/light.qss"
#     )

#     dark_path = resource_path(
#         "app/views/styles/themes/dark.qss"
#     )

#     with open(light_path, "r", encoding="utf-8") as f:
#         light_qss = f.read()

#     with open(dark_path, "r", encoding="utf-8") as f:
#         dark_qss = f.read()

#     app.setStyleSheet(light_qss)


def main():
    app = QApplication(sys.argv)
    #load_styles(app)

    controller = AppController(app)
    view = controller.start()

    window = MainWindow()
    window.setCentralWidget(view)

    controller.bind_main_window(window)

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()