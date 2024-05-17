from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QSizePolicy,
)
from PySide6.QtGui import (
    QFont,
)
from PySide6.QtCore import (
    Signal,
)

# TODO: add functionality
class LineEditTile(QWidget):
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

        self.line_edit = QLineEdit(self)
        self.line_edit.setMinimumWidth(1)
        self.line_edit.setFixedHeight(25)
        self.line_edit.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.line_edit.setFont(QFont(":/fonts/NotoSans.ttf",12))
        self.line_edit.textChanged.connect(self.textChanged.emit)

        # layout

        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(5)

        self.main_layout.addWidget(self.title)
        self.main_layout.addWidget(self.line_edit)

        self.setLayout(self.main_layout)

        # geometry

        self.setMaximumHeight(self.main_layout.minimumSize().height())
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

    def setTitle(self, text: str) -> None:
        self.title.setText(text)

    def text(self) -> str:
        return self.line_edit.text()