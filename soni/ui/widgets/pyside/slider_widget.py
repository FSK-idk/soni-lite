from PySide6.QtWidgets import (
    QWidget,
    QSizePolicy,
    QSlider,
)
from PySide6.QtCore import (
    Qt
)

class SliderWidget(QSlider):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.setOrientation(Qt.Orientation.Horizontal)
        self.setMinimumWidth(1)
        self.setFixedHeight(20)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)