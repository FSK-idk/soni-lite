import enum
from typing import List

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, Signal
from PySide6.QtSql import QSqlQuery, QSqlQueryModel

from etc.data_base import data_base
from etc.query import Query
from etc.audio_data import AudioData


class LoopFormat(enum.Enum):
    loop_none = enum.auto()
    loop_playlist = enum.auto()
    loop_audio = enum.auto()


class PlaylistModel(QWidget):
    playlistChanged = Signal(int)

    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)

        self.name = ""
        self.id = 0

        self.audio_datas: List[AudioData] = []

    def setPlaylist(self, name: str) -> None:
        self.name = name
        self.id = data_base.selectPlaylistId(name)
        self.playlistChanged.emit(self.id)
        self.audio_datas = data_base.selectPlaylistAudioDatas(str(self.id))

    def updatePlaylist(self) -> None:
        self.audio_datas = data_base.selectPlaylistAudioDatas(str(self.id))