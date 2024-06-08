from PySide6.QtWidgets import (
    QWidget,

)
from PySide6.QtCore import (
    Qt,
    QUrl,
    Signal,
)
from PySide6.QtMultimedia import (
    QMediaPlayer,
    QAudioOutput,
)

from model.playlist_model import LoopFormat
from etc.audio_data import AudioData


class AudioPlayerModel(QWidget):
    durationChanged = Signal(int)
    timeChanged = Signal(int)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.playing = False
        self.randoming = False
        self.looping = LoopFormat.loop_none

        self.audio_data = AudioData()

        self.audio_player = QMediaPlayer(self)
        self.audio_output = QAudioOutput(self)

        self.audio_player.setAudioOutput(self.audio_output)
        self.audio_player.durationChanged.connect(self.durationChanged.emit)
        self.audio_player.positionChanged.connect(self.timeChanged.emit)

        self.audio_output.setVolume(50)


    def play(self):
        pass

    def loop(self):
        pass

    def random(self):
        pass

    def next(self):
        pass

    def prev(self):
        pass





    def setAudio(self, url: QUrl):
        # self.audio_player.setSource(url)
        pass

    def setPlaylist(self):
        pass