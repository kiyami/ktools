import numpy as np
import csv

from app.models.load_result import LoadResult


class DataLoader:

    def load(self, path: str):

        try:
            with open(path, "r", encoding="utf-8") as f:
                lines = f.readlines()

            if not lines:
                return LoadResult(None, None, "Empty file")

            # 🔥 burada delimiter hesaplanır
            delimiter = self._detect_delimiter(path, lines)

            # 🔥 BURASI: parsing stratejisi
            if delimiter is None:
                reader = [line.strip().split() for line in lines]
            else:
                reader = list(csv.reader(lines, delimiter=delimiter))

            if not reader:
                return LoadResult(None, None, "Invalid file")

            first_row = reader[0]

            has_header = self._is_header(first_row)

            if has_header:
                headers = first_row
                data = reader[1:]
            else:
                headers = [f"Col {i+1}" for i in range(len(first_row))]
                data = reader

            if not data:
                return LoadResult(None, None, "No data rows")

            return LoadResult(
                data=np.array(data, dtype=object),
                headers=headers,
                error=None
            )

        except Exception as e:
            return LoadResult(None, None, str(e))
        
    def _detect_delimiter(self, path, lines):

        # 🔵 1. küçük sample al
        sample = "".join(lines[:5])

        # 🔵 2. extension hint
        if path.endswith(".tsv"):
            return "\t"

        if path.endswith(".csv"):
            # csv ama ; veya , olabilir
            pass

        # 🔵 3. içerik analizi (en önemli kısım)
        delimiters = [",", ";", "\t", "|"]

        best_delim = ","
        max_count = 0

        for d in delimiters:
            counts = [line.count(d) for line in lines[:10]]
            avg = sum(counts)

            if avg > max_count:
                max_count = avg
                best_delim = d

        # 🔵 4. fallback (whitespace)
        if max_count == 0:
            return None  # csv.reader whitespace split yapar

        return best_delim
    
    def _is_header(self, row):
        """
        Basit heuristic:
        - Eğer ilk satırda sayısal veri varsa header değildir
        - Eğer string ağırlıklıysa header kabul edilir
        """

        if not row:
            return False

        numeric_score = 0

        for cell in row:
            try:
                float(cell)
                numeric_score += 1
            except:
                pass

        # 🔥 çoğu sayıysa header değil
        return numeric_score < len(row) / 2