from app.config.paths import THEMES_DIR


class ThemeManager:

    def __init__(self, app):
        self.app = app
        self.current = "light"

    def apply(self, theme_name: str):

        qss_path = THEMES_DIR / f"{theme_name}.qss"

        with open(qss_path, "r", encoding="utf-8") as f:
            self.app.setStyleSheet(f.read())

        self.current = theme_name

    def toggle(self):
        if self.current == "light":
            self.apply("dark")
        else:
            self.apply("light")