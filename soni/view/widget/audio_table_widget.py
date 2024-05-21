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
)

from model.audio_data import AudioData
from model.audio_table_model import AudioTableModel


class AudioTableWidget(QTableView):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.audio_table_model = AudioTableModel()

        self.setSortingEnabled(True)
        self.setModel(self.audio_table_model.query_model)
        self.horizontalHeader().setFont(QFont(":/fonts/NotoSans.ttf",10))
        self.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.verticalHeader().hide()
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.horizontalHeader().sortIndicatorChanged.connect(self.sort)

    def search(self, search_data: AudioData):
        self.audio_table_model.setSearchData(search_data)
        self.audio_table_model.updateTable()

    def sort(self, index: int, order: Qt.SortOrder):
        self.audio_table_model.setSortData(order, index)
        self.audio_table_model.updateTable()

    def updateTable(self):
        self.audio_table_model.updateTable()
    
    def updateHeaders(self):
        self.audio_table_model.updateHeaders()
        self.audio_table_model.updateTable()
