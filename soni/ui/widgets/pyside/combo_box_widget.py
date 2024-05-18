from PySide6.QtWidgets import QWidget, QSizePolicy, QComboBox
from PySide6.QtGui import QFont, QWheelEvent
from PySide6.QtCore import Qt

class ComboBoxWidget(QComboBox):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.setMinimumWidth(1)
        self.setFixedHeight(20)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.setFont(QFont(":/fonts/NotoSans.ttf", 10))
        self.setMaxVisibleItems(5)
        self.view().setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.view().setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

    def wheelEvent(self, event: QWheelEvent):
        event.ignore()