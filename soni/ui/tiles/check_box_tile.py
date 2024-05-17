from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QSizePolicy,
    QCheckBox,
)
from PySide6.QtGui import (
    QFont,
)
from PySide6.QtCore import (
    Signal,
)

# TODO: add functionality
class CheckBoxTile(QWidget):
    # signals

    stateChanged = Signal(str)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        # widgets

        self.check_box = QCheckBox(self)
        self.check_box.setMinimumWidth(1)
        self.check_box.setFixedHeight(20)
        self.check_box.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.check_box.setFont(QFont(":/fonts/NotoSans.ttf",12))
        self.check_box.stateChanged.connect(self.stateChanged.emit)

        # layout

        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0,0,0,0)

        self.main_layout.addWidget(self.check_box)

        self.setLayout(self.main_layout)

        # geometry

        self.setMaximumHeight(self.main_layout.minimumSize().height())
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

    def setTitle(self, text : str) -> None:
        self.check_box.setText(text)

    def setChecked(self, checked : bool) -> None:
        self.check_box.setChecked(checked)

    def isChecked(self) -> int:
        return self.check_box.isChecked()