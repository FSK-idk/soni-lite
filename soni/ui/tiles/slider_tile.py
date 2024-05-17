from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QSizePolicy,
    QSlider,
)
from PySide6.QtGui import (
    QFont
)
from PySide6.QtCore import (
    Qt,
    Signal,
)

# TODO: add functionality
class SliderTile(QWidget):
    # signals

    valueChanged = Signal(str)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        # widgets

        self.title = QLabel(self)
        self.title.setMinimumWidth(1)
        self.title.setFixedHeight(20)
        self.title.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.title.setFont(QFont(":/fonts/NotoSans.ttf",12))

        self.slider = QSlider(Qt.Orientation.Horizontal, self)
        self.slider.setMinimumWidth(1)
        self.slider.setFixedHeight(25)
        self.slider.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.slider.setFont(QFont(":/fonts/NotoSans.ttf",12))
        self.slider.setMaximum(10)
        self.slider.valueChanged.connect(self.valueChanged.emit)

        # layout

        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(5)

        self.main_layout.addWidget(self.title)
        self.main_layout.addWidget(self.slider)

        self.setLayout(self.main_layout)

        # geometry

        self.setMaximumHeight(self.main_layout.minimumSize().height())
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

    def setTitle(self, text : str) -> None:
        self.title.setText(text)

    def value(self) -> int:
        return self.slider.value()