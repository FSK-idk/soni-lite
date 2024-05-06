from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QFileDialog,
)
from PySide6.QtGui import (
    QPalette,
)
from PySide6.QtCore import (
    Qt,
    QUrl,
    Signal,
)
from PySide6.QtMultimedia import (
    QMediaPlayer,
    QAudioOutput
)

# TODO: add functionality
class AudioPlayerWidget(QWidget):
    durationChanged = Signal(int)
    timeChanged = Signal(int)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        
        self.setMinimumSize(30, 30)

        # attributes
        self.audio_player = QMediaPlayer()
        self.audioOutput = QAudioOutput()

        self.audio_player.setAudioOutput(self.audioOutput)
        self.audio_player.durationChanged.connect(self.durationChanged.emit)
        self.audio_player.positionChanged.connect(self.timeChanged.emit)

        self.audioOutput.setVolume(50)

        # TODO: debug
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, Qt.GlobalColor.magenta)

        self.setAutoFillBackground(True)
        self.setPalette(palette)

        # Creating Buttons
        self.button_play = QPushButton('Play', self)
        self.button_play.resize(50, 50)
        self.button_play.move(0, 210)
        self.button_play.clicked.connect(self.play)
        self.button_pause = QPushButton('Pause', self)
        self.button_pause.resize(50, 50)
        self.button_pause.move(50, 210)
        self.button_pause.clicked.connect(self.pause)
        self.button_track_selection = QPushButton('Select', self)
        self.button_track_selection.resize(50, 50)
        self.button_track_selection.move(100, 210)
        self.button_track_selection.clicked.connect(self.seletcion_track)

    def play(self):
        self.audio_player.play()
 
    def pause(self):
        pass

    def seletcion_track(self):
        self.dialogue = QFileDialog.getOpenFileName(self,"Выбрать файл", '', '*mp3')
        self.audio_player.setSource(QUrl.fromLocalFile(self.dialogue[0]))
        print(self.dialogue[0])
