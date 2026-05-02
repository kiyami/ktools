import numpy as np
from dataclasses import dataclass


@dataclass
class LoadResult:
    data: np.ndarray | None
    headers: list[str] | None
    error: str | None = None