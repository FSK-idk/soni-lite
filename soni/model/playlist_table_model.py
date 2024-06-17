from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, Signal
from PySide6.QtSql import QSqlQuery, QSqlQueryModel

from etc.data_base import data_base
from etc.query import Query


class PlaylistTableModel(QSqlQueryModel):
    preupdated = Signal(int)
    updated = Signal()

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.descending = False
        self.sort_column = 0
        self.search_data = ""

        self.selected_row = -1

        data_base.updatedPlaylistTable.connect(self.updateTable)
        data_base.updatedPlaylistTable.connect(self.updateHeader)

        self.updateTable()
        self.updateHeader()

    def setSelectedRow(self, row: int) -> None:
        self.selected_row = row

    def setSearchData(self, search_data: str) -> None:
        self.search_data = search_data

    def setSortData(self, order: Qt.SortOrder, sort_column: int) -> None:
        self.descending = (order != Qt.SortOrder.DescendingOrder)
        self.sort_column = sort_column

    def updateTable(self) -> None:
        self.preupdated.emit(self.selected_row)

        query = QSqlQuery(data_base.data_base)
        query.prepare(Query.selectPlaylistTable(self.descending, self.sort_column))
        query.bindValue(":name", self.search_data)
        query.exec()
        self.setQuery(query)

        self.updated.emit()

    def updateHeader(self) -> None:
        self.setHeaderData(0, Qt.Orientation.Horizontal, "ID")
        self.setHeaderData(1, Qt.Orientation.Horizontal, "Name")