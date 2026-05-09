from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, Dict, Any, Sequence
from matplotlib.artist import Artist

# =========================================================
# ENUM
# =========================================================

class PlotType(Enum):

    LINE = "line"
    SCATTER = "scatter"
    HISTOGRAM = "histogram"
    ERRORBAR = "errorbar"
    ERRORBAR_ASYM = "errorbar_asym"


# =========================================================
# ARTIST
# =========================================================

@dataclass
class ArtistItem:

    plot_type: Optional[PlotType] = None
    label: Optional[str] = None
    obj: Optional[Artist] = None
    misc: Optional[object] = None
    settings: Dict = field(default_factory=dict)

    def remove(self):
        self.obj.remove()
    
# =========================================================
# BASE
# =========================================================

@dataclass
class PlotItem:

    plot_type: PlotType

    settings: Dict[str, Any] = field(default_factory=dict)

    # -----------------------------------------------------
    # VALIDATION
    # -----------------------------------------------------

    def is_valid(self) -> bool:
        return True

    # -----------------------------------------------------
    # SERIALIZE
    # -----------------------------------------------------

    def to_dict(self) -> Dict:

        return {
            "plot_type": self.plot_type.value,
            "settings": self.settings,
        }


# =========================================================
# LINE
# =========================================================

@dataclass
class LinePlotItem(PlotItem):

    x: Optional[Sequence[float]] = None
    y: Optional[Sequence[float]] = None

    def __init__(
        self,
        x,
        y,
        settings={},
    ):

        super().__init__(
            plot_type=PlotType.LINE,
            settings=settings or {},
        )

        self.x = x
        self.y = y

    def is_valid(self):

        return (
            self.x is not None and
            self.y is not None
        )

    def to_dict(self):

        data = super().to_dict()

        data.update({
            "x": self.x,
            "y": self.y,
        })

        return data


# =========================================================
# SCATTER
# =========================================================

@dataclass
class ScatterPlotItem(PlotItem):

    x: Optional[Sequence[float]] = None
    y: Optional[Sequence[float]] = None

    def __init__(
        self,
        x,
        y,
        settings={},
    ):

        super().__init__(
            plot_type=PlotType.SCATTER,
            settings=settings or {},
        )

        self.x = x
        self.y = y

    def is_valid(self):

        return (
            self.x is not None and
            self.y is not None
        )

    def to_dict(self):

        data = super().to_dict()

        data.update({
            "x": self.x,
            "y": self.y,
        })

        return data


# =========================================================
# HISTOGRAM
# =========================================================

@dataclass
class HistogramPlotItem(PlotItem):

    x: Optional[Sequence[float]] = None

    def __init__(
        self,
        x,
        settings={},
    ):

        super().__init__(
            plot_type=PlotType.HISTOGRAM,
            settings=settings or {},
        )

        self.x = x

    def is_valid(self):

        return self.x is not None

    def to_dict(self):

        data = super().to_dict()

        data.update({
            "x": self.x,
        })

        return data


# =========================================================
# ERRORBAR
# =========================================================

@dataclass
class ErrorbarPlotItem(PlotItem):

    x: Optional[Sequence[float]] = None
    y: Optional[Sequence[float]] = None

    xerr: Optional[Sequence[float]] = None
    yerr: Optional[Sequence[float]] = None

    def __init__(
        self,
        x,
        y,
        xerr=None,
        yerr=None,
        settings={},
    ):

        super().__init__(
            plot_type=PlotType.ERRORBAR,
            settings=settings or {},
        )

        self.x = x
        self.y = y

        self.xerr = xerr
        self.yerr = yerr

    def is_valid(self):

        return (
            self.x is not None and
            self.y is not None
        )

    def to_dict(self):

        data = super().to_dict()

        data.update({
            "x": self.x,
            "y": self.y,

            "xerr": self.xerr,
            "yerr": self.yerr,
        })

        return data


# =========================================================
# ASYMMETRIC ERRORBAR
# =========================================================

@dataclass
class AsymErrorbarPlotItem(PlotItem):

    x: Optional[Sequence[float]] = None
    y: Optional[Sequence[float]] = None

    xerr: Optional[Sequence[float]] = None
    yerr: Optional[Sequence[float]] = None

    xerr2: Optional[Sequence[float]] = None
    yerr2: Optional[Sequence[float]] = None

    def __init__(
        self,
        x,
        y,
        xerr=None,
        yerr=None,
        xerr2=None,
        yerr2=None,
        settings=None,
    ):

        super().__init__(
            plot_type=PlotType.ERRORBAR_ASYM,
            settings=settings or {},
        )

        self.x = x
        self.y = y

        self.xerr = xerr
        self.yerr = yerr

        self.xerr2 = xerr2
        self.yerr2 = yerr2

    def is_valid(self):

        return (
            self.x is not None and
            self.y is not None
        )

    def to_dict(self):

        data = super().to_dict()

        data.update({
            "x": self.x,
            "y": self.y,

            "xerr": self.xerr,
            "yerr": self.yerr,

            "xerr2": self.xerr2,
            "yerr2": self.yerr2,
        })

        return data
    

# =========================================================
# PLOT SELECTION
# =========================================================

@dataclass
class PlotSelections:

    plot_type: PlotType

    x: Optional[str]
    y: Optional[str]

    xerr: Optional[str]
    yerr: Optional[str]

    xerr2: Optional[str]
    yerr2: Optional[str]

    settings = Optional[dict]

    def __init__(self):
        self.x = None
        self.y = None

        self.xerr = None
        self.yerr = None

        self.xerr2 = None
        self.yerr2 = None

        self.settings = None

    def get_plot_type(self):
        return self.plot_type
    
    def get_settings(self):
        return self.settings
    
    def add_setting(self, key, value):
        self.settings[key] = value

    def add_settings(self, settings_dict):
        for key,value in settings_dict:
            self.settings[key] = value

    def get_constructor(self):
        if self.plot_type == PlotType.LINE:
            return LinePlotItem
        elif self.plot_type == PlotType.SCATTER:
            return ScatterPlotItem
        elif self.plot_type == PlotType.HISTOGRAM:
            return HistogramPlotItem
        elif self.plot_type == PlotType.ERRORBAR:
            return ErrorbarPlotItem
        elif self.plot_type == PlotType.ERRORBAR_ASYM:
            return AsymErrorbarPlotItem

    def get_headers(self, settings={}):

        if self.plot_type == PlotType.LINE:
            return {
                "x": self.x, 
                "y": self.y,
            }
        
        elif self.plot_type == PlotType.SCATTER:
            return {
                "x": self.x, 
                "y": self.y,
            }
        
        elif self.plot_type == PlotType.HISTOGRAM:
            return {
                "x": self.x, 
            }
        
        elif self.plot_type == PlotType.ERRORBAR:
            return {
                "x": self.x, 
                "y": self.y,
                "xerr": self.xerr, 
                "yerr": self.yerr,
            }
        
        elif self.plot_type == PlotType.ERRORBAR_ASYM:
            return {
                "x": self.x, 
                "y": self.y,
                "xerr": self.xerr, 
                "yerr": self.yerr,
                "xerr2": self.xerr2, 
                "yerr2": self.yerr2,
            }



