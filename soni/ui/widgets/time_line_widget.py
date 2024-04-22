from PySide6.QtWidgets import (
    QWidget,
)
from PySide6.QtGui import (
    QPalette,
)
from PySide6.QtCore import (
    Qt,
)

# TODO: add functionality
class TimeLineWidget(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        
        self.setMinimumSize(30, 30)

        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, Qt.GlobalColor.green)

        self.setAutoFillBackground(True)
        self.setPalette(palette)
