from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
)


def hbox(
    *widgets,
    spacing=0,
    margins=(0, 0, 0, 0),
    ratios=None
):

    widget = QWidget()
    layout = QHBoxLayout(widget)

    layout.setSpacing(spacing)
    layout.setContentsMargins(*margins)

    if ratios and (len(widgets) == len(ratios)):
        for w,r in zip(widgets,ratios):
            layout.addWidget(w,r)
    else:
        for w in widgets:
            layout.addWidget(w)

    return widget


def vbox(
    *widgets,
    spacing=0,
    margins=(0, 0, 0, 0),
    ratios=None
):

    widget = QWidget()
    layout = QVBoxLayout(widget)

    layout.setSpacing(spacing)
    layout.setContentsMargins(*margins)

    if ratios and (len(widgets) == len(ratios)):
        for w,r in zip(widgets,ratios):
            layout.addWidget(w,r)
    else:
        for w in widgets:
            layout.addWidget(w)

    return widget


def fill_into_layout(
        layout, 
        *widgets,
        spacing=0,
        margins=(0, 0, 0, 0),
    ):

    for w in widgets:

        if isinstance(w, QWidget):
            layout.addWidget(w)

        else:
            layout.addLayout(w)

    layout.setSpacing(spacing)
    layout.setContentsMargins(*margins)

    return layout