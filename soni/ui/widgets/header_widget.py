from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QSizePolicy,
    QHBoxLayout,
)
from PySide6.QtGui import (
    QPalette,
    QResizeEvent,
)
from PySide6.QtCore import (
    Qt,
    Signal,
)

from ui.widgets.clickable_label import ClickableLabel


class TrackHeaderWidget(QWidget):
    clicked = Signal()

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        
        self.setMinimumSize(100, 30)

        # widgets
        self.header = ClickableLabel("Track name", self)
        self.header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.header.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.header.clicked.connect(self.headerClickedEvent)

        # layout
        self.main_layout = QHBoxLayout()
        self.main_layout.addWidget(self.header)
        
        self.setLayout(self.main_layout)

    def headerClickedEvent(self):
        self.clicked.emit()

    def setName(self, name : str) -> None:
        self.header.setText(name)