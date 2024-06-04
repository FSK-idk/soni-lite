from PySide6.QtGui import QMouseEvent
from PySide6.QtCore import Signal

from view.basic.label_widget import LabelWidget


class PushLabelWidget(LabelWidget):
    clicked = Signal()

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        if self.rect().contains(event.pos()):
            self.clicked.emit()


