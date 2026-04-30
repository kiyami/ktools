from PySide6.QtWidgets import QMenuBar


def create_menu_bar(window):
    menubar = window.menuBar()

    # FILE
    file_menu = menubar.addMenu("File")
    window.action_open = file_menu.addAction("Open")
    window.action_save = file_menu.addAction("Save")
    window.action_export = file_menu.addAction("Export PNG")

    # ANALYSIS
    analysis_menu = menubar.addMenu("Analysis")
    window.action_fit_menu = analysis_menu.addAction("Fit Gaussian")
    window.action_peaks_menu = analysis_menu.addAction("Find Peaks")

    # VIEW
    view_menu = menubar.addMenu("View")
    window.action_clear_menu = view_menu.addAction("Clear Plot")