import numpy as np
import re
from pathlib import Path

from app.models.dataset import Dataset


class DataService:

    def __init__(self):
        self._datasets: list[Dataset] = []

    # ---- write ----
    def add(self, dataset: Dataset):
        self._datasets.append(dataset)

    def remove(self, index: int):
        del self._datasets[index]

    def clear(self):
        self._datasets.clear()

    # ---- read ----
    def get_all(self):
        return self._datasets

    def get(self, index: int):
        return self._datasets[index]
    
    def get_length(self):
        return len(self._datasets)
    
    def get_index(self, dataset: Dataset):
        return self._datasets.index(dataset)

    def get_headers(self, index: int):
        return self._datasets[index].headers

    def get_numeric(self, index: int):
        return self._datasets[index].numeric_data
    
    def get_raw(self, index: int):
        return self._datasets[index].raw_data
    
    def get_error(self, index: int):
        return self._datasets[index].error
    
    # =========================
    # PUBLIC API
    # =========================
    def load(self, path: str):

        filename = Path(path).stem

        try:
            with open(path, "r", encoding="utf-8") as f:
                lines = [line.rstrip("\n") for line in f]

            delimiter = self._detect_delimiter(path, lines)

            raw = self._parse_raw(lines, delimiter)

            if not raw:
                dataset = Dataset(None, None, None, None, "Invalid file")
                return dataset

            headers, data_rows = self._extract_header(raw)

            # numeric sadece data_rows'dan üretilmeli
            numeric = self._to_numeric(data_rows)

            dataset = Dataset(
                label=filename,
                raw_data=data_rows,
                numeric_data=numeric,
                headers=headers,
                error=None
            )

        except Exception as e:
            dataset = Dataset(None, None, None, None, str(e))

        self.add(dataset=dataset)

        return dataset
        
    # =========================
    # PARSING LAYER
    # =========================
    def _parse_raw(self, lines, delimiter):

        # CASE 1: structured formats
        if delimiter is not None:
            import csv
            return list(csv.reader(lines, delimiter=delimiter))

        # CASE 2: whitespace / messy txt
        return [
            self._split_whitespace(line)
            for line in lines
            if line.strip()
        ]

    def _split_whitespace(self, line: str):
        # robust split: multiple spaces + tabs
        return re.split(r"\s+", line.strip())

    # =========================
    # HEADER DETECTION
    # =========================
    def _extract_header(self, raw):

        first = raw[0]

        if self._is_header(first):
            return first, raw[1:]

        headers = [f"Col {i+1}" for i in range(len(first))]
        return headers, raw

    def _is_header(self, row):

        if not row:
            return False

        numeric = 0

        for cell in row:
            try:
                float(cell)
                numeric += 1
            except:
                pass

        # çoğu numeric ise header değildir
        return numeric < len(row) / 2

    # =========================
    # NUMERIC CONVERSION
    # =========================
    def _to_numeric(self, rows):

        if not rows:
            return None

        cleaned = []

        for row in rows:
            cleaned.append([self._safe_float(x) for x in row])

        arr = np.array(cleaned, dtype=float)

        if arr.ndim == 1:
            arr = arr.reshape(-1, 1)

        return arr

    def _safe_float(self, x):
        try:
            return float(x)
        except:
            return np.nan

    # =========================
    # DELIMITER DETECTION
    # =========================
    def _detect_delimiter(self, path, lines):

        # 1. explicit hints
        if path.endswith(".tsv"):
            return "\t"

        # 2. candidate delimiters
        delimiters = [",", ";", "\t", "|"]

        best = None
        best_score = 0

        sample_lines = lines[:10]

        for d in delimiters:
            score = sum(line.count(d) for line in sample_lines)

            if score > best_score:
                best_score = score
                best = d

        # 3. fallback: whitespace
        if best_score == 0:
            return None

        return best
