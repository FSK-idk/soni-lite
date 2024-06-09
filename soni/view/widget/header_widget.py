from PySide6.QtWidgets import (
    QWidget,
    QSizePolicy,
)
from PySide6.QtCore import Qt, Signal

from etc.audio_data import AudioData

from view.basic.push_label import PushLabelWidget
from view.basic.h_box_layout_widget import HBoxLayoutWidget


class TrackHeaderWidget(QWidget):
    clicked = Signal()

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        
        self.header = PushLabelWidget(self)
        self.header.setText("Audio Title")
        self.header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.header.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.header.clicked.connect(self.headerClickedEvent)

        self.main_layout = HBoxLayoutWidget()
        self.main_layout.addWidget(self.header)
        
        self.setLayout(self.main_layout)

        self.setMinimumSize(100, 30)

    def headerClickedEvent(self) -> None:
        self.clicked.emit()

    def setAudioData(self, audio_data: AudioData) -> None:
        self.setName(audio_data.name)

    def setName(self, name: str) -> None:
        self.header.setText(name)