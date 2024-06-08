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

class AudioPlayerModel(QWidget):
    durationChanged = Signal(int)
    timeChanged = Signal(int)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.audio_player = QMediaPlayer(self)
        self.audio_output = QAudioOutput(self)

        self.audio_player.setAudioOutput(self.audio_output)
        self.audio_player.durationChanged.connect(self.durationChanged.emit)
        self.audio_player.positionChanged.connect(self.timeChanged.emit)

        self.audio_output.setVolume(50)


    def play(self):
        # self.audio_player.play()
        pass
 
    def pause(self):
        # if self.pause_triger == False:
        #     self.audio_player.pause()
        #     self.pause_triger = True
        # else:
        #     self.audio_player.play()
        #     self.pause_triger = False
        pass

    def next(self):
        pass

    def prev(self):
        pass

    def setLoop(self, loop: bool):
        pass

    def setRandom(self, random: bool):
        pass

    def setAudio(self, url: QUrl):
        # self.audio_player.setSource(url)
        pass

    def setPlaylist(self):
        pass