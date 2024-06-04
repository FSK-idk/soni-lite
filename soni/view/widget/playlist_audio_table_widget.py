from PySide6.QtWidgets import (
    QWidget,
    QTableView,
    QAbstractItemView,
    QHeaderView
)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

from model.playlist_audio_table_model import PlaylistAudioTableModel


class PlaylistAudioTableWidget(QTableView):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        
        self.playlist_audio_table_model = PlaylistAudioTableModel()

        self.setSortingEnabled(True)
        self.setModel(self.playlist_audio_table_model)
        self.horizontalHeader().setFont(QFont(":/fonts/NotoSans.ttf",10))
        self.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.verticalHeader().hide()
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.horizontalHeader().sortIndicatorChanged.connect(self.sort)

    def sort(self, index: int, order: Qt.SortOrder) -> None:
        self.playlist_audio_table_model.setSortData(order, index)
        self.playlist_audio_table_model.updateTable()

    def setPlaylist(self, id: int) -> None:
        self.playlist_audio_table_model.setSearchData(id)
        self.playlist_audio_table_model.updateTable()

    def updateTable(self) -> None:
        self.playlist_audio_table_model.updateTable()
        self.playlist_audio_table_model.updateHeader()