from app.views.home_view import HomeView

from app.viewmodels.home_viewmodel import HomeViewModel
from app.viewmodels.table_viewmodel import TableViewModel
from app.viewmodels.canvas_viewmodel import CanvasViewModel
from app.viewmodels.analysis_viewmodel import AnalysisViewModel

from app.services.theme_manager import ThemeManager, Theme
from app.services.data_service import DataService

from app.models.dataset import Dataset


from app.views.settings_dialog import SettingsDialog

from app.adapters.artist_adapter import ArtistAdapter
from app.adapters.axis_adapter import AxisAdapter
from app.adapters.figure_adapter import FigureAdapter

from app.config.plot_settings_config import PLOT_SETTINGS_CONFIG
from app.config.axis_settings_config import AXIS_SETTINGS_CONFIG
from app.config.figure_settings_config import FIGURE_SETTINGS_CONFIG

from PySide6.QtWidgets import QFileDialog


class AppController:

    def __init__(self, app):
        self.app = app
        self.theme = ThemeManager(app)

    def _init_views(self):
        self.home_view = HomeView()

        self.table_view = self.home_view.get_table_view()
        self.canvas_view = self.home_view.get_canvas_view()
        self.analysis_view = self.home_view.get_analysis_view()

        self.settings_dialog = SettingsDialog(parent=self.home_view)

    def _init_viewmodels(self):
        self.data_service = DataService()

        self.home_vm = HomeViewModel()
        self.table_vm = TableViewModel(self.data_service)
        self.canvas_vm = CanvasViewModel(self.data_service)
        self.analysis_vm = AnalysisViewModel(self.data_service)

    def _handle_load_result(self, result: Dataset):
        if result.error:
            self.table_view.show_error(result.error)
        else:
            self.table_view.update_table(result)

    def _bind(self):

        # load data v->vm
        self.table_view.load_data_clicked.connect(
            self.table_vm.open_file_dialog
        )
        # file dropped v->vm
        self.table_view.file_dropped.connect(
            self.table_vm.load_data
        )
        # load data vm->v
        self.table_vm.data_loaded.connect(
            self.table_view.update_table
        )
        self.table_vm.update_visibility.connect(
            self.table_view.set_visibility
        )

        # remove data v->vm
        self.table_view.remove_data_clicked.connect(
            self.table_vm.remove_data
        )
        # remove data vm->v
        self.table_vm.data_removed.connect(
            self.table_view.update_table
        )
        self.table_vm.data_removed.connect(
            self.table_view.set_visibility
        )

        # reset data v->vm
        self.table_view.reset_clicked.connect(
            self.table_vm.reset_table
        )
        # reset data vm->v
        self.table_vm.table_resetted.connect(
            self.table_view.reset_table
        )

        # selected row changed
        self.table_view.selected_row_changed.connect(
            self.table_vm.update_row_and_table
        )

        self.table_vm.update_selected_row.connect(
            self.table_view.set_row
        )

        # set model
        self.table_vm.model_sended.connect(
            self.table_view.set_model
        )

        # message area
        self.home_vm.message_sended.connect(
            self.home_view.append_text
        )
        # log
        self.table_vm.message_sended.connect(
            self.home_vm.log
        )
        self.canvas_vm.message_sended.connect(
            self.home_vm.log
        )
        self.analysis_vm.message_sended.connect(
            self.home_vm.log
        )

        # plot settings
        self.table_vm.headers_sended.connect(
            self.canvas_view.fill_headers
        )
        self.table_vm.table_resetted.connect(
            self.canvas_view.reset
        )
        # plot data request/send
        self.canvas_view.plot_data_requested.connect(
            self.canvas_vm.request_selected_row
        )
        self.canvas_vm.selected_row_requested.connect(
            self.table_vm.send_selected_row
        )
        self.table_vm.selected_row_sended.connect(
            self.canvas_vm.get_plot_data
        )
        self.canvas_vm.plot_data_sended.connect(
            self.canvas_view.plot
        )
        # remove plot
        self.canvas_view.remove_plot_requested.connect(
            self.canvas_vm.remove_artist
        )
        self.canvas_vm.artist_removed.connect(
            self.canvas_view.update_list
        )

        # artist
        self.canvas_view.artist_plotted.connect(
            self.canvas_vm.add_artist
        )
        self.canvas_vm.artist_added.connect(
            self.canvas_view.update_list
        )
        self.canvas_vm.artist_added.connect(
            self.canvas_view.redraw
        )
        self.canvas_vm.artist_removed.connect(
            self.canvas_view.update_list
        )
        self.canvas_vm.artist_removed.connect(
            self.canvas_view.redraw
        )

        self.canvas_view.reset_requested.connect(
            self.canvas_vm.reset
        )
        self.canvas_vm.reset_done.connect(
            self.canvas_view.reset
        )

        # settings
        self.canvas_view.settings_button_clicked.connect(
            self._open_settings_dialog
        )

        self.settings_dialog.applied.connect(
            self.canvas_view.redraw
        )


    # ---------------- WINDOW ----------------
    def bind_main_window(self, window):
        self.window = window
        window.set_theme_manager(self.theme)
        window.open_requested.connect(self.table_vm.open_file_dialog)
        window.exit_requested.connect(window.close)
        window.theme_toggled.connect(self._on_theme_toggled)

        window.save_requested.connect(self._on_save_requested)

    def _on_theme_toggled(self, checked: bool):
        theme = Theme.DARK if checked else Theme.LIGHT
        self.theme.apply(theme)

        # UI sync controller tarafında
        config = self.theme.get_config()
        self.window.theme_btn.setText(config.text)

    def _open_settings_dialog(self):

        if self.settings_dialog.isVisible():
            self.settings_dialog.raise_()
            self.settings_dialog.activateWindow()
            return
        
        canvas = self.canvas_view.canvas
        figure = self.canvas_view.figure
        ax = self.canvas_view.ax

        artist_items = self.canvas_vm.artist_list

        # temizle
        self.settings_dialog.clear()

        # =====================================================
        # FIGURE
        # =====================================================

        self.settings_dialog.add_section(
            title="Figure",
            target=figure,
            config=FIGURE_SETTINGS_CONFIG,
            adapter=FigureAdapter(),
        )

        # =====================================================
        # AXIS
        # =====================================================

        self.settings_dialog.add_section(
            title="Axis",
            target=ax,
            config=AXIS_SETTINGS_CONFIG,
            adapter=AxisAdapter(),
        )

        # =====================================================
        # ARTISTS
        # =====================================================

        for i, artist_item in enumerate(artist_items):

            config = PLOT_SETTINGS_CONFIG.get(
                artist_item.plot_type,
                [],
            )

            self.settings_dialog.add_section(
                title=f"Artist {i+1}",
                target=artist_item,
                config=config,
                adapter=ArtistAdapter(),
            )

        # =====================================================
        # APPLY CALLBACK
        # =====================================================
        
        # self.settings_dialog.applied.connect(
        #     canvas.draw_idle
        # )

        self.settings_dialog.show()

    def _on_save_requested(self):

        file_path, _ = QFileDialog.getSaveFileName(
            self.window,
            "Save Figure",
            "",
            "PNG Files (*.png);;PDF Files (*.pdf);;SVG Files (*.svg)"
        )

        if not file_path:
            return

        self.canvas_view.savefig(file_path, dpi=300)

    def start(self):
        self._init_views()
        self._init_viewmodels()
        self._bind()

        self.table_vm.send_model()
        self.table_view.set_visibility(0)

        return self.home_view