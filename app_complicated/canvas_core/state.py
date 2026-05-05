from dataclasses import dataclass, field
from typing import List
from app.canvas_core.plot_entity import PlotEntity


@dataclass
class CanvasState:
    plots: List[PlotEntity] = field(default_factory=list)