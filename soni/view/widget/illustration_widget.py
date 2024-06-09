from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtGui import QResizeEvent, QPixmap
from PySide6.QtCore import Qt, QSize

from etc.audio_data import AudioData

from view.basic.v_box_layout_widget import VBoxLayoutWidget

import resources.resources_rc


class IllustrationWidget(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.fullness = 0.8
        self.pixmap = QPixmap(":/images/icon.png")
        self.pixmap_ratio = self.pixmap.width() / self.pixmap.height()

        self.illustration = QLabel(self)
        self.illustration.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.updateIllustration()

        self.main_layout = VBoxLayoutWidget()
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.illustration)

        self.setLayout(self.main_layout)

        self.setMinimumSize(40, 40)

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.updateIllustration()

    def setFullness(self, fullness: int) -> None:
        self.fullness = fullness
    
    def setAudioData(self, audio_data: AudioData) -> None:
        picture_png = audio_data.picture_png
        if picture_png:
            pixmap = QPixmap()
            pixmap.loadFromData(picture_png)
            self.setPixmap(pixmap)

    def setPixmap(self, pixmap: QPixmap) -> None:
        self.pixmap = pixmap
        self.pixmap_ratio = self.pixmap.width() / self.pixmap.height()
        self.updateIllustration()

    def clearPixmap(self) -> None:
        self.pixmap = QPixmap(":/images/icon.png")
        self.pixmap_ratio = self.pixmap.width() / self.pixmap.height()
        self.updateIllustration()

    def updateIllustration(self):
        size_x = int(self.width() * self.fullness)
        size_y = int(self.height() * self.fullness)
        screen_ratio = size_x / size_y
        if self.pixmap_ratio >= screen_ratio:
            size_y = int(size_x / self.pixmap_ratio)
        elif self.pixmap_ratio < screen_ratio:
            size_x = int(size_y * self.pixmap_ratio)
        self.illustration.setPixmap(self.pixmap.scaled(size_x, size_y))
