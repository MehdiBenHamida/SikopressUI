from dataclasses import dataclass


@dataclass
class SPushButtonTheme:
    style_sheet: str

@dataclass
class SGalleryTheme:
    pass

@dataclass
class STheme:
    push_button: SPushButtonTheme = SPushButtonTheme
    gallery: SGalleryTheme = SGalleryTheme

    isDark: bool = False
    isLight: bool = False
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if "dark" in cls.__module__:
            cls.isDark = True
            cls.isLight = False
        elif "light" in cls.__module__:
            cls.isDark = False
            cls.isLight = True
