from PySide6.QtWidgets import QWidget
from PySide6.QtSql import QSqlQueryModel
from PySide6.QtCore import Signal

from etc.data_base import data_base
from etc.query import Query


select_query = {
    "Genre": Query.selectGenreNames,
    "Performer": Query.selectPerformerNames,
    "Composer": Query.selectComposerNames,
    "Publisher": Query.selectPublisherNames,
    "ModifiedBy": Query.selectModifiedByNames,
    "PictureArtist": Query.selectPictureArtistNames,
    "TextAuthor": Query.selectTextAuthorNames,
    "Playlist": Query.selectPlaylistNames,
}


class ComboBoxModel(QSqlQueryModel):
    preupdated = Signal(str)
    updated = Signal()

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        data_base.updatedPlaylistTable.connect(self.updateTable)
        data_base.updatedAudioTable.connect(self.updateTable)

        self.descending = False
        self.table_name = ""
        self.text = ""

    def setText(self, text: str) -> None:
        self.text = text

    def setOrder(self, descending: bool) -> None:
        self.descending = descending

    def setTable(self, table_name: str) -> None:
        self.table_name = table_name
        self.updateTable()

    def updateTable(self) -> None:
        self.preupdated.emit(self.text)
        self.setQuery(select_query[self.table_name](self.descending), data_base.data_base)
        self.updated.emit()
