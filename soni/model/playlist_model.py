from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, Signal
from PySide6.QtSql import QSqlQuery, QSqlQueryModel

from etc.data_base import data_base
from etc.query import Query

class PlaylistModel(QWidget):
    playlistChanged = Signal(int)

    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)

        self.name = ""
        self.id = 0

    def setPlaylist(self, name: str):
        self.name = name
        self.id = data_base.selectPlaylistId(name)
        self.playlistChanged.emit(self.id)