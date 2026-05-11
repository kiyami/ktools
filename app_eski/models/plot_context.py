from dataclasses import dataclass, field
from typing import Optional, List

from matplotlib.figure import Figure
from matplotlib.axes import Axes

from app.models.plot_model import ArtistItem


@dataclass
class PlotContext:

    figure: Optional[Figure] = None

    axes: Optional[Axes] = None

    artists: List[ArtistItem] = field(default_factory=list)