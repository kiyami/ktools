from dataclasses import dataclass
from typing import Optional


@dataclass
class PlotEntity:
    id: int
    data_id: int
    label: str
    plot_type: str

    x_col: int = 0
    y_col: int = 0

    # error columns (optional)
    yerr_cols: Optional[tuple[int, int] | int] = None

    visible: bool = True

    color: Optional[str] = None
    linewidth: float = 1.5