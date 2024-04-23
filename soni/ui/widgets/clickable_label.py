from PySide6.QtWidgets import (
    QWidget,
    QLabel,
)
from PySide6.QtGui import (
    QMouseEvent,
)
from PySide6.QtCore import (
    Signal
)


class ClickableLabel(QLabel):
    # signals
    clicked = Signal(bool)

    def __init__(self, text: str = "", parent: QWidget | None = None) -> None:
        super().__init__(text, parent)
        self.checked = False
    
    def mouseReleaseEvent(self, event : QMouseEvent) -> None:
        if self.rect().contains(event.pos()):
            self.checked = not self.checked
            self.clicked.emit(self.checked)


