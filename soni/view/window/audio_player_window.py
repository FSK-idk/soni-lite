import os

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QToolBar
from PySide6.QtGui import QScreen, QAction, QPixmap
from PySide6.QtCore import Qt

from etc.data_base import data_base

from view.basic.v_box_layout_widget import VBoxLayoutWidget
from view.basic.h_box_layout_widget import HBoxLayoutWidget
from view.basic.stacked_layout_widget import StackedLayoutWidget

from view.widget.header_widget import TrackHeaderWidget
from view.widget.audio_player_widget import AudioPlayerWidget
from view.widget.illustration_widget import IllustrationWidget
from view.widget.timeline_widget import TimelineWidget
from view.widget.playlist_widget import PlaylistWidget

from view.window.audio_library_window import AudioLibraryWindow
from view.window.playlist_library_window import PlaylistLibraryWindow

import resources.resources_rc


class AudioPlayerWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        os.environ['QT_MULTIMEDIA_PREFERRED_PLUGINS'] = 'windowsmediafoundation'
        data_base.init()

        self.playlist_open = False
        self.minimum_window_ratio = 2

        self.audio_library = AudioLibraryWindow()
        self.playlist_library = PlaylistLibraryWindow()

        self.timeline = TimelineWidget(self)
        self.illustration = IllustrationWidget(self)
        self.audio_header = TrackHeaderWidget(self)
        self.audio_player = AudioPlayerWidget(self)
        self.playlist = PlaylistWidget(self)

        self.timeline.timeChanged.connect(self.audio_player.setTime)
        self.timeline.volumeChanged.connect(self.audio_player.setVolume)
        self.audio_header.clicked.connect(self.openPlaylist)
        self.audio_player.durationChanged.connect(self.timeline.setEndMilliseconds)
        self.audio_player.timeChanged.connect(self.timeline.setCurrentMilliseconds)
        self.audio_player.audioEnded.connect(self.audio_player.onAudioEnded)
        self.playlist.audioChanged.connect(self.audio_player.setAudioData)
        self.playlist.audioChanged.connect(self.illustration.setAudioData)
        self.playlist.audioChanged.connect(self.audio_header.setAudioData)
        self.audio_player.nextAudio.connect(self.playlist.next)
        self.audio_player.nextRandomAudio.connect(self.playlist.nextRandom)
        self.audio_player.prevAudio.connect(self.playlist.prev)

        self.right_stack_layout = StackedLayoutWidget()
        self.right_stack_layout.addWidget(self.audio_player)
        self.right_stack_layout.addWidget(self.playlist)

        self.right_side_layout = VBoxLayoutWidget()
        self.right_side_layout.addWidget(self.audio_header)
        self.right_side_layout.addLayout(self.right_stack_layout)

        self.center_layout = HBoxLayoutWidget()
        self.center_layout.addWidget(self.illustration, 1)
        self.center_layout.addLayout(self.right_side_layout, 3)

        self.main_layout = VBoxLayoutWidget()
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.addLayout(self.center_layout)
        self.main_layout.addWidget(self.timeline)

        self.widget = QWidget(self)
        self.widget.setLayout(self.main_layout)
        self.setCentralWidget(self.widget)

        self.toolbar = QToolBar(self)
        self.toolbar.setFloatable(False)
        self.toolbar.setMovable(False)
        self.addToolBar(self.toolbar)
        self.toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.open_playlist_library_action = QAction(QPixmap(":icon/list-music-white.svg"), "playlist", self)
        self.open_playlist_library_action.triggered.connect(self.playlist_library.show)
        self.toolbar.addAction(self.open_playlist_library_action)

        self.open_audio_library_action = QAction(QPixmap(":icon/library-white.svg"), "library", self)
        self.open_audio_library_action.triggered.connect(self.audio_library.show)
        self.toolbar.addAction(self.open_audio_library_action)

        self.setWindowTitle("soni.lite")
        self.setWindowIcon(QPixmap(":image/icon-s.png"))
        self.setGeometry(0, 0, 800, 400)
        self.setMinimumSize(400, 300)

        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geometry = self.geometry()
        geometry.moveCenter(center)
        self.move(geometry.topLeft())

    def openPlaylist(self) -> None:
        self.playlist_open = not self.playlist_open
        self.right_stack_layout.setCurrentIndex(1 if self.playlist_open else 0)

    def closeEvent(self, event) -> None:
        self.audio_library.close()
        self.playlist_library.close()