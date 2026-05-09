from app.adapters.base_adapter import BaseAdapter


class ArtistAdapter(BaseAdapter):

    @staticmethod
    def get(artist_item, key):

        return artist_item.settings.get(key)

    @staticmethod
    def set(artist_item, key, value):

        artist_item.settings[key] = value

        if artist_item.obj is not None:
            artist_item.obj.set(**artist_item.settings)