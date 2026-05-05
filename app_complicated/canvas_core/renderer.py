class CanvasRenderer:

    def __init__(self, ax, store):
        self.ax = ax
        self.store = store

    def render(self, state):

        self.ax.clear()

        for plot in state.plots:

            if not plot.visible:
                continue

            result = self.store.get(plot.data_id)
            if result is None or result.numeric_data is None:
                continue

            data = result.numeric_data

            # -----------------------
            # BASIC XY
            # -----------------------
            x = data[:, plot.x_col] if plot.x_col is not None else None
            y = data[:, plot.y_col] if plot.y_col is not None else None

            # -----------------------
            # LINE
            # -----------------------
            if plot.plot_type == "line":
                self.ax.plot(x, y, label=plot.label)

            # -----------------------
            # SCATTER
            # -----------------------
            elif plot.plot_type == "scatter":
                self.ax.scatter(x, y, label=plot.label)

            # -----------------------
            # HIST
            # -----------------------
            elif plot.plot_type == "hist":
                self.ax.hist(x, label=plot.label)

            # -----------------------
            # ERRORBAR SYMMETRIC
            # -----------------------
            elif plot.plot_type == "errorbar_sym":

                yerr = None
                xerr = None

                if plot.yerr_cols:
                    col = plot.yerr_cols[0]
                    if col is not None:
                        yerr = data[:, col]

                if plot.xerr_cols:
                    col = plot.xerr_cols[0]
                    if col is not None:
                        xerr = data[:, col]

                self.ax.errorbar(
                    x,
                    y,
                    yerr=yerr,
                    xerr=xerr,
                    fmt='o',
                    label=plot.label
                )

            # -----------------------
            # ERRORBAR ASYMMETRIC
            # -----------------------
            elif plot.plot_type == "errorbar_asym":

                yerr = None
                xerr = None

                if plot.yerr_cols and len(plot.yerr_cols) == 2:
                    low, high = plot.yerr_cols
                    if low is not None and high is not None:
                        yerr = [data[:, low], data[:, high]]

                if plot.xerr_cols and len(plot.xerr_cols) == 2:
                    low, high = plot.xerr_cols
                    if low is not None and high is not None:
                        xerr = [data[:, low], data[:, high]]

                self.ax.errorbar(
                    x,
                    y,
                    yerr=yerr,
                    xerr=xerr,
                    fmt='o',
                    label=plot.label
                )

        self.ax.legend()