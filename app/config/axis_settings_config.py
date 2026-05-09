from app.config.plot_settings_config import (
    SettingField,
    FieldType,
)

AXIS_SETTINGS_CONFIG = [

    SettingField(
        key="title",
        label="Title",
        field_type=FieldType.TEXT,
        default="",
        group="Labels",
    ),

    SettingField(
        key="xlabel",
        label="X Label",
        field_type=FieldType.TEXT,
        default="",
        group="Labels",
    ),

    SettingField(
        key="ylabel",
        label="Y Label",
        field_type=FieldType.TEXT,
        default="",
        group="Labels",
    ),

    SettingField(
        key="xscale",
        label="X Scale",
        field_type=FieldType.COMBO,
        default="linear",
        options=["linear", "log"],
        group="Scale",
    ),

    SettingField(
        key="yscale",
        label="Y Scale",
        field_type=FieldType.COMBO,
        default="linear",
        options=["linear", "log"],
        group="Scale",
    ),

    SettingField(
        key="grid",
        label="Grid",
        field_type=FieldType.BOOL,
        default=False,
        group="Style",
    ),
]