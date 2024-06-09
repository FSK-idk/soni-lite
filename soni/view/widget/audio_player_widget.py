from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Signal, Qt

from model.audio_player_model import AudioPlayerModel
from model.playlist_model import LoopFormat

from view.basic.h_box_layout_widget import HBoxLayoutWidget
from view.basic.v_box_layout_widget import VBoxLayoutWidget
from view.basic.push_label_widget import PushLabelWidget

import resources.resources_rc


class AudioPlayerWidget(QWidget):
    durationChanged = Signal(int)
    timeChanged = Signal(int)
    audioEnded = Signal()
    nextAudio = Signal()
    nextRandomAudio = Signal()
    prevAudio = Signal()

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        
        self.audio_player_model = AudioPlayerModel(self)

        self.audio_player_model.durationChanged.connect(self.durationChanged.emit)
        self.audio_player_model.timeChanged.connect(self.timeChanged.emit)
        self.audio_player_model.audioEnded.connect(self.onAudioEnded)

        self.button_play = PushLabelWidget(self)
        self.button_random = PushLabelWidget(self)
        self.button_loop = PushLabelWidget(self)
        self.button_next = PushLabelWidget(self)
        self.button_prev = PushLabelWidget(self)

        self.button_play.setFixedSize(50,50)
        self.button_play.setPixmap(QPixmap(":icon/play-white.svg").scaled(40, 40, mode=Qt.TransformationMode.SmoothTransformation))
        self.button_play.clicked.connect(self.play)
        self.button_random.setFixedSize(50,50)
        self.button_random.setPixmap(QPixmap(":icon/shuffle-gray.svg").scaled(40, 40, mode=Qt.TransformationMode.SmoothTransformation))
        self.button_random.clicked.connect(self.random)
        self.button_loop.setFixedSize(50,50)
        self.button_loop.setPixmap(QPixmap(":icon/repeat-gray.svg").scaled(40, 40, mode=Qt.TransformationMode.SmoothTransformation))
        self.button_loop.clicked.connect(self.loop)
        self.button_next.setFixedSize(50,50)
        self.button_next.setPixmap(QPixmap(":icon/skip-forward-white.svg").scaled(40, 40, mode=Qt.TransformationMode.SmoothTransformation))
        self.button_next.clicked.connect(self.audio_player_model.next)
        self.button_prev.setFixedSize(50,50)
        self.button_prev.setPixmap(QPixmap(":icon/skip-back-white.svg").scaled(40, 40, mode=Qt.TransformationMode.SmoothTransformation))
        self.button_prev.clicked.connect(self.audio_player_model.prev)
        self.audio_player_model.nextAudio.connect(self.nextAudio.emit)
        self.audio_player_model.nextRandomAudio.connect(self.nextRandomAudio.emit)
        self.audio_player_model.prevAudio.connect(self.prevAudio.emit)

        self.center_layout = HBoxLayoutWidget()
        self.center_layout.addStretch(1)
        self.center_layout.addWidget(self.button_prev)
        self.center_layout.addWidget(self.button_play)
        self.center_layout.addWidget(self.button_next)
        self.center_layout.addStretch(1)

        self.left_layout = VBoxLayoutWidget()
        self.left_layout.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.left_layout.addWidget(self.button_random)

        self.right_layout = VBoxLayoutWidget()
        self.right_layout.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.right_layout.addWidget(self.button_loop)

        self.main_layout = HBoxLayoutWidget()
        self.main_layout.addLayout(self.left_layout)
        self.main_layout.addLayout(self.center_layout)
        self.main_layout.addLayout(self.right_layout)
        self.setLayout(self.main_layout)

    def onAudioEnded(self) -> None:
        match self.audio_player_model.looping:
            case LoopFormat.loop_none:
                self.audio_player_model.pause()
                self.button_play.setPixmap(QPixmap(":icon/play-white.svg").scaled(40, 40, mode=Qt.TransformationMode.SmoothTransformation))
            case LoopFormat.loop_playlist:
                self.audio_player_model.next()
                self.audio_player_model.play()
                self.button_play.setPixmap(QPixmap(":icon/pause-white.svg").scaled(40, 40, mode=Qt.TransformationMode.SmoothTransformation))
            case LoopFormat.loop_audio:
                self.audio_player_model.play()
                self.button_play.setPixmap(QPixmap(":icon/pause-white.svg").scaled(40, 40, mode=Qt.TransformationMode.SmoothTransformation))

    def play(self) -> None:
        if not self.audio_player_model.playing:
            self.audio_player_model.play()
            self.button_play.setPixmap(QPixmap(":icon/pause-white.svg").scaled(40, 40, mode=Qt.TransformationMode.SmoothTransformation))
        else:
            self.audio_player_model.pause()
            self.button_play.setPixmap(QPixmap(":icon/play-white.svg").scaled(40, 40, mode=Qt.TransformationMode.SmoothTransformation))

    def loop(self) -> None:
        self.audio_player_model.loop()
        match self.audio_player_model.looping:
            case LoopFormat.loop_none:
                self.button_loop.setPixmap(QPixmap(":icon/repeat-gray.svg").scaled(40, 40, mode=Qt.TransformationMode.SmoothTransformation))
            case LoopFormat.loop_playlist:
                self.button_loop.setPixmap(QPixmap(":icon/repeat-white.svg").scaled(40, 40, mode=Qt.TransformationMode.SmoothTransformation))
            case LoopFormat.loop_audio:
                self.button_loop.setPixmap(QPixmap(":icon/repeat-1-white.svg").scaled(40, 40, mode=Qt.TransformationMode.SmoothTransformation))

    def random(self) -> None:
        self.audio_player_model.random()
        if self.audio_player_model.randoming:
            self.button_random.setPixmap(QPixmap(":icon/shuffle-white.svg").scaled(40, 40, mode=Qt.TransformationMode.SmoothTransformation))
        else:
            self.button_random.setPixmap(QPixmap(":icon/shuffle-gray.svg").scaled(40, 40, mode=Qt.TransformationMode.SmoothTransformation))

    def setTime(self, milliseconds: int) -> None:
        self.audio_player_model.setTime(milliseconds)

    def setVolume(self, volume: int) -> None:
        self.audio_player_model.setVolume(volume)

    def setAudioData(self, audio_data) -> None:
        self.audio_player_model.setAudioData(audio_data)
