from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from PySide6.QtSql import QSqlQuery, QSqlQueryModel

from etc.data_base import data_base
from etc.query import Query
from etc.audio_data import AudioData

class PlaylistAudioTableModel(QSqlQueryModel):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.descending = False
        self.sort_column = 2
        self.playlist_id = AudioData()

        self.updateTable()
        self.updateHeader()

    def setSearchData(self, playlist_id: int):
        self.playlist_id = playlist_id

    def updateTable(self):
        query = QSqlQuery(data_base.data_base)
        query.prepare(Query.selectPlaylistAudioTable(self.descending, self.sort_column))
        query.bindValue(":id", self.playlist_id)
        query.exec()
        self.setQuery(query)

    def updateHeader(self):
        self.setHeaderData(0, Qt.Orientation.Horizontal, "ID")
        self.setHeaderData(1, Qt.Orientation.Horizontal, "Title")
        self.setHeaderData(2, Qt.Orientation.Horizontal, "Serial")


    def moveUp(self, audio_id: int) -> None:
        data_base.movePlaylistAudioUp(self.playlist_id, audio_id)

    def moveDown(self, audio_id: int) -> None:
        data_base.movePlaylistAudioDown(self.playlist_id, audio_id)