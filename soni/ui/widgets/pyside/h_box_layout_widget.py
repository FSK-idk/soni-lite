from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
)
from PySide6.QtCore import (
    Qt,
)

class HBoxLayoutWidget(QHBoxLayout):
    def __init__(self, parent: QWidget | None = None) -> None:
        if parent:
            super().__init__(parent)
        else:
            super().__init__()

        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(2)

