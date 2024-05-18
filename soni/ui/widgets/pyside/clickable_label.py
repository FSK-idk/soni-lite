from PySide6.QtGui import QMouseEvent
from PySide6.QtCore import Signal

from ui.widgets.pyside.label_widget import LabelWidget

class ClickableLabelWidget(LabelWidget):
    clicked = Signal()

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        # do not signal if the mouse is not on the label
        if self.rect().contains(event.pos()):
            self.clicked.emit()


