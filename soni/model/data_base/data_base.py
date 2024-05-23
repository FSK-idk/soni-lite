import imghdr
import os
from typing import List

from PySide6.QtSql import (
    QSqlDatabase,
    QSqlQuery
)

from model.audio_data import AudioData
from model.data_base.data_base_default import DataBaseDefault
from model.data_base.query import Queries, info_attributes


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

    def select_album_id(self, name: str) -> int | None:
        query = QSqlQuery(self.data_base)
        query.prepare(Queries.select_album_id_one())
        query.bindValue(':name', name)
        query.exec()
        return query.value(0) if query.next() else None

    def insert_album(self, name: str) -> int:
        query = QSqlQuery(self.data_base)
        query.prepare(Queries.insert_album())
        query.bindValue(':name', name)
        query.exec()
        return query.lastInsertId()

    def select_genre_id(self, name: str) -> int | None:
        query = QSqlQuery(self.data_base)
        query.prepare(Queries.select_genre_id_one())
        query.bindValue(':name', name)
        query.exec()
        return query.value(0) if query.next() else None

    def select_performer_id(self, name: str) -> int | None:
        query = QSqlQuery(self.data_base)
        query.prepare(Queries.select_performer_id_one())
        query.bindValue(':name', name)
        query.exec()
        return query.value(0) if query.next() else None

    def insert_performer(self, name: str) -> int:
        query = QSqlQuery(self.data_base)
        query.prepare(Queries.insert_performer())
        query.bindValue(':name', name)
        query.exec()
        return query.lastInsertId()

    def select_composer_id(self, name: str) -> int | None:
        query = QSqlQuery(self.data_base)
        query.prepare(Queries.select_composer_id_one())
        query.bindValue(':name', name)
        query.exec()
        return query.value(0) if query.next() else None

    def insert_composer(self, name: str) -> int:
        query = QSqlQuery(self.data_base)
        query.prepare(Queries.insert_composer())
        query.bindValue(':name', name)
        query.exec()
        return query.lastInsertId()

    def select_publisher_id(self, name: str) -> int | None:
        query = QSqlQuery(self.data_base)
        query.prepare(Queries.select_publisher_id_one())
        query.bindValue(':name', name)
        query.exec()
        return query.value(0) if query.next() else None

    def insert_publisher(self, name: str) -> int:
        query = QSqlQuery(self.data_base)
        query.prepare(Queries.insert_publisher())
        query.bindValue(':name', name)
        query.exec()
        return query.lastInsertId()

    def select_modified_by_id(self, name: str) -> int | None:
        query = QSqlQuery(self.data_base)
        query.prepare(Queries.select_modified_by_id_one())
        query.bindValue(':name', name)
        query.exec()
        return query.value(0) if query.next() else None

    def insert_modified_by(self, name: str) -> int:
        query = QSqlQuery(self.data_base)
        query.prepare(Queries.insert_modified_by())
        query.bindValue(':name', name)
        query.exec()
        return query.lastInsertId()

    def select_picture_mime_type_id(self, type: str) -> int | None:
        query = QSqlQuery(self.data_base)
        query.prepare(Queries.select_picture_mime_type_id_one())
        query.bindValue(':type', type)
        query.exec()
        return query.value(0) if query.next() else None

    def select_picture_artist_id(self, name: str) -> int | None:
        query = QSqlQuery(self.data_base)
        query.prepare(Queries.select_picture_artist_id_one())
        query.bindValue(':name', name)
        query.exec()
        return query.value(0) if query.next() else None

    def insert_picture_artist(self, name: str) -> int:
        query = QSqlQuery(self.data_base)
        query.prepare(Queries.insert_picture_artist())
        query.bindValue(':name', name)
        query.exec()
        return query.lastInsertId()

    def select_text_author_id(self, name: str) -> int | None:
        query = QSqlQuery(self.data_base)
        query.prepare(Queries.select_text_author_id_one())
        query.bindValue(':name', name)
        query.exec()
        return query.value(0) if query.next() else None

    def insert_text_author(self, name: str) -> int:
        query = QSqlQuery(self.data_base)
        query.prepare(Queries.insert_text_author())
        query.bindValue(':name', name)
        query.exec()
        return query.lastInsertId()

    def insert_audio(self, info: AudioData) -> None:
        filepath = None
        if info.filepath != "":
            filepath = info.filepath

        album_id = None
        if info.album_title != "":
            album_id = self.select_album_id(info.album_title)
            if album_id == None:
                album_id = self.insert_album(info.album_title)

        genre_id = None
        if info.genre != "":
            genre_id = self.select_genre_id(info.genre)

        performer_id = None
        if info.performer != "":
            performer_id = self.select_performer_id(info.performer)
            if performer_id == None:
                performer_id = self.insert_performer(info.performer)

        composer_id = None
        if info.composer != "":
            composer_id = self.select_composer_id(info.composer)
            if composer_id == None:
                composer_id = self.insert_composer(info.composer)

        publisher_id = None
        if info.publisher != "":
            publisher_id = self.select_publisher_id(info.publisher)
            if publisher_id == None:
                publisher_id = self.insert_publisher(info.publisher)

        modified_by_id = None
        if info.modified_by != "":
            modified_by_id = self.select_modified_by_id(info.modified_by)
            if modified_by_id == None:
                modified_by_id = self.insert_modified_by(info.modified_by)

        picture = None
        if os.path.isfile(info.picture_filepath):
            with open(info.picture_filepath, 'rb') as file:
                picture = file.read()

        picture_mime_type_id = None
        if os.path.isfile(info.picture_filepath):
            type = imghdr.what(info.picture_filepath)
            if type:
                picture_mime_type_id = self.select_picture_mime_type_id(type)

        picture_artist_id = None
        if info.picture_artist != "":
            picture_artist_id = self.select_picture_artist_id(info.picture_artist)
            if picture_artist_id == None:
                picture_artist_id = self.insert_picture_artist(info.picture_artist)

        text_author_id = None
        if info.text_author != "":
            text_author_id = self.select_text_author_id(info.text_author)
            if text_author_id == None:
                text_author_id = self.insert_text_author(info.text_author)

        original_album_id = None
        if info.original_album_title != "":
            original_album_id = self.select_album_id(info.original_album_title)
            if album_id == None:
                original_album_id = self.insert_album(info.original_album_title)

        original_performer_id = None
        if info.original_performer != "":
            original_performer_id = self.select_performer_id(info.original_performer)
            if original_performer_id == None:
                original_performer_id = self.insert_performer(info.original_performer)

        original_composer_id = None
        if info.original_composer != "":
            original_composer_id = self.select_composer_id(info.original_composer)
            if original_composer_id == None:
                original_composer_id = self.insert_composer(info.original_composer)

        original_publisher_id = None
        if info.original_publisher != "":
            original_publisher_id = self.select_publisher_id(info.original_publisher)
            if original_publisher_id == None:
                original_publisher_id = self.insert_publisher(info.original_publisher)

        original_text_author_id = None
        if info.publisher != "":
            original_text_author_id = self.select_text_author_id(info.original_text_author)
            if original_text_author_id == None:
                original_text_author_id = self.insert_text_author(info.original_text_author)

        isrc = None
        if info.isrc != "":
            isrc = info.isrc

        query = QSqlQuery(self.data_base)
        query.prepare(Queries.insert_audio())

        query.bindValue(':filepath', filepath)
        query.bindValue(':title', info.title)
        query.bindValue(':album_id', album_id)
        query.bindValue(':duration', None)
        query.bindValue(':genre_id', genre_id)
        query.bindValue(':language_id', None)
        query.bindValue(':rating', None)
        query.bindValue(':bpm', None)
        query.bindValue(':performer_id', performer_id)
        query.bindValue(':composer_id', composer_id)
        query.bindValue(':publisher_id', publisher_id)
        query.bindValue(':modified_by_id', modified_by_id)
        query.bindValue(':release_date', None)
        query.bindValue(':copyright', None)
        query.bindValue(':comments', None)
        query.bindValue(':picture', picture)
        query.bindValue(':picture_mime_type_id', picture_mime_type_id)
        query.bindValue(':picture_artist_id', picture_artist_id)
        query.bindValue(':text', info.text)
        query.bindValue(':text_author_id', text_author_id)
        query.bindValue(':original_title', info.original_title)
        query.bindValue(':original_album_id', original_album_id)
        query.bindValue(':original_performer_id', original_performer_id)
        query.bindValue(':original_composer_id', original_composer_id)
        query.bindValue(':original_publisher_id', original_publisher_id)
        query.bindValue(':original_release_date', None)
        query.bindValue(':original_text_author_id', original_text_author_id)
        query.bindValue(':isrc', isrc)
        query.bindValue(':website', None)
        query.bindValue(':copyright_website', None)

        query.exec()

    def query_select_all(self, table_name: str, attributes: List[str]) -> QSqlQuery:
        query = QSqlQuery(self.data_base)
        query.prepare(f"SELECT {', '.join(attributes)} FROM {table_name}")
        query.exec()
        return query

    def get_audio(self, id : int) -> AudioData:
        query = QSqlQuery(self.data_base)
        query.prepare(Queries.select_one_audio())
        query.bindValue(':id', id)
        query.exec()

        audio_data = AudioData()

        rec = query.record()

        if query.next():
            row = [query.value(index) for index in range(rec.count())]
            audio_data.setData(row)
        
        return audio_data

    def update_audio(self, audio_data : AudioData) -> None:
        print('updating')
        
        # TODO: update other tables


        # TODO: update audio table


data_base = DataBase()