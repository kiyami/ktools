# app/adapters/axis_adapter.py

import math
from app.adapters.base_adapter import BaseAdapter


class AxisAdapter(BaseAdapter):

    _limits_cache = {}

    # =====================================================
    # PARSER (string -> float safe)
    # =====================================================

    @staticmethod
    def _parse_float(value):

        if value is None:
            return None

        if isinstance(value, (int, float)):
            return float(value)

        try:
            return float(value)  # supports: "1e-7", "-3.2"
        except Exception:
            return None

    # =====================================================
    # FORMAT (UI DISPLAY)
    # =====================================================

    @staticmethod
    def _format(value):

        if value is None:
            return ""

        try:
            v = float(value)

            if v == 0:
                return "0"

            # small or large -> scientific
            if abs(v) < 1e-3 or abs(v) > 1e5:
                return f"{v:.2e}"

            # normal
            return f"{v:g}"

        except Exception:
            return str(value)

    # =====================================================
    # GET
    # =====================================================

    @staticmethod
    def get(ax, key):

        if key == "title":
            return ax.get_title()

        if key == "xlabel":
            return ax.get_xlabel()

        if key == "ylabel":
            return ax.get_ylabel()

        if key == "xscale":
            return ax.get_xscale()

        if key == "yscale":
            return ax.get_yscale()

        if key == "grid":
            return any(
                line.get_visible()
                for line in ax.get_xgridlines()
            )

        if key == "xlim_min":
            return AxisAdapter._format(ax.get_xlim()[0])

        if key == "xlim_max":
            return AxisAdapter._format(ax.get_xlim()[1])

        if key == "ylim_min":
            return AxisAdapter._format(ax.get_ylim()[0])

        if key == "ylim_max":
            return AxisAdapter._format(ax.get_ylim()[1])

        if key == "tick_size":
            return 12

        if key == "numeric_size":
            return 12
        
        if key == "label_size":
            return int(ax.xaxis.label.get_fontsize())

        return None

    # =====================================================
    # SET
    # =====================================================

    @staticmethod
    def set(ax, key, value):

        if key == "title":
            ax.set_title(value)

        elif key == "xlabel":
            ax.set_xlabel(value)

        elif key == "ylabel":
            ax.set_ylabel(value)

        elif key == "xscale":
            ax.set_xscale(value)

        elif key == "yscale":
            ax.set_yscale(value)

        elif key == "grid":
            ax.grid(bool(value))

        # -------------------------
        # LIMITS (string safe)
        # -------------------------

        elif key in ("xlim_min", "xlim_max"):
            AxisAdapter._set_limit(ax, "x", key, value)

        elif key in ("ylim_min", "ylim_max"):
            AxisAdapter._set_limit(ax, "y", key, value)

        # -------------------------
        # TICKS
        # -------------------------
        elif key == "numeric_size":
            try:
                ax.tick_params(axis="both", labelsize=float(value))
            except Exception:
                pass

        elif key == "label_size":

            try:
                size = float(value)

                ax.title.set_fontsize(size)

                ax.xaxis.label.set_fontsize(size)
                ax.yaxis.label.set_fontsize(size)

                legend = ax.get_legend()

                if legend:
                    legend.prop.set_size(size)

            except Exception:
                pass

    # =====================================================
    # LIMIT HANDLER
    # =====================================================

    @staticmethod
    def _set_limit(ax, axis, key, value):

        val = AxisAdapter._parse_float(value)
        if val is None:
            return

        cache_key = f"{id(ax)}_{axis}"

        if cache_key not in AxisAdapter._limits_cache:
            AxisAdapter._limits_cache[cache_key] = [None, None]

        if key.endswith("min"):
            AxisAdapter._limits_cache[cache_key][0] = val
        else:
            AxisAdapter._limits_cache[cache_key][1] = val

        vmin, vmax = AxisAdapter._limits_cache[cache_key]

        if vmin is not None and vmax is not None:

            if axis == "x":
                ax.set_xlim(vmin, vmax)
            else:
                ax.set_ylim(vmin, vmax)