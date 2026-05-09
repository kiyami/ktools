from app.config.plot_settings_config import (
    SettingField,
    FieldType,
)

FIGURE_SETTINGS_CONFIG = [

    SettingField(
        key="facecolor",
        label="Background Color",
        field_type=FieldType.COLOR,
        default="#ffffff",
    ),
]