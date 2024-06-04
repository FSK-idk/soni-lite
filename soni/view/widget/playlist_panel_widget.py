from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, QModelIndex

from view.basic.v_box_layout_widget import VBoxLayoutWidget

from view.tile.push_line_edit_tile import PushLineEditTile

from view.widget.playlist_table_widget import PlaylistTableWidget


class PlaylistPanelWidget(QWidget):
    changedPlaylist = Signal(int)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.line = PushLineEditTile(self)
        self.playlist_table = PlaylistTableWidget(self)

        self.line.setTitle("Name")
        self.line.setButtonText("...")
        self.line.clicked.connect(self.playlist_table.search)
        self.playlist_table.selectionModel().currentRowChanged.connect(self.onChangedRow)

        self.main_layout = VBoxLayoutWidget()
        self.main_layout.addWidget(self.line)
        self.main_layout.addWidget(self.playlist_table)

        self.setLayout(self.main_layout)

    def onChangedRow(self, cur: QModelIndex, prev: QModelIndex) -> None:
        idx = self.playlist_table.model().index(cur.row(), 0)
        self.changedPlaylist.emit(self.playlist_table.model().data(idx))

    def updatePanel(self) -> None:
        self.playlist_table.updateTable()