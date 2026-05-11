from enum import Enum
from dataclasses import dataclass
from pathlib import Path

from PySide6.QtWidgets import QApplication

from app.utils.resource_utils import resource_path


# ── Paths ────────────────────────────────────────────────
# resource_path() resolves against sys._MEIPASS when running
# as a PyInstaller bundle, and against the project root otherwise.
def _qss(filename: str) -> Path:
    return Path(resource_path(f"app/views/styles/themes/{filename}"))


# ── Theme enum ───────────────────────────────────────────
class Theme(Enum):
    LIGHT = "light"
    DARK  = "dark"


# ── Per-theme metadata ───────────────────────────────────
@dataclass(frozen=True)
class ThemeConfig:
    qss_path: Path
    label: str 


THEME_CONFIGS: dict[Theme, ThemeConfig] = {
    Theme.LIGHT: ThemeConfig(
        qss_path=_qss("light.qss"),
        label="Light ☀️",
    ),
    Theme.DARK: ThemeConfig(
        qss_path=_qss("dark.qss"),
        label="Dark 🌙",
    ),
}


# ── Manager ──────────────────────────────────────────────
class ThemeManager:

    _DEFAULT = Theme.LIGHT

    def __init__(self, app: QApplication):
        self._app = app
        self._current = self._DEFAULT
        self.apply(self._DEFAULT)

    # ── public ───────────────────────────────────────────

    def apply(self, theme: Theme) -> bool:
        """Load and apply the QSS for *theme*. Returns True on success."""
        config = THEME_CONFIGS[theme]

        if not config.qss_path.exists():
            print(f"[ThemeManager] QSS not found: {config.qss_path}")
            return False

        try:
            qss = config.qss_path.read_text(encoding="utf-8")
        except OSError as e:
            print(f"[ThemeManager] Could not read QSS: {e}")
            return False

        self._app.setStyleSheet(qss)
        self._current = theme
        return True

    def toggle(self) -> Theme:
        """Switch to the other theme and return the new one."""
        next_theme = Theme.DARK if self._current == Theme.LIGHT else Theme.LIGHT
        self.apply(next_theme)
        return next_theme

    @property
    def current(self) -> Theme:
        return self._current

    @property
    def config(self) -> ThemeConfig:
        return THEME_CONFIGS[self._current]