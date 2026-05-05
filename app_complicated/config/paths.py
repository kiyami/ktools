from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

APP_DIR = BASE_DIR / "app"
THEMES_DIR = APP_DIR / "views" / "styles" / "themes"