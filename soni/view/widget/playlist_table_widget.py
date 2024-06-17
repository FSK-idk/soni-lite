from PySide6.QtWidgets import QWidget, QTableView, QAbstractItemView, QHeaderView
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt, QItemSelection

from model.playlist_table_model import PlaylistTableModel


class PlaylistTableWidget(QTableView):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.playlist_table_model = PlaylistTableModel()

        self.playlist_table_model.preupdated.connect(self.preupdatePlaylistTable)
        self.playlist_table_model.updated.connect(self.updatePlaylistTable)

        self.setSortingEnabled(True)
        self.setModel(self.playlist_table_model)
        self.horizontalHeader().setFont(QFont(":/fonts/NotoSans.ttf",10))
        self.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.verticalHeader().hide()
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.horizontalHeader().sortIndicatorChanged.connect(self.sort)

        self.selectionModel().selectionChanged.connect(self.onSelectionChanged)

    def sort(self, index: int, order: Qt.SortOrder) -> None:
        self.playlist_table_model.setSortData(order, index)
        self.playlist_table_model.updateTable()

    def onSelectionChanged(self, selected: QItemSelection, deselected: QItemSelection) -> None:
        if self.selectionModel().selectedRows():
            row = self.selectionModel().selectedRows()[0].row()
            self.playlist_table_model.setSelectedRow(row)

    # Need to save selection before update
    def preupdatePlaylistTable(self, row: int) -> None:
        self.temp_row = row

    def updatePlaylistTable(self) -> None:
        self.selectRow(self.temp_row)

    def search(self, search_data: str) -> None:
        self.playlist_table_model.setSearchData(search_data)
        self.playlist_table_model.updateTable()