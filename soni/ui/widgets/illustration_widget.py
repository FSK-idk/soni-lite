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
    QSize
)

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
        self.illustration.setPixmap(self.pixmap.scaled(QSize(int(self.height() * self.fullness), int(self.height() * self.fullness))))


    def resizeEvent(self, event : QResizeEvent) -> None:
        self.setMinimumWidth(self.height())
        self.illustration.resize(QSize(self.height(), self.height()))
        self.illustration.setPixmap(self.pixmap.scaled(QSize(int(self.height() * self.fullness), int(self.height() * self.fullness))))

    def setFullness(self, fullness : int) -> None:
        self.fullness = fullness
    
    def setIllustration(self, pixmap : QPixmap) -> None:
        self.pixmap = pixmap
        self.illustration.setPixmap(self.pixmap.scaled(QSize(int(self.height() * self.fullness), int(self.height() * self.fullness))))