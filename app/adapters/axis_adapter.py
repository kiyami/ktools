from app.adapters.base_adapter import BaseAdapter


class AxisAdapter(BaseAdapter):

    @staticmethod
    def get(ax, key):

        if key == "title":
            return ax.get_title()

        elif key == "xlabel":
            return ax.get_xlabel()

        elif key == "ylabel":
            return ax.get_ylabel()

        return None

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
            ax.grid(value)