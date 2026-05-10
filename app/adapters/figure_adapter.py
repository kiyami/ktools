from app.adapters.base_adapter import BaseAdapter

from matplotlib.colors import to_hex


class FigureAdapter(BaseAdapter):

    @staticmethod
    def get(fig, key):

        if key == "facecolor":
            return to_hex(fig.get_facecolor())

        return None

    @staticmethod
    def set(fig, key, value):

        if key == "facecolor":
            fig.set_facecolor(value)