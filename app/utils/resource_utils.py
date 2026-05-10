import os
import sys


def resource_path(relative_path: str) -> str:
    """
    PyInstaller + normal runtime uyumlu resource resolver
    """

    base_path = getattr(sys, "_MEIPASS", os.path.abspath("."))

    return os.path.join(base_path, relative_path)