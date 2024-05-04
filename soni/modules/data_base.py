from PySide6.QtSql import (
    QSqlDatabase,
    QSqlQuery
)

from modules.data_base_default import DataBaseDefault
from modules.data_base_query import DataBaseQuery


class DataBase():
    def __init__(self) -> None:
        self.data_base = QSqlDatabase("QSQLITE")
        self.data_base.setDatabaseName("./soni/data/library.sqlite")
        self.data_base.open()

        self.create_data_base()

    def create_data_base(self) -> None:
        # create tables

        QSqlQuery(DataBaseQuery.create_table_audio, self.data_base).exec()
        QSqlQuery(DataBaseQuery.create_table_album, self.data_base).exec()
        QSqlQuery(DataBaseQuery.create_table_genre, self.data_base).exec()
        QSqlQuery(DataBaseQuery.create_table_language, self.data_base).exec()
        QSqlQuery(DataBaseQuery.create_table_performer, self.data_base).exec()
        QSqlQuery(DataBaseQuery.create_table_composer, self.data_base).exec()
        QSqlQuery(DataBaseQuery.create_table_composer, self.data_base).exec()
        QSqlQuery(DataBaseQuery.create_table_modified_by, self.data_base).exec()
        QSqlQuery(DataBaseQuery.create_table_picture_mime_type, self.data_base).exec()
        QSqlQuery(DataBaseQuery.create_table_picture_artist, self.data_base).exec()
        QSqlQuery(DataBaseQuery.create_table_text_author, self.data_base).exec()
        QSqlQuery(DataBaseQuery.create_table_playlist, self.data_base).exec()

        # store default data

        query = QSqlQuery(self.data_base)
        query.prepare(DataBaseQuery.insert_genre)
        for name in DataBaseDefault.genres:
            query.bindValue(":name", name)
            query.exec()


        query = QSqlQuery(self.data_base)
        query.prepare(DataBaseQuery.insert_language)
        for code, name in DataBaseDefault.languages.items():
            query.bindValue(":name", name)
            query.bindValue(":code", code)
            query.exec()
        
        query = QSqlQuery(self.data_base)
        query.prepare(DataBaseQuery.insert_picture_mime_type)
        for type in DataBaseDefault.picture_mime_types:
            query.bindValue(":type", type)
            query.exec()