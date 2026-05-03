from dataclasses import dataclass
import numpy as np


@dataclass
class LoadResult:
    raw_data: list[list[str]] | None
    numeric_data: np.ndarray | None
    headers: list[str] | None
    error: str | None = None