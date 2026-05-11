class BaseAdapter:

    @staticmethod
    def get(target, key):
        raise NotImplementedError

    @staticmethod
    def set(target, key, value):
        raise NotImplementedError