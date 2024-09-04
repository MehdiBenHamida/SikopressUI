from sikopress.SThemes.base import *

@dataclass
class SWhiteShadesPushButtonTheme(SPushButtonTheme):
    pass

@dataclass
class SWhiteShadesGalleryTheme(SGalleryTheme):
    pass

@dataclass
class SWhiteShadesTheme(STheme):
    push_button: SPushButtonTheme = SWhiteShadesPushButtonTheme
    gallery: SGalleryTheme = SWhiteShadesGalleryTheme