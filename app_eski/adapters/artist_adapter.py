# from app.adapters.base_adapter import BaseAdapter


# class ArtistAdapter(BaseAdapter):

#     @staticmethod
#     def get(artist_item, key):

#         return artist_item.settings.get(key)

#     @staticmethod
#     def set(artist_item, key, value):

#         artist_item.settings[key] = value

#         if artist_item.obj is not None:
#             artist_item.obj.set(**artist_item.settings)

from app.adapters.base_adapter import BaseAdapter
from matplotlib.collections import PathCollection


class ArtistAdapter(BaseAdapter):

    @staticmethod
    def get(artist_item, key):
        return artist_item.settings.get(key)

    @staticmethod
    def set(artist_item, key, value):

        artist_item.settings[key] = value

        obj = artist_item.obj

        if obj is None:
            return

        settings = artist_item.settings.copy()

        # ==========================================
        # SCATTER SPECIAL HANDLING
        # ==========================================

        if isinstance(obj, PathCollection):

            # size
            if "s" in settings:
                size = settings.pop("s")
                obj.set_sizes([size])

            # color
            if "color" in settings:
                color = settings.pop("color")
                obj.set_facecolor(color)

            # marker unsupported
            if "marker" in settings:
                settings.pop("marker")

        # ==========================================
        # GENERIC
        # ==========================================

        if settings:
            obj.set(**settings)