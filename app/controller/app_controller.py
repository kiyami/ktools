from app.services.theme_manager import ThemeManager
from app.views.home_view import HomeView
from app.viewmodels.home_viewmodel import HomeViewModel


class AppController:

    def __init__(self, app, window):
        self.app    = app
        self.window = window
        self.theme  = ThemeManager(app)

        self.home_view = HomeView()
        self.home_vm   = HomeViewModel(home_view=self.home_view)

        self._bind()

        self.window.set_theme_label(self.theme.config.label)

    # ── Binding ──────────────────────────────────────────

    def _bind(self):
        self.window.open_requested.connect(self.home_vm.data_panel_vm.load_data)
        self.window.save_requested.connect(self._on_save)
        self.window.theme_toggled.connect(self._on_theme_toggled)

    # ── Slots ────────────────────────────────────────────

    def _on_theme_toggled(self):
        self.theme.toggle()
        self.window.set_theme_label(self.theme.config.label)

    def _on_save(self):
        pass
