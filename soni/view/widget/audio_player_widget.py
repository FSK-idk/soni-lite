from PySide6.QtWidgets import QWidget
from PySide6.QtGui import (
    QPixmap,
)
from PySide6.QtCore import Signal

import resources.resources_rc

from model.audio_player_model import AudioPlayerModel
from model.playlist_model import LoopFormat

from view.basic.h_box_layout_widget import HBoxLayoutWidget
from view.basic.v_box_layout_widget import VBoxLayoutWidget
from view.basic.push_button_widget import PushButtonWidget


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

        self.button_play = PushButtonWidget(self)
        self.button_random = PushButtonWidget(self)
        self.button_loop = PushButtonWidget(self)
        self.button_next = PushButtonWidget(self)
        self.button_prev = PushButtonWidget(self)

        self.button_play.setText("On pause")
        self.button_play.clicked.connect(self.play)
        self.button_random.setText("No random")
        self.button_random.clicked.connect(self.random)
        self.button_loop.setText("No loop")
        self.button_loop.clicked.connect(self.loop)
        self.button_next.setText("Next")
        self.button_next.clicked.connect(self.audio_player_model.next)
        self.button_prev.setText("Prev")
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

    def onAudioEnded(self) -> None:
        match self.audio_player_model.looping:
            case LoopFormat.loop_none:
                self.audio_player_model.pause()
                self.button_play.setText("On pause")
            case LoopFormat.loop_playlist:
                self.audio_player_model.next()
                self.audio_player_model.play()
                self.button_play.setText("Playing")
            case LoopFormat.loop_audio:
                self.audio_player_model.play()
                self.button_play.setText("Playing")

    def play(self):
        if not self.audio_player_model.playing:
            self.audio_player_model.play()
            self.button_play.setText("Playing")
        else:
            self.audio_player_model.pause()
            self.button_play.setText("On pause")

    def loop(self):
        self.audio_player_model.loop()
        match self.audio_player_model.looping:
            case LoopFormat.loop_none:
                self.button_loop.setText("No loop")
            case LoopFormat.loop_playlist:
                self.button_loop.setText("Loop playlist")
            case LoopFormat.loop_audio:
                self.button_loop.setText("Loop audio")

    def random(self):
        self.audio_player_model.random()
        if self.audio_player_model.randoming:
            self.button_random.setText("Random")
        else:
            self.button_random.setText("No random")

    def setTime(self, milliseconds: int) -> None:
        self.audio_player_model.setTime(milliseconds)

    def setVolume(self, volume: int) -> None:
        self.audio_player_model.setVolume(volume)

    def setAudioData(self, audio_data) -> None:
        self.audio_player_model.setAudioData(audio_data)
