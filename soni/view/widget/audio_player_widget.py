from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QFileDialog,

)
from PySide6.QtGui import (
    QPalette,
    QPixmap,
)
from PySide6.QtCore import (
    Qt,
    QUrl,
    Signal,
)

import resources.resources_rc

from model.audio_player_model import AudioPlayerModel

from view.basic.h_box_layout_widget import HBoxLayoutWidget
from view.basic.v_box_layout_widget import VBoxLayoutWidget


class AudioPlayerWidget(QWidget):
    durationChanged = Signal(int)
    timeChanged = Signal(int)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        
        self.audio_player_model = AudioPlayerModel(self)

        self.button_play = QPushButton(self)
        self.button_random = QPushButton(self)
        self.button_loop = QPushButton(self)
        self.button_next = QPushButton(self)
        self.button_prev = QPushButton(self)

        self.button_play.setText("Pause")
        self.button_play.clicked.connect(self.audio_player_model.play)
        self.button_random.setText("No Random")
        self.button_random.clicked.connect(self.audio_player_model.random)
        self.button_loop.setText("No Loop")
        self.button_loop.clicked.connect(self.audio_player_model.loop)
        self.button_next.setText("Next")
        self.button_next.clicked.connect(self.audio_player_model.next)
        self.button_prev.setText("Prev")
        self.button_prev.clicked.connect(self.audio_player_model.prev)

        self.center_layout = HBoxLayoutWidget()
        self.center_layout.addStretch(1)
        self.center_layout.addWidget(self.button_prev)
        self.center_layout.addWidget(self.button_play)
        self.center_layout.addWidget(self.button_next)
        self.center_layout.addStretch(1)

        self.bottom_layout = HBoxLayoutWidget()
        self.bottom_layout.addWidget(self.button_random)
        self.bottom_layout.addStretch(1)
        self.bottom_layout.addWidget(self.button_loop)

        self.main_layout = VBoxLayoutWidget()
        self.main_layout.addStretch(1)
        self.main_layout.addLayout(self.center_layout)
        self.main_layout.addStretch(1)
        self.main_layout.addLayout(self.bottom_layout)
        self.setLayout(self.main_layout)

    def selectAudio(self) -> None:
        self.filepath, _ = QFileDialog.getOpenFileName(self,"Выбрать файл", '', '*mp3')
        self.audio_player_model.setAudio(QUrl.fromLocalFile(self.filepath))
