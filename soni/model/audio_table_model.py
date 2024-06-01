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


header_title = {
    'title':                   'Title',
    'album_title':             'Album title',
    'duration':                'Duration',
    'genre':                   'Genre',
    'language':                'Language',
    'rating':                  'Rating',
    'bpm':                     'BPM',
    'performer':               'Performer',
    'composer':                'Composer',
    'publisher':               'Publisher',
    'modified_by':             'Modified by',
    'release_date':            'Release date',
    'picture_artist':          'Picture artist',
    'text_author':             'Text author',
    'original_title':          'Original title',
    'original_album_title':    'Original album title',
    'original_performer':      'Original performer',
    'original_composer':       'Original composer',
    'original_publisher':      'Original publisher',
    'original_release_date':   'Original release date',
    'original_text_author':    'Original text author',
    'isrc':                    'ISRC',
}


class AudioTableModel:
    def __init__(self):

        self.ascending_order = True
        self.sort_column_index = 0
        self.search_data = AudioData()
        self.query_model = QSqlQueryModel()

        self.updateTable()
        self.updateHeaders()

    def setSearchData(self, search_data: AudioData):
        self.search_data = search_data

    def setSortData(self, order: Qt.SortOrder, sort_column_index: int):
        self.ascending_order = (order != Qt.SortOrder.AscendingOrder)
        self.sort_column_index = sort_column_index

    def updateTable(self):
        query = QSqlQuery(data_base.data_base)
        query.prepare(Queries.select_audio(self.ascending_order, self.sort_column_index))
        query.bindValue(":title", self.search_data.title)
        query.bindValue(":album_title", self.search_data.album_title)
        query.bindValue(":duration", "")
        query.bindValue(":genre", self.search_data.genre)
        query.bindValue(":language", "")
        query.bindValue(":rating", "")
        query.bindValue(":bpm", "")
        query.bindValue(":performer", self.search_data.performer)
        query.bindValue(":composer", self.search_data.composer)
        query.bindValue(":publisher", self.search_data.publisher)
        query.bindValue(":modified_by", self.search_data.modified_by)
        query.bindValue(":release_date", "")
        query.bindValue(":picture_artist", self.search_data.picture_artist)
        query.bindValue(":text_author", self.search_data.text_author)
        query.bindValue(":original_title", self.search_data.original_title)
        query.bindValue(":original_album_title", self.search_data.original_album_title)
        query.bindValue(":original_performer", self.search_data.original_performer)
        query.bindValue(":original_composer", self.search_data.original_composer)
        query.bindValue(":original_publisher", self.search_data.original_publisher)
        query.bindValue(":original_release_date", "")
        query.bindValue(":original_text_author", self.search_data.original_text_author)
        query.bindValue(":isrc", self.search_data.isrc)
        query.exec()
        self.query_model.setQuery(query)

    def updateHeaders(self):
        self.query_model.setHeaderData(0, Qt.Orientation.Horizontal, "ID")
        self.query_model.setHeaderData(1, Qt.Orientation.Horizontal, "Title")
        col = 2
        for key, val in config.items("Library Shown Parameters"):
            if val == 'True':
                self.query_model.setHeaderData(col, Qt.Orientation.Horizontal, header_title[key])
                col+=1
