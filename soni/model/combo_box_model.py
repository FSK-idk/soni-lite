from PySide6.QtWidgets import QWidget
from PySide6.QtSql import QSqlQueryModel

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
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.descending = False
        self.table_name = ""

    def setOrder(self, descending: bool) -> None:
        self.descending = descending

    def setTable(self, table_name: str) -> None:
        self.table_name = table_name
        self.setQuery(select_query[self.table_name](self.descending), data_base.data_base)
    
    def updateTable(self) -> None:
        self.setQuery(select_query[self.table_name](self.descending), data_base.data_base)