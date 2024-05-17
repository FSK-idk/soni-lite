from typing import List

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QComboBox,
    QLabel,
    QSizePolicy,
)
from PySide6.QtGui import (
    QFont
)
from PySide6.QtCore import (
    Qt,
    Signal,
)

# TODO: add functionality
class ComboBoxTile(QWidget):
    # signals

    textChanged = Signal(str)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        # widgets

        self.title = QLabel(self)
        self.title.setMinimumWidth(1)
        self.title.setFixedHeight(20)
        self.title.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.title.setFont(QFont(":/fonts/NotoSans.ttf",12))

        self.combo_box = QComboBox(self)
        self.combo_box.setMinimumWidth(1)
        self.combo_box.setFixedHeight(25)
        self.combo_box.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.combo_box.setFont(QFont(":/fonts/NotoSans.ttf",12))
        self.combo_box.setMaxVisibleItems(5)
        self.combo_box.view().setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.combo_box.view().setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.combo_box.currentIndexChanged.connect(self.textChanged.emit)

        # layout

        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(5)

        self.main_layout.addWidget(self.title)
        self.main_layout.addWidget(self.combo_box)

        self.setLayout(self.main_layout)

        # geometry

        self.setMaximumHeight(self.main_layout.minimumSize().height())
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

    def setTitle(self, text: str) -> None:
        self.title.setText(text)

    def addItems(self, items: List[str]) -> None:
        self.combo_box.addItems(items)

    def text(self) -> str:
        return self.combo_box.currentText()