from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from PySide6.QtSql import QSqlQuery, QSqlQueryModel

from etc.data_base import data_base
from etc.config import config
from etc.query import Query
from etc.audio_data import AudioData


header_title = {
    "id":                       "ID",
    "name":                     "Title",
    "album_name":               "Album title",
    "genre_name":               "Genre",
    "performer_name":           "Performer",
    "composer_name":            "Composer",
    "publisher_name":           "Publisher",
    "modified_by_name":         "Modified by",
    "picture_artist_name":      "Picture artist",
    "text_author_name":         "Text author",
}


class AudioTableModel(QSqlQueryModel):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        
        self.descending = False
        self.sort_column = 0
        self.search_data = AudioData()

        self.updateTable()
        self.updateHeader()

    def setSearchData(self, search_data: AudioData) -> None:
        self.search_data = search_data

    def setSortData(self, order: Qt.SortOrder, sort_column: int) -> None:
        self.descending = (order != Qt.SortOrder.DescendingOrder)
        self.sort_column = sort_column

    def updateTable(self) -> None:
        query = QSqlQuery(data_base.data_base)
        query.prepare(Query.selectAudioTable(self.descending, self.sort_column))
        query.bindValue(":name", self.search_data.name)
        query.bindValue(":album_name", self.search_data.album_name)
        query.bindValue(":genre_name", self.search_data.genre_name)
        query.bindValue(":performer_name", self.search_data.performer_name)
        query.bindValue(":composer_name", self.search_data.composer_name)
        query.bindValue(":publisher_name", self.search_data.publisher_name)
        query.bindValue(":modified_by_name", self.search_data.modified_by_name)
        query.bindValue(":picture_artist_name", self.search_data.picture_artist_name)
        query.bindValue(":text_author_name", self.search_data.text_author_name)
        query.exec()
        self.setQuery(query)

    def updateHeader(self) -> None:
        idx = 0
        for key, val in config.items("Audio Library Shown Parameters"):
            if val == "True":
                self.setHeaderData(idx, Qt.Orientation.Horizontal, header_title[key])
                idx += 1
