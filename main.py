import sys
from PySide2.QtWidgets import QApplication
from ui.main_window import MainWindow

import matplotlib
matplotlib.use("Qt5Agg")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())