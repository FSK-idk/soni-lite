from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QHBoxLayout,
    QVBoxLayout,
    QStackedLayout,
    QSlider,
    QWidget,
    QLabel,
    QPushButton,
    QSizePolicy,
    QMenuBar,
    QTableView,
    QScrollArea,
    QDialog,
    QAbstractItemView,
    QHeaderView,
    QLineEdit,
    QStyledItemDelegate,
)
from PySide6.QtGui import (
    QScreen,
    QAction,
    QFont,
)
from PySide6.QtCore import (
    Qt,
    QSortFilterProxyModel,
    Signal
)
from PySide6.QtSql import (
    QSqlTableModel,
    QSqlRelationalTableModel,
    QSqlRelation,
    QSqlQuery,
    QSqlQueryModel,
)

from modules.data_base import data_base
from modules.config import config
from modules.query import Queries

from ui.dialogs.new_audio_dialog import NewAudioDialog
from ui.dialogs.modify_audio_dialog import ModifyAudioDialog

from ui.widgets.pyside.push_button_widget import PushButtonWidget
from ui.widgets.pyside.v_box_layout_widget import VBoxLayoutWidget
from ui.widgets.pyside.h_box_layout_widget import HBoxLayoutWidget

from ui.widgets.search_info_panel_widget import SearchInfoPanelWidget

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
    
        self.model = QSqlQueryModel(self)
        query = QSqlQuery(Queries.select_audio(), data_base.data_base)
        self.model.setQuery(query)

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

        self.sort_data = (True, 0)

        # layout

        self.main_layout = VBoxLayoutWidget()
        self.main_layout.addWidget(self.table)

        self.setLayout(self.main_layout)

    def onSortIndicatorChanged(self, logicalIndex: int, order: Qt.SortOrder):
        self.sort_data = (order != Qt.SortOrder.AscendingOrder, logicalIndex)
        self.onTableUpdate()

    def onTableUpdate(self):
        query = QSqlQuery(Queries.select_audio(self.sort_data[0], self.sort_data[1]), data_base.data_base)
        self.model.setQuery(query)

    def onShownParametersChanged(self):
        query = QSqlQuery(Queries.select_audio(), data_base.data_base)
        self.model.setQuery(query)
        self.model.setHeaderData(0, Qt.Orientation.Horizontal, "ID")
        self.model.setHeaderData(1, Qt.Orientation.Horizontal, "Title")
        col = 2
        for key, val in config.items("Library Shown Parameters"):
            if val == 'True':
                self.model.setHeaderData(col, Qt.Orientation.Horizontal, header_titles[key])
                col+=1
