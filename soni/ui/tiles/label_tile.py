from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QSizePolicy,
)
from PySide6.QtGui import (
    QFont
)
from PySide6.QtCore import (
    Qt,
)

# TODO: add functionality
class LabelTile(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        # widgets

        self.title = QLabel(self)
        self.title.setMinimumWidth(1)
        self.title.setFixedHeight(20)
        self.title.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.title.setFont(QFont(":/fonts/NotoSans.ttf",12))

        # layout

        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0,0,0,0)

        self.main_layout.addWidget(self.title)

        self.setLayout(self.main_layout)

        # geometry

        self.setMaximumHeight(self.main_layout.minimumSize().height())
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

    def setTitle(self, text : str) -> None:
        self.title.setText(text)
