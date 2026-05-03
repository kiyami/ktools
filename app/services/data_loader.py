import numpy as np
import csv
import re

from app.models.load_result import LoadResult


class DataLoader:

    # =========================
    # PUBLIC API
    # =========================
    def load(self, path: str):

        try:
            with open(path, "r", encoding="utf-8") as f:
                lines = [line.rstrip("\n") for line in f]

            if not lines:
                return LoadResult(None, None, None, "Empty file")

            delimiter = self._detect_delimiter(path, lines)

            raw = self._parse_raw(lines, delimiter)

            if not raw or len(raw) == 0:
                return LoadResult(None, None, None, "Invalid file")

            headers, data_rows = self._extract_header(raw)

            numeric = self._to_numeric(data_rows)

            return LoadResult(
                raw_data=raw,
                numeric_data=numeric,
                headers=headers,
                error=None
            )

        except Exception as e:
            return LoadResult(None, None, None, str(e))

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
