from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QStackedLayout,
    QWidget,
)
from PySide6.QtGui import (
    QScreen,
    QAction,
)

from view.widget.audio_library_widget import AudioLibraryWidget
from view.widget.playlist_library_widget import PlaylistLibraryWidget

class LibraryWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        # widgets

        self.audio_library = AudioLibraryWidget(self)
        self.playlist_library = PlaylistLibraryWidget(self)

        # layout
        self.main_layout = QStackedLayout()
        self.main_layout.addWidget(self.audio_library)
        self.main_layout.addWidget(self.playlist_library)

        self.widget = QWidget(self)
        self.widget.setLayout(self.main_layout)
        self.setCentralWidget(self.widget)

        # menu

        self.show_audio_action = QAction("audio", self)
        self.show_audio_action.triggered.connect(self.showAudio)

        self.show_playlist_action = QAction("playlist", self)
        self.show_playlist_action.triggered.connect(self.showPlaylist)

        # audio
        self.audio_new_audio_action = QAction("new", self)
        self.audio_new_audio_action.triggered.connect(self.audio_library.newAudio)

        self.audio_modify_audio_action = QAction("modify", self)
        self.audio_modify_audio_action.triggered.connect(self.audio_library.modifyAudio)

        self.audio_delete_audio_action = QAction("delete", self)
        self.audio_delete_audio_action.triggered.connect(self.audio_library.deleteAudio)
        
        # playlist
        self.playlist_new_playlist_action = QAction("new", self)
        self.playlist_new_playlist_action.triggered.connect(self.playlist_library.newPlaylist)

        self.playlist_delete_playlist_action = QAction("delete", self)
        self.playlist_delete_playlist_action.triggered.connect(self.playlist_library.deletePlaylist)

        self.playlist_add_audio_action = QAction("add", self)
        self.playlist_add_audio_action.triggered.connect(self.playlist_library.addAudio)

        self.playlist_modify_audio_action = QAction("modify", self)
        self.playlist_modify_audio_action.triggered.connect(self.playlist_library.modifyAudio)

        self.playlist_remove_audio_action = QAction("remove", self)
        self.playlist_remove_audio_action.triggered.connect(self.playlist_library.removeAudio)

        # test
        self.test_action = QAction("test", self)
        self.test_action.triggered.connect(self.test)

        # self

        self.setWindowTitle("soni.library")
        self.setGeometry(0, 0, 800, 400)

        # center window
        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geometry = self.geometry()
        geometry.moveCenter(center)
        self.move(geometry.topLeft())

        self.showAudio()

    def showAudio(self) -> None:
        self.main_layout.setCurrentIndex(0)
        self.menuBar().clear()
        self.menuBar().addAction(self.show_playlist_action)
        self.menuBar().addAction(self.audio_new_audio_action)
        self.menuBar().addAction(self.audio_modify_audio_action)
        self.menuBar().addAction(self.audio_delete_audio_action)
        self.menuBar().addAction(self.test_action)

    def showPlaylist(self) -> None:
        self.main_layout.setCurrentIndex(1)
        self.menuBar().clear()
        self.menuBar().addAction(self.show_audio_action)
        self.menuBar().addAction(self.playlist_new_playlist_action)
        self.menuBar().addAction(self.playlist_delete_playlist_action)
        self.menuBar().addAction(self.playlist_add_audio_action)
        self.menuBar().addAction(self.playlist_modify_audio_action)
        self.menuBar().addAction(self.playlist_remove_audio_action)
        self.menuBar().addAction(self.test_action)

    def test(self) -> None:
        print("test")
        pass