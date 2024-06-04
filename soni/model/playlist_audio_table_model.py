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
        self.sort_column = 0
        self.search_data = AudioData()

        self.updateTable()
        self.updateHeader()

    def setSearchData(self, search_data: int):
        self.search_data = search_data

    def setSortData(self, order: Qt.SortOrder, sort_column: int):
        self.descending = (order != Qt.SortOrder.DescendingOrder)
        self.sort_column = sort_column

    def updateTable(self):
        query = QSqlQuery(data_base.data_base)
        query.prepare(Query.selectPlaylistAudioTable(self.descending, self.sort_column))
        query.bindValue(":id", self.search_data)
        query.exec()
        self.setQuery(query)

    def updateHeader(self):
        self.setHeaderData(0, Qt.Orientation.Horizontal, "ID")
        self.setHeaderData(1, Qt.Orientation.Horizontal, "Title")