from pathlib import Path
from enum import Enum
from dataclasses import dataclass

from app.config.paths import THEMES_DIR


class Theme(Enum):
    LIGHT = "light"
    DARK = "dark"


@dataclass
class ThemeConfig:
    qss_path: Path
    text: str


THEMES = {
    Theme.LIGHT: ThemeConfig(
        qss_path=THEMES_DIR / "light.qss",
        text="Light ☀️",
    ),
    Theme.DARK: ThemeConfig(
        qss_path=THEMES_DIR / "dark.qss",
        text="Dark 🌙",
    ),
}

class ThemeManager:

    initial_theme = Theme.LIGHT

    def __init__(self, app):
        self.app = app

        # ✔ FIX: None riskini kaldır
        self.current: Theme = self.initial_theme

        self.apply(self.initial_theme)

    def apply(self, theme: Theme):
        config = THEMES[theme]
        qss_path = config.qss_path

        if not qss_path.exists():
            print(f"[ThemeManager] QSS not found: {qss_path}")
            return

        try:
            with open(qss_path, "r", encoding="utf-8") as f:
                self.app.setStyleSheet(f.read())
        except Exception as e:
            print(f"[ThemeManager] Failed to load theme: {e}")
            return

        self.current = theme

    def get_current(self) -> Theme:
        return self.current

    def get_config(self) -> ThemeConfig:
        return THEMES[self.current]