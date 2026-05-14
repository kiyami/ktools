import pandas as pd


class DatasetFactory:
    """
    Testlerde kullanılacak hazır DataFrame üreticisi.
    """

    @staticmethod
    def simple():
        return pd.DataFrame({
            "x": [1, 2, 3],
            "y": [4, 5, 6]
        })

    @staticmethod
    def missing_values():
        return pd.DataFrame({
            "a": [1, None, 3],
            "b": [None, 5, 6]
        })

    @staticmethod
    def mixed_types():
        return pd.DataFrame({
            "a": [1, "x", 3],
            "b": ["a", "b", "c"]
        })

    @staticmethod
    def empty():
        return pd.DataFrame()

    @staticmethod
    def wide_dataset():
        return pd.DataFrame({
            f"col_{i}": range(5)
            for i in range(10)
        })