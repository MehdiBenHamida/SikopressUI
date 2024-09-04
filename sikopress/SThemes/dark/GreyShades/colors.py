from dataclasses import dataclass

from sikopress.SThemes.colors import SColors


@dataclass
class SGreyShadesColors(SColors):
    primary: str = "#000000"
    secondary: str = "#000000"
    info: str = "#000000"
    success: str = "#000000"
    warning: str = "#000000"
    danger: str = "#000000"
    light: str = "#000000"
    dark: str = "#000000"
