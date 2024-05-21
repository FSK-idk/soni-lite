from PySide6.QtWidgets import (
    QWidget,
    QLabel,
)
from PySide6.QtGui import (
    QResizeEvent,
    QPixmap,
)
from PySide6.QtCore import (
    Qt,
)

from ui.widgets.pyside.v_box_layout_widget import VBoxLayoutWidget

import res.resources_rc


class IllustrationWidget(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        # attributes

        self.fullness = 0.8
        self.pixmap = QPixmap(":/images/icon.png")

        # widgets

        self.illustration = QLabel(self)
        self.illustration.setAlignment(Qt.AlignmentFlag.AlignCenter)
        size = int(min(self.width(), self.height()) * self.fullness)
        self.illustration.setPixmap(self.pixmap.scaled(size, size))

        # layout

        self.main_layout = VBoxLayoutWidget()
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.illustration)

        self.setLayout(self.main_layout)

        # self
        
        self.setMinimumSize(40, 40)

    def resizeEvent(self, event: QResizeEvent) -> None:
        size = int(min(self.width(), self.height()) * self.fullness)
        self.illustration.setPixmap(self.pixmap.scaled(size, size))

    def setFullness(self, fullness: int) -> None:
        self.fullness = fullness
    
    def setIllustration(self, pixmap: QPixmap) -> None:
        self.pixmap = pixmap
        size = int(min(self.width(), self.height()) * self.fullness)
        self.illustration.setPixmap(self.pixmap.scaled(size, size))