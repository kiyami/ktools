# app/config/axis_settings_config.py

from app.config.plot_settings_config import (
    SettingField,
    FieldType,
)

AXIS_SETTINGS_CONFIG = [

    # =====================================================
    # TEXTS
    # =====================================================

    SettingField(
        key="title",
        label="Title",
        field_type=FieldType.TEXT,
    ),

    SettingField(
        key="xlabel",
        label="X Label",
        field_type=FieldType.TEXT,
    ),

    SettingField(
        key="ylabel",
        label="Y Label",
        field_type=FieldType.TEXT,
    ),

    # =====================================================
    # SCALE
    # =====================================================

    SettingField(
        key="xscale",
        label="X Scale",
        field_type=FieldType.COMBO,
        default="linear",
        options=["linear", "log"],
    ),

    SettingField(
        key="yscale",
        label="Y Scale",
        field_type=FieldType.COMBO,
        default="linear",
        options=["linear", "log"],
    ),

    # =====================================================
    # GRID
    # =====================================================

    SettingField(
        key="grid",
        label="Grid",
        field_type=FieldType.BOOL,
        default=False,
    ),

    # =====================================================
    # LIMITS
    # =====================================================

    SettingField(
        key="xlim_min",
        label="X Min",
        field_type=FieldType.TEXT,
        default="",
    ),

    SettingField(
        key="xlim_max",
        label="X Max",
        field_type=FieldType.TEXT,
        default="",
    ),

    SettingField(
        key="ylim_min",
        label="Y Min",
        field_type=FieldType.TEXT,
        default="",
    ),

    SettingField(
        key="ylim_max",
        label="Y Max",
        field_type=FieldType.TEXT,
        default="",
    ),

    # =====================================================
    # NUMERICS
    # =====================================================

    SettingField(
        key="numeric_size",
        label="Numeric Size",
        field_type=FieldType.INT,
        default=10,
        min=1,
        max=40,
        step=1,
    ),

]