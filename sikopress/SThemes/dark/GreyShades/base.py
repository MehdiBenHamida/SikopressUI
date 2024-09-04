from dataclasses import dataclass

from sikopress.SThemes.base import SGalleryTheme, SPushButtonTheme, STheme


@dataclass
class SGreyShadesPushButtonTheme(SPushButtonTheme):
    pass


@dataclass
class SGreyShadesGalleryTheme(SGalleryTheme):
    pass


@dataclass
class SGreyShadesTheme(STheme):
    push_button: SPushButtonTheme = SGreyShadesPushButtonTheme
    gallery: SGalleryTheme = SGreyShadesGalleryTheme
