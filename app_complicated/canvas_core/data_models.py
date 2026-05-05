from dataclasses import dataclass
from typing import List, Optional


# LINE / SCATTER
@dataclass
class XYData:
    x: List[float]
    y: List[float]


# HISTOGRAM
@dataclass
class HistData:
    values: List[float]


# ERRORBAR
@dataclass
class ErrorBarData:
    x: List[float]
    y: List[float]

    yerr: Optional[object] = None
    xerr: Optional[object] = None