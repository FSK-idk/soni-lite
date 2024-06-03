from PySide6.QtCore import (
    Qt,
)
from PySide6.QtSql import (
    QSqlQuery,
    QSqlQueryModel,
)

from model.data_base.data_base import data_base
from model.config import config
from model.data_base.query import Queries
from model.audio_data import AudioData

class PlaylistAudioTableModel:
    def __init__(self):

        self.ascending_order = True
        self.sort_column_index = 0
        self.search_data = AudioData()
        self.query_model = QSqlQueryModel()

        self.updateTable()
        self.updateHeaders()

    def setPlaylistData(self, playlist_id: int):
        self.search_data = playlist_id

    def setSortData(self, order: Qt.SortOrder, sort_column_index: int):
        self.ascending_order = (order != Qt.SortOrder.AscendingOrder)
        self.sort_column_index = sort_column_index

    def updateTable(self):
        query = QSqlQuery(data_base.data_base)
        query.prepare(Queries.select_playlist_audio(self.ascending_order, self.sort_column_index))
        query.bindValue(":id", self.search_data)
        query.exec()
        self.query_model.setQuery(query)

    def updateHeaders(self):
        self.query_model.setHeaderData(0, Qt.Orientation.Horizontal, "ID")
        self.query_model.setHeaderData(1, Qt.Orientation.Horizontal, "Title")
