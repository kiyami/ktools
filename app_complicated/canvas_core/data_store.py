class DataStore:

    def __init__(self):
        self._data = {}
        self._order = []  # UI list order

    def add(self, result):
        data_id = len(self._order)
        self._data[data_id] = result
        self._order.append(data_id)
        return data_id

    def get(self, data_id):
        return self._data.get(data_id)

    def remove(self, data_id):
        if data_id in self._data:
            del self._data[data_id]
            self._order.remove(data_id)

    def clear(self):
        self._data.clear()
        self._order.clear()

    def list(self):
        return [self._data[i] for i in self._order]

    def count(self):
        return len(self._order)