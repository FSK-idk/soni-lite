from PySide6.QtWidgets import (
    QWidget,
    QSizePolicy,
)
from PySide6.QtCore import (
    Qt,
    Signal,
)

from view.default.clickable_label import ClickableLabelWidget
from view.default.h_box_layout_widget import HBoxLayoutWidget


class TrackHeaderWidget(QWidget):
    clicked = Signal()

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        
        # widgets

        self.header = ClickableLabelWidget(self)
        self.header.setText("Audio Title")
        self.header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.header.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.header.clicked.connect(self.headerClickedEvent)

        # layout

        self.main_layout = HBoxLayoutWidget()
        self.main_layout.addWidget(self.header)
        
        self.setLayout(self.main_layout)

        # self
        
        self.setMinimumSize(100, 30)

    def headerClickedEvent(self) -> None:
        self.clicked.emit()

    def setName(self, name: str) -> None:
        self.header.setText(name)