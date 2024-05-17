import os

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QHBoxLayout,
    QVBoxLayout,
    QStackedLayout,
    QSlider,
    QWidget,
    QLabel,
    QPushButton,
    QSizePolicy,
    QMenuBar,
)
from PySide6.QtGui import (
    QScreen,
    QResizeEvent,
    QAction
)
from PySide6.QtCore import (
    Qt
)

from modules.data_base import data_base

from ui.widgets.header_widget import TrackHeaderWidget
from ui.widgets.audio_player_widget import AudioPlayerWidget
from ui.widgets.illustration_widget import IllustrationWidget
from ui.widgets.timeline_widget import TimelineWidget
from ui.widgets.playlist_widget import PlaylistWidget

from ui.windows.library_window import LibraryWindow
from ui.windows.settings_window import SettingsWindow


class AudioPlayerWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # basic init
        
        os.environ['QT_MULTIMEDIA_PREFERRED_PLUGINS'] = 'windowsmediafoundation'
        data_base.init()

        # name
        self.setWindowTitle("soni")

        # geometry
        self.setGeometry(0, 0, 800, 400)
        self.setMinimumSize(400, 300)

        # center window
        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geometry = self.geometry()
        geometry.moveCenter(center)
        self.move(geometry.topLeft())

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
        self.track_header.clicked.connect(self.openPlaylist)

        self.audio_player = AudioPlayerWidget(self)
        self.playlist = PlaylistWidget(self)

        self.audio_player.durationChanged.connect(self.timeline.setEndMilliseconds)
        self.audio_player.timeChanged.connect(self.timeline.setCurrentMilliseconds)

        # layout
        self.right_stack_layout = QStackedLayout()
        self.right_stack_layout.addWidget(self.audio_player)
        self.right_stack_layout.addWidget(self.playlist)

        self.right_side_layout = QVBoxLayout()
        self.right_side_layout.addWidget(self.track_header)
        self.right_side_layout.addLayout(self.right_stack_layout)

        self.center_layout = QHBoxLayout()
        self.center_layout.addWidget(self.illustration, 1)
        self.center_layout.addLayout(self.right_side_layout, 3)

        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.center_layout)
        self.main_layout.addWidget(self.timeline)

        # set layout
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

        self.test_action = QAction("test", self)
        self.test_action.setCheckable(True)
        self.test_action.triggered.connect(self.test)
        self.menuBar().addAction(self.test_action)

    def openPlaylist(self):
        self.playlist_open = not self.playlist_open
        self.right_stack_layout.setCurrentIndex(1 if self.playlist_open else 0)

    def test(self, checked):
        from modules.time import TimeFormat
        self.timeline.setTimeFormat(TimeFormat.HHmmss if checked else TimeFormat.mmss)
