from pathlib import Path
from app.config.paths import THEMES_DIR


class ThemeManager:

    LIGHT = "light"
    DARK = "dark"

    LIGHT_TEXT = "Light ☀️"
    DARK_TEXT = "Dark 🌙"

    def __init__(self, app):
        self.app = app
        self.current = self.LIGHT

    def apply(self, theme_name: str):
        qss_path = THEMES_DIR / f"{theme_name}.qss"

        if not Path(qss_path).exists():
            print(f"[ThemeManager] QSS not found: {qss_path}")
            return

        with open(qss_path, "r", encoding="utf-8") as f:
            self.app.setStyleSheet(f.read())

        self.current = theme_name

    def set_dark_mode(self, enabled: bool):
        self.apply(self.DARK if enabled else self.LIGHT)