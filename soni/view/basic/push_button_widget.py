from PySide6.QtWidgets import QWidget, QSizePolicy, QPushButton
from PySide6.QtGui import QFont


class PushButtonWidget(QPushButton):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.setMinimumWidth(1)
        self.setFixedHeight(20)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.setFont(QFont(":/fonts/NotoSans.ttf", 10))