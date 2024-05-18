from PySide6.QtWidgets import (
    QWidget,
    QSizePolicy,
    QTextEdit,
)
from PySide6.QtGui import (
    QFont,
)
from PySide6.QtCore import (
    Qt
)

class TextEditWidget(QTextEdit):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.setMinimumWidth(1)
        self.setMinimumHeight(1)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setFont(QFont(":/fonts/NotoSans.ttf", 10))
        self.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)