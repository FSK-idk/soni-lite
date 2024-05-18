from PySide6.QtWidgets import (
    QWidget,
    QSizePolicy,
    QLineEdit,
)
from PySide6.QtGui import (
    QFont,
)

class LineEditWidget(QLineEdit):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.setMinimumWidth(1)
        self.setFixedHeight(20)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.setFont(QFont(":/fonts/NotoSans.ttf", 10))