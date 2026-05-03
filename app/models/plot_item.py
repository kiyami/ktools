from dataclasses import dataclass


@dataclass
class PlotItem:
    id: int
    x_idx: int
    y_idx: int
    label: str

    # 🎨 style state (future-proof)
    color: str = "auto"
    linewidth: float = 1.5
    visible: bool = True