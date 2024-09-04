from PySide6.QtWidgets import QWidget
from sikopress.SThemes import STheme
from dataclasses import dataclass

@dataclass
class SGalleryItem:
    id: int
    title: str
    description: str | None
    image: str



class SGallery(QWidget):

    def __init__(self, theme: STheme, items: list[SGalleryItem], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.theme = theme
        self.items = items

    def addItem(self, item: SGalleryItem):
        self.items.append(item)

    def addItems(self, items: list[SGalleryItem]):
        self.items.extend(items)

