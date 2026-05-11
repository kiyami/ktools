from pathlib import Path
import sys


def resource_path(relative_path: str) -> Path:
    """PyInstaller uyumlu absolute path döndürür."""
    if hasattr(sys, "_MEIPASS"):
        base_path = Path(sys._MEIPASS)
    else:
        base_path = Path(__file__).resolve().parent

    return base_path / relative_path


THEMES_PATH = resource_path("../../app/views/styles/themes")

LIGTH_THEME_PATH = resource_path("../../app/views/styles/themes/light.qss")
DARK_THEME_PATH  = resource_path("../../app/wievs/styles/themes/dark.qss")
