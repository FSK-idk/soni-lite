import os

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QStackedLayout,
    QWidget,
    QSizePolicy,
    QMenuBar,
)
from PySide6.QtGui import (
    QScreen,
    QAction
)
from PySide6.QtCore import (
    Qt
)

from model.data_base.data_base import data_base

from view.default.v_box_layout_widget import VBoxLayoutWidget
from view.default.h_box_layout_widget import HBoxLayoutWidget

from view.widget.header_widget import TrackHeaderWidget
from view.widget.audio_player_widget import AudioPlayerWidget
from view.widget.illustration_widget import IllustrationWidget
from view.widget.timeline_widget import TimelineWidget
from view.widget.playlist_widget import PlaylistWidget

from view.window.library_window import LibraryWindow
from view.window.settings_window import SettingsWindow


class AudioPlayerWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        # init

        os.environ['QT_MULTIMEDIA_PREFERRED_PLUGINS'] = 'windowsmediafoundation'
        data_base.init()

        # attributes

        self.playlist_open = False
        self.minimum_window_ratio = 2

        # windows

        self.library = LibraryWindow()
        self.settings = SettingsWindow()

        # widgets

        self.timeline = TimelineWidget(self)
        self.illustration = IllustrationWidget(self)
        self.track_header = TrackHeaderWidget(self)
        self.audio_player = AudioPlayerWidget(self)
        self.playlist = PlaylistWidget(self)

        self.track_header.clicked.connect(self.openPlaylist)
        self.audio_player.durationChanged.connect(self.timeline.setEndMilliseconds)
        self.audio_player.timeChanged.connect(self.timeline.setCurrentMilliseconds)

        # layout

        self.right_stack_layout = QStackedLayout()
        self.right_stack_layout.addWidget(self.audio_player)
        self.right_stack_layout.addWidget(self.playlist)

        self.right_side_layout = VBoxLayoutWidget()
        self.right_side_layout.addWidget(self.track_header)
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

        # menu

        self.open_playlist_action = QAction("playlist", self)
        self.open_playlist_action.setCheckable(True)
        self.open_playlist_action.triggered.connect(self.openPlaylist)
        self.menuBar().addAction(self.open_playlist_action)

        self.open_library_action = QAction("library", self)
        self.open_library_action.triggered.connect(self.library.show)
        self.menuBar().addAction(self.open_library_action)

        self.open_settings_action = QAction("settings", self)
        self.open_settings_action.triggered.connect(self.settings.show)
        self.menuBar().addAction(self.open_settings_action)

        self.test_action = QAction("select", self)
        self.test_action.setCheckable(True)
        self.test_action.triggered.connect(self.audio_player.selectAudio)
        self.menuBar().addAction(self.test_action)

        self.test_action = QAction("test", self)
        self.test_action.setCheckable(True)
        self.test_action.triggered.connect(self.test)
        self.menuBar().addAction(self.test_action)

        # self

        self.setWindowTitle("soni")
        self.setGeometry(0, 0, 800, 400)
        self.setMinimumSize(400, 300)

        # center window
        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geometry = self.geometry()
        geometry.moveCenter(center)
        self.move(geometry.topLeft())
        

    def openPlaylist(self) -> None:
        self.playlist_open = not self.playlist_open
        self.right_stack_layout.setCurrentIndex(1 if self.playlist_open else 0)

    def test(self, checked: bool) -> None:
        print("test")

        return