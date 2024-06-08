from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QFileDialog,
    QHBoxLayout,
    QVBoxLayout,

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


class AudioPlayerWidget(QWidget):
    durationChanged = Signal(int)
    timeChanged = Signal(int)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        
        self.setMinimumSize(30, 30)

        self.audio_player_model = AudioPlayerModel(self)
        self.filepath = ""

        # widgets

        self.button_play = QPushButton(self)
        # self.button_pause = QPushButton(self)
        self.button_random_order = QPushButton(self)
        self.button_loop = QPushButton(self)
        self.button_next = QPushButton(self)
        self.button_past = QPushButton(self)

        self.button_play.setIcon(QPixmap(":/icons/play-black.svg"))
        self.button_play.clicked.connect(self.play)

        # self.button_pause.setText('Pause')
        # self.button_pause.clicked.connect(self.pause)

        self.button_random_order.setText('Random')
        self.button_random_order.clicked.connect(self.random_order)

        self.button_loop.setText('Loop')
        self.button_loop.clicked.connect(self.loop)

        self.button_next.setText('Next')
        self.button_next.clicked.connect(self.next)

        self.button_past.setText('Prev')
        self.button_past.clicked.connect(self.past)

        # layout

        self.hlayout_mid = QHBoxLayout()
        self.hlayout_bottomn = QHBoxLayout()
        self.vlayout = QVBoxLayout(self)

        self.hlayout_mid.addStretch(1)
        self.hlayout_mid.addWidget(self.button_past)
        self.hlayout_mid.addWidget(self.button_play)
        self.hlayout_mid.addWidget(self.button_next)
        self.hlayout_mid.addStretch(1)
        self.hlayout_bottomn.addWidget(self.button_random_order)
        self.hlayout_bottomn.addStretch(1)
        self.hlayout_bottomn.addWidget(self.button_loop)
        self.vlayout.addStretch(1)
        self.vlayout.addLayout(self.hlayout_mid)
        self.vlayout.addStretch(1)
        self.vlayout.addLayout(self.hlayout_bottomn)
        self.setLayout(self.vlayout)

    def play(self):
        self.audio_player_model.play()
 
    def pause(self):
        self.audio_player_model.pause()

    def selectAudio(self) -> None:
        self.filepath, _ = QFileDialog.getOpenFileName(self,"Выбрать файл", '', '*mp3')
        self.audio_player_model.setAudio(QUrl.fromLocalFile(self.filepath))

    def loop(self):
        pass

    def next(self):
        pass

    def past(self):
        pass

    def random_order(self):
        pass
