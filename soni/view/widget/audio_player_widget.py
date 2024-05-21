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
from PySide6.QtMultimedia import (
    QMediaPlayer,
    QAudioOutput,
)

import resources.resources_rc

# TODO: add functionality
class AudioPlayerWidget(QWidget):
    durationChanged = Signal(int)
    timeChanged = Signal(int)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        
        self.setMinimumSize(30, 30)

        # attributes

        self.audio_player = QMediaPlayer()
        self.audio_output = QAudioOutput()

        self.audio_player.setAudioOutput(self.audio_output)
        self.audio_player.durationChanged.connect(self.durationChanged.emit)
        self.audio_player.positionChanged.connect(self.timeChanged.emit)

        self.audio_output.setVolume(50)

        self.filepath = ""

        # TODO: debug
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, Qt.GlobalColor.black)

        self.setAutoFillBackground(True)
        self.setPalette(palette)

        self.pause_triger = False

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
        self.audio_player.play()
 
    def pause(self):
        if self.pause_triger == False:
            self.audio_player.pause()
            self.pause_triger = True
        else:
            self.audio_player.play()
            self.pause_triger = False

    def selectAudio(self) -> None:
        self.filepath, _ = QFileDialog.getOpenFileName(self,"Выбрать файл", '', '*mp3')
        self.audio_player.setSource(QUrl.fromLocalFile(self.filepath))

    def loop(self):
        pass

    def next(self):
        pass

    def past(self):
        pass

    def random_order(self):
        pass
