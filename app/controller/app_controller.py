from app.services.theme_manager import ThemeManager, Theme
from app.views.home_view import HomeView
from app.viewmodels.home_viewmodel import HomeViewModel


class AppController:

    def __init__(self, app):
        self.app = app
        self.theme = ThemeManager(app)

    def _init_views(self):
        self.home_view = HomeView()

    def _init_viewmodels(self):
        self.home_vm = HomeViewModel()

    def _on_theme_toggled(self):
        new_theme = self.theme.toggle()
        self.window.set_theme_label(self.theme.config.label)
 
    def _on_save_requested(self):
        pass  # hook up later

    def _bind(self):
        self.window.theme_toggled.connect(self._on_theme_toggled)
        self.window.save_requested.connect(self._on_save_requested)

    def bind_main_window(self, window):
        self.window = window
        self.window.set_theme_label(self.theme.config.label)
 
        self._bind()

    def start(self):
        self._init_views()
        self._init_viewmodels()

        return self.home_view