from PySide6.QtWidgets import (
    QWidget,
    QTableView,
    QAbstractItemView,
    QHeaderView,
)
from PySide6.QtGui import (
    QFont,
)
from PySide6.QtCore import (
    Qt,
    QSortFilterProxyModel,
)
from PySide6.QtSql import (
    QSqlQuery,
    QSqlQueryModel,
)

from model.data_base.data_base import data_base
from model.config import config
from model.data_base.query import Queries
from model.audio_info import AudioInfo

from view.default.v_box_layout_widget import VBoxLayoutWidget

header_titles = {
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

class AudioTableWidget(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        # attributes
        self.sort_data = (True, 0)
        self.info = AudioInfo()
    
        self.model = QSqlQueryModel(self)
        self.onTableUpdate()

        # widgets
        
        self.table = QTableView(self)
        self.table.setSortingEnabled(True)

        proxyModel =  QSortFilterProxyModel(self)

        proxyModel.setSourceModel(self.model)
        self.table.setModel(proxyModel)

        self.table.setModel(self.model)
        self.table.horizontalHeader().setFont(QFont(":/fonts/NotoSans.ttf",10))
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.verticalHeader().hide()
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.table.horizontalHeader().sortIndicatorChanged.connect(self.onSortIndicatorChanged)


        # layout

        self.main_layout = VBoxLayoutWidget()
        self.main_layout.addWidget(self.table)

        self.setLayout(self.main_layout)

    def onSearch(self, info: AudioInfo):
        self.info = info
        self.onTableUpdate()

    def onSortIndicatorChanged(self, logicalIndex: int, order: Qt.SortOrder):
        self.sort_data = (order != Qt.SortOrder.AscendingOrder, logicalIndex)
        self.onTableUpdate()

    def onTableUpdate(self):
        query = QSqlQuery(data_base.data_base)
        query.prepare(Queries.select_audio(self.info, self.sort_data[0], self.sort_data[1]))
        query.bindValue(":title", self.info.title)
        query.bindValue(":album_title", self.info.album_title)
        query.bindValue(":duration", "")
        query.bindValue(":genre", self.info.genre)
        query.bindValue(":language", "")
        query.bindValue(":rating", "")
        query.bindValue(":bpm", "")
        query.bindValue(":performer", self.info.performer)
        query.bindValue(":composer", self.info.composer)
        query.bindValue(":publisher", self.info.publisher)
        query.bindValue(":modified_by", self.info.modified_by)
        query.bindValue(":release_date", "")
        query.bindValue(":picture_artist", self.info.picture_artist)
        query.bindValue(":text_author", self.info.text_author)
        query.bindValue(":original_title", self.info.original_title)
        query.bindValue(":original_album_title", self.info.original_album_title)
        query.bindValue(":original_performer", self.info.original_performer)
        query.bindValue(":original_composer", self.info.original_composer)
        query.bindValue(":original_publisher", self.info.original_publisher)
        query.bindValue(":original_release_date", "")
        query.bindValue(":original_text_author", self.info.original_text_author)
        query.bindValue(":isrc", self.info.isrc)
        query.exec()
        self.model.setQuery(query)

    def onShownParametersChanged(self):
        self.onTableUpdate()
        self.model.setHeaderData(0, Qt.Orientation.Horizontal, "ID")
        self.model.setHeaderData(1, Qt.Orientation.Horizontal, "Title")
        col = 2
        for key, val in config.items("Library Shown Parameters"):
            if val == 'True':
                self.model.setHeaderData(col, Qt.Orientation.Horizontal, header_titles[key])
                col+=1
