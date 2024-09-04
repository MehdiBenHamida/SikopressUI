from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from PySide6.QtWidgets import QWidget

if TYPE_CHECKING:
    from sikopress.SThemes import STheme


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

    def addItem(self, item: SGalleryItem) -> None:
        """Add a gallery item to the gallery."""
        self.items.append(item)

    def addItems(self, items: list[SGalleryItem]) -> None:
        """Add a list of gallery items to the gallery."""
        self.items.extend(items)
