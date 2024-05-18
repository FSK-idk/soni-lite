from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
)
from PySide6.QtCore import (
    Qt,
)

class VBoxLayoutWidget(QVBoxLayout):
    def __init__(self) -> None:
        super().__init__()

        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(2)
        self.setAlignment(Qt.AlignmentFlag.AlignTop)

