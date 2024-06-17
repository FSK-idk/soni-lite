from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from PySide6.QtSql import QSqlQuery, QSqlQueryModel

from etc.data_base import data_base
from etc.query import Query


class PlaylistAudioTableModel(QSqlQueryModel):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.descending = False
        self.sort_column = 2
        self.playlist_id = -1

        data_base.updatedPlaylistTable.connect(self.updateTable)
        data_base.updatedPlaylistTable.connect(self.updateHeader)

        self.updateTable()
        self.updateHeader()

    def setPlaylistId(self, playlist_id: int) -> None:
        # print("AAA")
        self.playlist_id = playlist_id
        self.updateTable()

    def setPlaylistName(self, name: str) -> None:
        # print("BBB", name)
        if name != "":
            self.playlist_id = data_base.selectPlaylistId(name)
            self.updateTable()

    def updateTable(self) -> None:
        print("id", self.playlist_id)
        query = QSqlQuery(data_base.data_base)
        query.prepare(Query.selectPlaylistAudioTable(self.descending, self.sort_column))
        query.bindValue(":id", self.playlist_id)
        query.exec()
        self.setQuery(query)

    def updateHeader(self) -> None:
        self.setHeaderData(0, Qt.Orientation.Horizontal, "ID")
        self.setHeaderData(1, Qt.Orientation.Horizontal, "Title")
        self.setHeaderData(2, Qt.Orientation.Horizontal, "Serial")

    def moveUp(self, audio_id: int) -> None:
        data_base.movePlaylistAudioUp(str(self.playlist_id), str(audio_id))
        # self.updateTable()

    def moveDown(self, audio_id: int) -> None:
        data_base.movePlaylistAudioDown(str(self.playlist_id), str(audio_id))
        # self.updateTable()
