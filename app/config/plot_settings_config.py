# app/config/plot_settings_config.py

from dataclasses import dataclass
from typing import Any, Optional, List, Dict

from app.models.plot_model import PlotType


# =========================================================
# FIELD TYPES
# =========================================================

class FieldType:
    TEXT = "text"
    INT = "int"
    FLOAT = "float"
    BOOL = "bool"
    COLOR = "color"
    COMBO = "combo"


# =========================================================
# FIELD SCHEMA
# =========================================================

@dataclass(frozen=True)
class SettingField:

    key: str
    label: str

    field_type: str

    default: Any = None

    options: Optional[List[Any]] = None

    min: Optional[float] = None
    max: Optional[float] = None
    step: Optional[float] = None

    group: str = "General"


# =========================================================
# COMMON FIELDS
# =========================================================

COMMON_FIELDS = [

    SettingField(
        key="label",
        label="Label",
        field_type=FieldType.TEXT,
        default="",
        group="General",
    ),

    SettingField(
        key="alpha",
        label="Opacity",
        field_type=FieldType.FLOAT,
        default=1.0,
        min=0.0,
        max=1.0,
        step=0.1,
        group="Style",
    ),

    SettingField(
        key="color",
        label="Color",
        field_type=FieldType.COLOR,
        default="#4e79a7",
        group="Style",
    ),
]


# =========================================================
# LINE
# =========================================================

LINE_FIELDS = [

    *COMMON_FIELDS,

    SettingField(
        key="linewidth",
        label="Line Width",
        field_type=FieldType.FLOAT,
        default=1.5,
        min=0.1,
        max=20.0,
        step=0.1,
        group="Line",
    ),

    SettingField(
        key="linestyle",
        label="Line Style",
        field_type=FieldType.COMBO,
        default="-",
        options=["-", "--", "-.", ":"],
        group="Line",
    ),

    SettingField(
        key="marker",
        label="Marker",
        field_type=FieldType.COMBO,
        default="",
        options=["", "o", "s", "^", "x", "*"],
        group="Marker",
    ),
]


# =========================================================
# SCATTER
# =========================================================

SCATTER_FIELDS = [

    *COMMON_FIELDS,

    SettingField(
        key="s",
        label="Point Size",
        field_type=FieldType.FLOAT,
        default=30,
        min=1,
        max=500,
        step=1,
        group="Scatter",
    ),

    SettingField(
        key="marker",
        label="Marker",
        field_type=FieldType.COMBO,
        default="o",
        options=["o", "s", "^", "x", "*"],
        group="Marker",
    ),
]


# =========================================================
# HISTOGRAM
# =========================================================

HISTOGRAM_FIELDS = [

    *COMMON_FIELDS,

    SettingField(
        key="bins",
        label="Bins",
        field_type=FieldType.INT,
        default=20,
        min=1,
        max=500,
        group="Histogram",
    ),

    SettingField(
        key="histtype",
        label="Type",
        field_type=FieldType.COMBO,
        default="bar",
        options=["bar", "step", "stepfilled"],
        group="Histogram",
    ),

    SettingField(
        key="edgecolor",
        label="Edge Color",
        field_type=FieldType.COLOR,
        default="#000000",
        group="Style",
    ),
]


# =========================================================
# ERRORBAR
# =========================================================

ERRORBAR_FIELDS = [

    *COMMON_FIELDS,

    SettingField(
        key="elinewidth",
        label="Error Line Width",
        field_type=FieldType.FLOAT,
        default=1.0,
        min=0.1,
        max=20,
        step=0.1,
        group="Errorbar",
    ),

    SettingField(
        key="capsize",
        label="Cap Size",
        field_type=FieldType.FLOAT,
        default=3,
        min=0,
        max=20,
        step=1,
        group="Errorbar",
    ),

    SettingField(
        key="marker",
        label="Marker",
        field_type=FieldType.COMBO,
        default="o",
        options=["o", "s", "^", "x", "*"],
        group="Marker",
    ),
]


# =========================================================
# MAP
# =========================================================

PLOT_SETTINGS_CONFIG: Dict[PlotType, List[SettingField]] = {

    PlotType.LINE: LINE_FIELDS,
    PlotType.SCATTER: SCATTER_FIELDS,
    PlotType.HISTOGRAM: HISTOGRAM_FIELDS,
    PlotType.ERRORBAR: ERRORBAR_FIELDS,
    PlotType.ERRORBAR_ASYM: ERRORBAR_FIELDS,
}