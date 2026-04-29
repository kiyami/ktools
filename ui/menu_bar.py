from PySide2.QtWidgets import QMenuBar


def create_menu_bar(window):
    menubar = window.menuBar()

    # FILE
    file_menu = menubar.addMenu("File")
    file_menu.addAction("Open")
    file_menu.addAction("Save")
    file_menu.addAction("Export PNG")

    # ANALYSIS
    analysis_menu = menubar.addMenu("Analysis")
    analysis_menu.addAction("Fit Gaussian")
    analysis_menu.addAction("Find Peaks")

    # VIEW
    view_menu = menubar.addMenu("View")
    view_menu.addAction("Clear Plot")