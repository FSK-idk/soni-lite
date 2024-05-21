import imghdr
import os
from typing import List

from PySide6.QtSql import (
    QSqlDatabase,
    QSqlQuery
)

from model.audio_info import AudioInfo
from model.data_base.data_base_default import DataBaseDefault
from model.data_base.query import Queries


class DataBase():
    def init(self) -> None:
        self.data_base = QSqlDatabase('QSQLITE')
        self.data_base.setDatabaseName("./soni/data/library.sqlite")
        self.data_base.open()

        self.create_data_base()

    def create_data_base(self) -> None:
        # create tables

        QSqlQuery(Queries.create_table_audio(), self.data_base).exec()
        QSqlQuery(Queries.create_table_album(), self.data_base).exec()
        QSqlQuery(Queries.create_table_genre(), self.data_base).exec()
        QSqlQuery(Queries.create_table_language(), self.data_base).exec()
        QSqlQuery(Queries.create_table_performer(), self.data_base).exec()
        QSqlQuery(Queries.create_table_composer(), self.data_base).exec()
        QSqlQuery(Queries.create_table_publisher(), self.data_base).exec()
        QSqlQuery(Queries.create_table_modified_by(), self.data_base).exec()
        QSqlQuery(Queries.create_table_picture_mime_type(), self.data_base).exec()
        QSqlQuery(Queries.create_table_picture_artist(), self.data_base).exec()
        QSqlQuery(Queries.create_table_text_author(), self.data_base).exec()
        QSqlQuery(Queries.create_table_playlist(), self.data_base).exec()
        QSqlQuery(Queries.create_table_playlist_audio(), self.data_base).exec()

        # store default data

        query = QSqlQuery(self.data_base)
        query.prepare(Queries.insert_genre())
        for name in DataBaseDefault.genres:
            query.bindValue(':name', name)
            query.exec()


        query = QSqlQuery(self.data_base)
        query.prepare(Queries.insert_language())
        for code, name in DataBaseDefault.languages.items():
            query.bindValue(':name', name)
            query.bindValue(':code', code)
            query.exec()
        
        query = QSqlQuery(self.data_base)
        query.prepare(Queries.insert_picture_mime_type())
        for type in DataBaseDefault.picture_mime_types:
            query.bindValue(':type', type)
            query.exec()

    def select_album(self, name: str) -> int | None:
        if name == "":
            return None
        
        query = QSqlQuery(self.data_base)
        query.prepare(Queries.select_album_id)
        query.bindValue(':name', name)
        query.exec()
        
        if query.next():
            return query.value(0)
        else:
            query = QSqlQuery(self.data_base)
            query.prepare(Queries.insert_album())
            query.bindValue(':name', name)
            query.exec()
            return query.lastInsertId()

    def select_genre(self, name: str) -> int | None:
        if name == "":
            return None
        
        query = QSqlQuery(self.data_base)
        query.prepare(Queries.select_genre_id)
        query.bindValue(':name', name)
        query.exec()
        
        if query.next():
            return query.value(0)
        else:
            return None
        
    def select_performer(self, name: str) -> int | None:
        if name == "":
            return None
        
        query = QSqlQuery(self.data_base)
        query.prepare(Queries.select_performer_id)
        query.bindValue(':name', name)
        query.exec()
        
        if query.next():
            return query.value(0)
        else:
            query = QSqlQuery(self.data_base)
            query.prepare(Queries.insert_performer())
            query.bindValue(':name', name)
            query.exec()
            return query.lastInsertId()
        
    def select_composer(self, name: str) -> int | None:
        if name == "":
            return None
        
        query = QSqlQuery(self.data_base)
        query.prepare(Queries.select_composer_id)
        query.bindValue(':name', name)
        query.exec()
        
        if query.next():
            return query.value(0)
        else:
            query = QSqlQuery(self.data_base)
            query.prepare(Queries.insert_composer())
            query.bindValue(':name', name)
            query.exec()
            return query.lastInsertId()
        
    def select_publisher(self, name: str) -> int | None:
        if name == "":
            return None
        
        query = QSqlQuery(self.data_base)
        query.prepare(Queries.select_publisher_id)
        query.bindValue(':name', name)
        query.exec()
        
        if query.next():
            return query.value(0)
        else:
            query = QSqlQuery(self.data_base)
            query.prepare(Queries.insert_publisher())
            query.bindValue(':name', name)
            query.exec()
            return query.lastInsertId()
        
    def select_modified_by(self, name: str) -> int | None:
        if name == "":
            return None
        
        query = QSqlQuery(self.data_base)
        query.prepare(Queries.select_modified_by_id)
        query.bindValue(':name', name)
        query.exec()
        
        if query.next():
            return query.value(0)
        else:
            query = QSqlQuery(self.data_base)
            query.prepare(Queries.insert_modified_by())
            query.bindValue(':name', name)
            query.exec()
            return query.lastInsertId()

    def select_blob(self, filepath):
        if not os.path.isfile(filepath):
            return None
        
        with open(filepath, 'rb') as file:
            blob_data = file.read()
        return blob_data

    def select_picture_mime_type(self, filepath):
        if not os.path.isfile(filepath):
            return None

        type = imghdr.what(filepath)

        query = QSqlQuery(self.data_base)
        query.prepare(Queries.select_picture_mime_type_id)
        query.bindValue(':type', type)
        query.exec()
        
        if query.next():
            return query.value(0)
        else:
            return None

    def select_picture_artist(self, name: str) -> int | None:
        if name == "":
            return None
        
        query = QSqlQuery(self.data_base)
        query.prepare(Queries.select_picture_artist_id)
        query.bindValue(':name', name)
        query.exec()
        
        if query.next():
            return query.value(0)
        else:
            query = QSqlQuery(self.data_base)
            query.prepare(Queries.insert_picture_artist())
            query.bindValue(':name', name)
            query.exec()
            return query.lastInsertId()

    def select_text_author(self, name: str) -> int | None:
        if name == "":
            return None
        
        query = QSqlQuery(self.data_base)
        query.prepare(Queries.select_text_author_id)
        query.bindValue(':name', name)
        query.exec()
        
        if query.next():
            return query.value(0)
        else:
            query = QSqlQuery(self.data_base)
            query.prepare(Queries.insert_text_author())
            query.bindValue(':name', name)
            query.exec()
            return query.lastInsertId()
        
    def insert_audio(self, info: AudioInfo) -> None:
        query = QSqlQuery(self.data_base)
        query.prepare(Queries.insert_audio)

        query.bindValue(':filepath', info.filepath)
        query.bindValue(':title', info.title)
        query.bindValue(':album_id', self.select_album(info.album_title))
        query.bindValue(':duration', None)
        query.bindValue(':genre_id', self.select_genre(info.genre))
        query.bindValue(':language_id', None)
        query.bindValue(':rating', None)
        query.bindValue(':bpm', None)
        query.bindValue(':performer_id', self.select_performer(info.performer))
        query.bindValue(':composer_id', self.select_composer(info.composer))
        query.bindValue(':publisher_id', self.select_publisher(info.publisher))
        query.bindValue(':modified_by_id', self.select_modified_by(info.modified_by))
        query.bindValue(':release_date', None)
        query.bindValue(':copyright', None)
        query.bindValue(':comments', None)
        query.bindValue(':picture', self.select_blob(info.picture_filepath))
        query.bindValue(':picture_mime_type_id', self.select_picture_mime_type(info.picture_filepath))
        query.bindValue(':picture_artist_id', self.select_picture_artist(info.picture_artist))
        query.bindValue(':text', info.text)
        query.bindValue(':text_author_id', self.select_text_author(info.text_author))
        query.bindValue(':original_title', info.original_title)
        query.bindValue(':original_album_id', self.select_album(info.original_album_title))
        query.bindValue(':original_performer_id', self.select_performer(info.original_performer))
        query.bindValue(':original_composer_id', self.select_composer(info.original_composer))
        query.bindValue(':original_publisher_id', self.select_publisher(info.original_publisher))
        query.bindValue(':original_release_date', None)
        query.bindValue(':original_text_author_id', self.select_text_author(info.original_text_author))
        query.bindValue(':isrc', info.isrc if info.isrc != "" else None)
        query.bindValue(':website', None)
        query.bindValue(':copyright_website', None)

        query.exec()

    def search(self, info: AudioInfo) -> None:
        pass

    def query_select_all(self, table_name: str, attributes: List[str]) -> QSqlQuery:
        query = QSqlQuery(self.data_base)
        query.prepare(f"SELECT {', '.join(attributes)} FROM {table_name}")
        query.exec()
        return query

data_base = DataBase()