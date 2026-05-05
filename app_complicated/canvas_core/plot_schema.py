from dataclasses import dataclass
from typing import Literal


ErrorMode = Literal["none", "symmetric", "asymmetric"]


@dataclass(frozen=True)
class PlotSchema:
    plot_type: str

    x_cols: int = 1
    y_cols: int = 1

    error_mode: ErrorMode = "none"

    yerr_cols: int = 0
    xerr_cols: int = 0