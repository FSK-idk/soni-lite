from PySide6.QtWidgets import QWidget


from view.default.v_box_layout_widget import VBoxLayoutWidget

from view.tile.search_line_edit_tile import SearchLineEditTile

from view.widget.playlist_table_widget import PlaylistTableWidget

class PlaylistPanelWidget(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        # widgets

        self.line = SearchLineEditTile(self)
        self.table = PlaylistTableWidget(self)

        self.line.setTitle("Name")
        self.line.clicked.connect(self.table.search)

        # layout

        self.main_layout = VBoxLayoutWidget()
        self.main_layout.addWidget(self.line)
        self.main_layout.addWidget(self.table)

        self.setLayout(self.main_layout)

    def updatePanel(self) -> None:
        self.table.updateTable()
