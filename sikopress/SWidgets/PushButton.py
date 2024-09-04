from sikopress.SThemes import STheme
from PySide6.QtWidgets import QPushButton


class SPushButton(QPushButton):
    def __init__(self, theme: STheme, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.theme = theme
        self.setStyleSheet(self.theme.push_button.style_sheet)

