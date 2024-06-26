import os
import time

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QUrl, Signal
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput

from etc.audio_data import AudioData

from model.playlist_model import LoopFormat


class AudioPlayerModel(QWidget):
    durationChanged = Signal(int)
    timeChanged = Signal(int)
    audioEnded = Signal()
    nextAudio = Signal()
    nextRandomAudio = Signal()
    prevAudio = Signal()

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
        self.audio_player.mediaStatusChanged.connect(self.onStatusChanged)

        self.audio_output.setVolume(0.5)

    def onStatusChanged(self, status: QMediaPlayer.MediaStatus) -> None:
        match status:
            case QMediaPlayer.MediaStatus.EndOfMedia:
                self.audioEnded.emit()

    def play(self) -> None:
        self.playing = True
        self.audio_player.play()

    def pause(self) -> None:
        self.playing = False
        self.audio_player.pause()

    def loop(self) -> None:
        match self.looping:
            case LoopFormat.loop_none:
                self.looping = LoopFormat.loop_playlist
            case LoopFormat.loop_playlist:
                self.looping = LoopFormat.loop_audio
            case LoopFormat.loop_audio:
                self.looping = LoopFormat.loop_none

    def random(self) -> None:
        self.randoming = not self.randoming

    def next(self) -> None:
        if self.randoming:
            self.nextRandomAudio.emit()
        else:
            self.nextAudio.emit()

    def prev(self) -> None:
        self.prevAudio.emit()

    def setTime(self, milliseconds: int) -> None:
        self.audio_player.setPosition(milliseconds)

    def setVolume(self, volume: int) -> None:
        self.audio_output.setVolume(volume / 100)

    def setAudioData(self, audio_data: AudioData) -> None:
        self.audio_data = audio_data
        if os.path.isfile(audio_data.filepath):
            if self.playing:
                self.audio_player.stop()
                time.sleep(.05)
            self.audio_player.setSource(QUrl.fromLocalFile(audio_data.filepath))
            if self.playing:
                time.sleep(.05)
                self.audio_player.play()
        else:
            self.nextAudio.emit()