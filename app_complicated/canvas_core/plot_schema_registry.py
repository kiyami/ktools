from app.canvas_core.plot_schema import PlotSchema


class PlotSchemaRegistry:

    _schemas = {
        "line": PlotSchema(
            plot_type="line",
            x_cols=1,
            y_cols=1
        ),

        "scatter": PlotSchema(
            plot_type="scatter",
            x_cols=1,
            y_cols=1
        ),

        "hist": PlotSchema(
            plot_type="hist",
            x_cols=1,
            y_cols=0
        ),

        "errorbar": PlotSchema(
            plot_type="errorbar",
            x_cols=1,
            y_cols=1,
            error_mode="symmetric",
            yerr_cols=1
        ),

        "errorbar_asym": PlotSchema(
            plot_type="errorbar_asym",
            x_cols=1,
            y_cols=1,
            error_mode="asymmetric",
            yerr_cols=2
        )
    }

    @classmethod
    def get(cls, plot_type: str) -> PlotSchema:
        return cls._schemas.get(plot_type)