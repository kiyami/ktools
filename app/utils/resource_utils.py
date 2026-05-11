import sys
from pathlib import Path


# Project root: three levels up from app/utils/resource_utils.py
_PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent


def resource_path(relative_path: str) -> str:
    """
    Resolve a path to a bundled resource.

    - Normal run:         resolves relative to the project root,
                          regardless of the working directory.
    - PyInstaller bundle: resolves relative to sys._MEIPASS, where
                          PyInstaller extracts all bundled data files.
    """
    base = Path(getattr(sys, "_MEIPASS", _PROJECT_ROOT))
    return str(base / relative_path)