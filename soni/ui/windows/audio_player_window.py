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
    QAction
)
from PySide6.QtCore import (
    Qt
)

from ui.widgets.track_header_widget import TrackHeaderWidget
from ui.widgets.audio_player_widget import AudioPlayerWidget
from ui.widgets.illustration_widget import IllustrationWidget
from ui.widgets.time_line_widget import TimeLineWidget
from ui.widgets.playlist_widget import PlaylistWidget

from ui.windows.library_window import LibraryWindow
from ui.windows.settings_window import SettingsWindow


class AudioPlayerWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # name
        self.setWindowTitle("soni")

        # geometry
        self.setGeometry(0, 0, 800, 400)

        # center window
        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geometry = self.geometry()
        geometry.moveCenter(center)
        self.move(geometry.topLeft())

        # windows
        self.library = LibraryWindow()
        self.settings = SettingsWindow()

        # widgets
        self.time_line = TimeLineWidget(self)
        self.illustration = IllustrationWidget(self)
        self.track_header = TrackHeaderWidget(self)
        self.audio_player = AudioPlayerWidget(self)
        self.playlist = PlaylistWidget(self)

        # layout
        self.right_stack_layout = QStackedLayout()
        self.right_stack_layout.addWidget(self.audio_player)
        self.right_stack_layout.addWidget(self.playlist)

        self.right_side_layout = QVBoxLayout()
        self.right_side_layout.addWidget(self.track_header)
        self.right_side_layout.addLayout(self.right_stack_layout)

        self.center_layout = QHBoxLayout()
        self.center_layout.addWidget(self.illustration)
        self.center_layout.addLayout(self.right_side_layout)

        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.center_layout)
        self.main_layout.addWidget(self.time_line)

        # set layout
        self.widget = QWidget(self)
        self.widget.setLayout(self.main_layout)
        self.setCentralWidget(self.widget)

        # menu
        self.open_playlist_action = QAction("playlist", self)
        self.open_playlist_action.setCheckable(True)
        self.open_playlist_action.triggered.connect(self.open_playlist)
        self.menuBar().addAction(self.open_playlist_action)

        self.open_library_action = QAction("library", self)
        self.open_library_action.triggered.connect(self.library.show)
        self.menuBar().addAction(self.open_library_action)

        self.open_settings_action = QAction("settings", self)
        self.open_settings_action.triggered.connect(self.settings.show)
        self.menuBar().addAction(self.open_settings_action)

    def open_playlist(self, checked):
        self.right_stack_layout.setCurrentIndex(1 if checked else 0)