from PySide6.QtWidgets import QWidget, QTableView, QAbstractItemView, QHeaderView
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

from etc.audio_data import AudioData
from model.audio_table_model import AudioTableModel


class AudioTableWidget(QTableView):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.audio_table_model = AudioTableModel()

        self.setSortingEnabled(True)
        self.setModel(self.audio_table_model)
        self.horizontalHeader().setFont(QFont(":/fonts/NotoSans.ttf",10))
        self.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.verticalHeader().hide()
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.horizontalHeader().sortIndicatorChanged.connect(self.sort)

    def sort(self, index: int, order: Qt.SortOrder) -> None:
        self.audio_table_model.setSortData(order, index)
        self.audio_table_model.updateTable()

    def search(self, search_data: AudioData) -> None:
        self.audio_table_model.setSearchData(search_data)
        self.audio_table_model.updateTable()

    def updateTable(self) -> None:
        self.audio_table_model.updateTable()
        self.audio_table_model.updateHeader()
