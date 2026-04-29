from PySide2.QtWidgets import QToolBar, QAction


def create_tool_bar(window):
    toolbar = QToolBar("Main Toolbar")
    window.addToolBar(toolbar)

    action_plot = QAction("Plot", window)
    action_fit = QAction("Fit", window)
    action_peaks = QAction("Peaks", window)
    action_clear = QAction("Clear", window)

    toolbar.addAction(action_plot)
    toolbar.addAction(action_fit)
    toolbar.addAction(action_peaks)
    toolbar.addAction(action_clear)

    # expose actions (optional but useful)
    window.action_plot = action_plot
    window.action_fit = action_fit
    window.action_peaks = action_peaks
    window.action_clear = action_clear