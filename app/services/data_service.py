from pathlib import Path
import pandas as pd

from app.models.dataset import Dataset


class DataService:

    def __init__(self):
        self._datasets: dict[str, Dataset] = {}
        self._order: list[str] = []

    # =========================
    # COLLECTION
    # =========================

    def add(self, dataset: Dataset) -> str:
        """
        Dataset ekler ve key olarak label kullanır.
        Label çakışırsa otomatik suffix ekler.
        """

        key = dataset.label

        # duplicate handling
        if key in self._datasets:
            i = 1
            new_key = f"{key}_{i}"

            while new_key in self._datasets:
                i += 1
                new_key = f"{key}_{i}"

            key = new_key
            dataset.label = key  # label sync

        self._datasets[key] = dataset
        self._order.append(key)

        return key

    def remove(self, key: str) -> None:
        """
        Dataset siler (dict + order sync)
        """

        if key in self._datasets:
            del self._datasets[key]

        if key in self._order:
            self._order.remove(key)

    def clear(self) -> None:
        self._datasets.clear()
        self._order.clear()

    # =========================
    # ACCESS
    # =========================

    def get(self, key: str) -> Dataset:
        return self._datasets[key]

    def get_by_index(self, index: int) -> Dataset:
        key = self._order[index]
        return self._datasets[key]

    def get_all(self) -> list[Dataset]:
        return [self._datasets[k] for k in self._order]

    def keys(self) -> list[str]:
        return self._order.copy()

    def count(self) -> int:
        return len(self._datasets)

    # =========================
    # LOAD
    # =========================

    def load(
        self,
        path: str,
        *,
        delimiter: str | None = None,
        encoding: str = "utf-8"
    ) -> Dataset:

        file_path = Path(path)

        try:
            df = pd.read_csv(
                file_path,
                sep=delimiter,
                encoding=encoding,
                engine="python"
            )

            if df is None or df.empty:
                raise ValueError(f"Failed to load dataset: {file_path}")

            dataset = Dataset(
                label=file_path.stem,
                dataframe=df,
                path=file_path,
                metadata={
                    "delimiter": delimiter,
                    "encoding": encoding,
                    "source": file_path.suffix
                }
            )

        except Exception as e:
            dataset = Dataset(
                label=file_path.stem,
                dataframe=pd.DataFrame(),
                path=file_path,
                error=str(e),
                metadata={"status": "failed"}
            )

        self.add(dataset)
        return dataset

    # =========================
    # UTILITIES
    # =========================

    def save_csv(self, key: str, path: str) -> None:
        self._datasets[key].dataframe.to_csv(path, index=False)

    # =========================
    # DEBUG / DEBUGGING UI
    # =========================

    def debug_state(self) -> dict:
        return {
            "count": len(self._datasets),
            "order": self._order,
            "keys": list(self._datasets.keys())
        }