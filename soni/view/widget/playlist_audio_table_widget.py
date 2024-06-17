from PySide6.QtWidgets import QWidget, QTableView, QAbstractItemView, QHeaderView
from PySide6.QtGui import QFont

from model.playlist_audio_table_model import PlaylistAudioTableModel


class PlaylistAudioTableWidget(QTableView):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        
        self.playlist_audio_table_model = PlaylistAudioTableModel()

        self.setModel(self.playlist_audio_table_model)
        self.horizontalHeader().setFont(QFont(":/fonts/NotoSans.ttf",10))
        self.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.verticalHeader().hide()
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)

    def setPlaylistId(self, id: int) -> None:
        self.playlist_audio_table_model.setPlaylistId(id)

    def setPlaylistName(self, name: str) -> None:
        self.playlist_audio_table_model.setPlaylistName(name)

    def moveUp(self) -> None:
        row = self.selectionModel().selectedRows()[0].row()
        self.playlist_audio_table_model.moveUp(self.selectionModel().selectedRows()[0].data())
        self.selectRow(row - 1)

    def moveDown(self) -> None:
        row = self.selectionModel().selectedRows()[0].row()
        self.playlist_audio_table_model.moveDown(self.selectionModel().selectedRows()[0].data())
        self.selectRow(row + 1)
