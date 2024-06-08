from PySide6.QtWidgets import (
    QWidget,
    QTableView,
    QAbstractItemView,
    QHeaderView
)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt, QItemSelectionModel

from model.playlist_table_model import PlaylistTableModel


class PlaylistTableWidget(QTableView):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.playlist_table_model = PlaylistTableModel()

        self.setSortingEnabled(True)
        self.setModel(self.playlist_table_model)
        self.horizontalHeader().setFont(QFont(":/fonts/NotoSans.ttf",10))
        self.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.verticalHeader().hide()
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.horizontalHeader().sortIndicatorChanged.connect(self.sort)

    def sort(self, index: int, order: Qt.SortOrder) -> None:
        self.playlist_table_model.setSortData(order, index)
        self.playlist_table_model.updateTable()

    def search(self, search_data: str) -> None:
        self.playlist_table_model.setSearchData(search_data)
        self.playlist_table_model.updateTable()

    def updateTable(self) -> None:
        flag, row = False, 0
        if self.selectionModel().selectedRows():
            row = self.selectionModel().selectedRows()[0].row()
            flag = True
    
        self.playlist_table_model.updateTable()
        self.playlist_table_model.updateHeader()
        
        if flag:
            self.selectRow(row)