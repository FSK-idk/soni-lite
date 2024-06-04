import os

from PySide6.QtGui import QPixmap
from PySide6.QtCore import QByteArray, QBuffer, Qt, QIODevice
from PySide6.QtSql import (
    QSqlDatabase,
    QSqlQuery
)

from etc.audio_data import AudioData
from etc.table_default import TableDefault
from etc.query import Query


class DataBase():
    def init(self) -> None:
        self.data_base = QSqlDatabase("QSQLITE")
        self.data_base.setDatabaseName("./soni/data/library.sqlite")
        self.data_base.open()

        self.createTables()

    def createTables(self) -> None:

        QSqlQuery(Query.createAudioTable(), self.data_base).exec()
        QSqlQuery(Query.createAlbumTable(), self.data_base).exec()
        QSqlQuery(Query.createGenreTable(), self.data_base).exec()
        QSqlQuery(Query.createPerformerTable(), self.data_base).exec()
        QSqlQuery(Query.createComposerTable(), self.data_base).exec()
        QSqlQuery(Query.createPublisherTable(), self.data_base).exec()
        QSqlQuery(Query.createModifiedByTable(), self.data_base).exec()
        QSqlQuery(Query.createPictureArtistTable(), self.data_base).exec()
        QSqlQuery(Query.createTextAuthorTable(), self.data_base).exec()
        QSqlQuery(Query.createPlaylistTable(), self.data_base).exec()
        QSqlQuery(Query.createPlaylistAudioTable(), self.data_base).exec()

        query = QSqlQuery(self.data_base)
        query.prepare(Query.insertGenre())
        for name in TableDefault.genres:
            query.bindValue(":name", name)
            query.exec()

    def insertAudio(self, audio_data: AudioData) -> None:
        filepath = None
        if audio_data.filepath != "":
            filepath = audio_data.filepath

        album_id = None
        if audio_data.album_name != "":
            query = QSqlQuery(self.data_base)
            query.prepare(Query.selectAlbumId())
            query.bindValue(":name", audio_data.album_name)
            query.exec()
            album_id = query.value(0) if query.next() else None
            if album_id == None:
                query = QSqlQuery(self.data_base)
                query.prepare(Query.insertAlbum())
                query.bindValue(":name", audio_data.album_name)
                query.exec()
                album_id = query.lastInsertId()

        genre_id = None
        if audio_data.genre_name != "":
            query = QSqlQuery(self.data_base)
            query.prepare(Query.selectGenreId())
            query.bindValue(":name", audio_data.genre_name)
            query.exec()
            genre_id = query.value(0) if query.next() else None

        performer_id = None
        if audio_data.performer_name != "":
            query = QSqlQuery(self.data_base)
            query.prepare(Query.selectPerformerId())
            query.bindValue(":name", audio_data.performer_name)
            query.exec()
            performer_id = query.value(0) if query.next() else None
            if performer_id == None:
                query = QSqlQuery(self.data_base)
                query.prepare(Query.insertPerformer())
                query.bindValue(":name", audio_data.performer_name)
                query.exec()
                performer_id = query.lastInsertId()

        composer_id = None
        if audio_data.composer_name != "":
            query = QSqlQuery(self.data_base)
            query.prepare(Query.selectComposerId())
            query.bindValue(":name", audio_data.composer_name)
            query.exec()
            composer_id = query.value(0) if query.next() else None
            if composer_id == None:
                query = QSqlQuery(self.data_base)
                query.prepare(Query.insertComposer())
                query.bindValue(":name", audio_data.composer_name)
                query.exec()
                composer_id = query.lastInsertId()

        publisher_id = None
        if audio_data.publisher_name != "":
            query = QSqlQuery(self.data_base)
            query.prepare(Query.selectPublisherId())
            query.bindValue(":name", audio_data.publisher_name)
            query.exec()
            publisher_id =  query.value(0) if query.next() else None
            if publisher_id == None:
                query = QSqlQuery(self.data_base)
                query.prepare(Query.insertPublisher())
                query.bindValue(":name", audio_data.publisher_name)
                query.exec()
                publisher_id = query.lastInsertId()

        modified_by_id = None
        if audio_data.modified_by_name != "":
            query = QSqlQuery(self.data_base)
            query.prepare(Query.selectModifiedById())
            query.bindValue(":name", audio_data.modified_by_name)
            query.exec()
            modified_by_id = query.value(0) if query.next() else None

            if modified_by_id == None:
                query = QSqlQuery(self.data_base)
                query.prepare(Query.insertModifiedBy())
                query.bindValue(":name", audio_data.modified_by_name)
                query.exec()
                modified_by_id = query.lastInsertId()

        picture_png = QByteArray()
        if os.path.isfile(audio_data.picture_filepath):
            pixmap = QPixmap(audio_data.picture_filepath)
            picture_png = QByteArray()
            buffer = QBuffer(picture_png)
            buffer.open( QIODevice.OpenModeFlag.WriteOnly)
            pixmap.save( buffer, "PNG" )

        picture_artist_id = None
        if audio_data.picture_artist_name != "":
            query = QSqlQuery(self.data_base)
            query.prepare(Query.selectPictureArtistId())
            query.bindValue(":name", audio_data.picture_artist_name)
            query.exec()
            picture_artist_id = query.value(0) if query.next() else None
            if picture_artist_id == None:
                query = QSqlQuery(self.data_base)
                query.prepare(Query.insertPictureArtist())
                query.bindValue(":name", audio_data.picture_artist_name)
                query.exec()
                return query.lastInsertId()

        text = None
        if audio_data.text != "":
            text = audio_data.text

        text_author_id = None
        if audio_data.text_author_name != "":
            query = QSqlQuery(self.data_base)
            query.prepare(Query.selectTextAuthorId())
            query.bindValue(":name", audio_data.text_author_name)
            query.exec()
            text_author_id =  query.value(0) if query.next() else None
            if text_author_id == None:
                query = QSqlQuery(self.data_base)
                query.prepare(Query.insertTextAuthor())
                query.bindValue(":name", audio_data.text_author_name)
                query.exec()
                text_author_id = query.lastInsertId()


        query = QSqlQuery(self.data_base)
        query.prepare(Query.insertAudio())
        query.bindValue(":name", audio_data.name)
        query.bindValue(":filepath", filepath)
        query.bindValue(":album_id", album_id)
        query.bindValue(":genre_id", genre_id)
        query.bindValue(":performer_id", performer_id)
        query.bindValue(":composer_id", composer_id)
        query.bindValue(":publisher_id", publisher_id)
        query.bindValue(":modified_by_id", modified_by_id)
        query.bindValue(":picture_png", picture_png)
        query.bindValue(":picture_artist_id", picture_artist_id)
        query.bindValue(":text", text)
        query.bindValue(":text_author_id", text_author_id)
        query.exec()

    def selectAudioData(self, id: str) -> AudioData:
        query = QSqlQuery(self.data_base)
        query.prepare(Query.selectAudioData())
        query.bindValue(":id", id)
        query.exec()

        audio_data = AudioData()
        rec = query.record()
        if query.next():
            row = [query.value(index) for index in range(rec.count())]
            audio_data.setData(row)

        return audio_data

    def updateAudio(self, audio_data: AudioData) -> None:
        filepath = None
        if audio_data.filepath != "":
            filepath = audio_data.filepath

        album_id = None
        if audio_data.album_name != "":
            query = QSqlQuery(self.data_base)
            query.prepare(Query.selectAlbumId())
            query.bindValue(":name", audio_data.album_name)
            query.exec()
            album_id = query.value(0) if query.next() else None
            if album_id == None:
                query = QSqlQuery(self.data_base)
                query.prepare(Query.insertAlbum())
                query.bindValue(":name", audio_data.album_name)
                query.exec()
                album_id = query.lastInsertId()

        genre_id = None
        if audio_data.genre_name != "":
            query = QSqlQuery(self.data_base)
            query.prepare(Query.selectGenreId())
            query.bindValue(":name", audio_data.genre_name)
            query.exec()
            genre_id = query.value(0) if query.next() else None

        performer_id = None
        if audio_data.performer_name != "":
            query = QSqlQuery(self.data_base)
            query.prepare(Query.selectPerformerId())
            query.bindValue(":name", audio_data.performer_name)
            query.exec()
            performer_id = query.value(0) if query.next() else None
            if performer_id == None:
                query = QSqlQuery(self.data_base)
                query.prepare(Query.insertPerformer())
                query.bindValue(":name", audio_data.performer_name)
                query.exec()
                performer_id = query.lastInsertId()

        composer_id = None
        if audio_data.composer_name != "":
            query = QSqlQuery(self.data_base)
            query.prepare(Query.selectComposerId())
            query.bindValue(":name", audio_data.composer_name)
            query.exec()
            composer_id = query.value(0) if query.next() else None
            if composer_id == None:
                query = QSqlQuery(self.data_base)
                query.prepare(Query.insertComposer())
                query.bindValue(":name", audio_data.composer_name)
                query.exec()
                composer_id = query.lastInsertId()

        publisher_id = None
        if audio_data.publisher_name != "":
            query = QSqlQuery(self.data_base)
            query.prepare(Query.selectPublisherId())
            query.bindValue(":name", audio_data.publisher_name)
            query.exec()
            publisher_id =  query.value(0) if query.next() else None
            if publisher_id == None:
                query = QSqlQuery(self.data_base)
                query.prepare(Query.insertPublisher())
                query.bindValue(":name", audio_data.publisher_name)
                query.exec()
                publisher_id = query.lastInsertId()

        modified_by_id = None
        if audio_data.modified_by_name != "":
            query = QSqlQuery(self.data_base)
            query.prepare(Query.selectModifiedById())
            query.bindValue(":name", audio_data.modified_by_name)
            query.exec()
            modified_by_id = query.value(0) if query.next() else None

            if modified_by_id == None:
                query = QSqlQuery(self.data_base)
                query.prepare(Query.insertModifiedBy())
                query.bindValue(":name", audio_data.modified_by_name)
                query.exec()
                modified_by_id = query.lastInsertId()

        picture_png = QByteArray()
        if os.path.isfile(audio_data.picture_filepath):
            pixmap = QPixmap(audio_data.picture_filepath)
            buffer = QBuffer(picture_png)
            buffer.open(QIODevice.OpenModeFlag.WriteOnly)
            pixmap.save(buffer, "PNG")

        picture_artist_id = None
        if audio_data.picture_artist_name != "":
            query = QSqlQuery(self.data_base)
            query.prepare(Query.selectPictureArtistId())
            query.bindValue(":name", audio_data.picture_artist_name)
            query.exec()
            picture_artist_id = query.value(0) if query.next() else None
            if picture_artist_id == None:
                query = QSqlQuery(self.data_base)
                query.prepare(Query.insertPictureArtist())
                query.bindValue(":name", audio_data.picture_artist_name)
                query.exec()
                return query.lastInsertId()

        text = None
        if audio_data.text != "":
            text = audio_data.text

        text_author_id = None
        if audio_data.text_author_name != "":
            query = QSqlQuery(self.data_base)
            query.prepare(Query.selectTextAuthorId())
            query.bindValue(":name", audio_data.text_author_name)
            query.exec()
            text_author_id =  query.value(0) if query.next() else None
            if text_author_id == None:
                query = QSqlQuery(self.data_base)
                query.prepare(Query.insertTextAuthor())
                query.bindValue(":name", audio_data.text_author_name)
                query.exec()
                text_author_id = query.lastInsertId()

        query = QSqlQuery(self.data_base)
        query.prepare(Query.updateAudio())
        query.bindValue(":name", audio_data.name)
        query.bindValue(":filepath", filepath)
        query.bindValue(":album_id", album_id)
        query.bindValue(":genre_id", genre_id)
        query.bindValue(":performer_id", performer_id)
        query.bindValue(":composer_id", composer_id)
        query.bindValue(":publisher_id", publisher_id)
        query.bindValue(":modified_by_id", modified_by_id)
        query.bindValue(":picture_png", picture_png)
        query.bindValue(":picture_artist_id", picture_artist_id)
        query.bindValue(":text", text)
        query.bindValue(":text_author_id", text_author_id)
        query.bindValue(":id", audio_data.id)
        query.exec()

        self.shrink()

    def deleteAudio(self, id: int) -> None:
        query = QSqlQuery(self.data_base)
        query.prepare(Query.deleteAudio())
        query.bindValue(":id", id)
        query.exec()
        self.shrink()

    def shrink(self):
        query = QSqlQuery(self.data_base)
        query.prepare(Query.selectUnusedAlbumIds())
        query.exec()
        id = []
        while query.next():
            id.append(query.value(0))
        if id:
            query = QSqlQuery(self.data_base)
            query.prepare(Query.deleteAlbums(len(id)))
            for i in id:
                query.addBindValue(i)
            query.exec()


        query = QSqlQuery(self.data_base)
        query.prepare(Query.selectUnusedPerformerIds())
        query.exec()
        id = []
        while query.next():
            id.append(query.value(0))
        if id:
            query = QSqlQuery(self.data_base)
            query.prepare(Query.deletePerformers(len(id)))
            for i in id:
                query.addBindValue(i)
            query.exec()


        query = QSqlQuery(self.data_base)
        query.prepare(Query.selectUnusedComposerIds())
        query.exec()
        id = []
        while query.next():
            id.append(query.value(0))
        if id:
            query = QSqlQuery(self.data_base)
            query.prepare(Query.deleteComposers(len(id)))
            for i in id:
                query.addBindValue(i)
            query.exec()


        query = QSqlQuery(self.data_base)
        query.prepare(Query.selectUnusedPublisherIds())
        query.exec()
        id = []
        while query.next():
            id.append(query.value(0))
        if id:
            query = QSqlQuery(self.data_base)
            query.prepare(Query.deletePublishers(len(id)))
            for i in id:
                query.addBindValue(i)
            query.exec()


        query = QSqlQuery(self.data_base)
        query.prepare(Query.selectUnusedModifiedByIds())
        query.exec()
        id = []
        while query.next():
            id.append(query.value(0))
        if id:
            query = QSqlQuery(self.data_base)
            query.prepare(Query.deleteModifiedBys(len(id)))
            for i in id:
                query.addBindValue(i)
            query.exec()


        query = QSqlQuery(self.data_base)
        query.prepare(Query.selectUnusedPictureArtistIds())
        query.exec()
        id = []
        while query.next():
            id.append(query.value(0))
        if id:
            query = QSqlQuery(self.data_base)
            query.prepare(Query.deletePictureArtists(len(id)))
            for i in id:
                query.addBindValue(i)
            query.exec()


        query = QSqlQuery(self.data_base)
        query.prepare(Query.selectUnusedTextAuthorIds())
        query.exec()
        id = []
        while query.next():
            id.append(query.value(0))
        if id:
            query = QSqlQuery(self.data_base)
            query.prepare(Query.deleteTextAuthors(len(id)))
            for i in id:
                query.addBindValue(i)
            query.exec()

        query = QSqlQuery(self.data_base)
        query.prepare(Query.selectUnusedPlaylistAudioIds())
        query.exec()
        id = []
        while query.next():
            id.append(query.value(0))
        if id:
            query = QSqlQuery(self.data_base)
            query.prepare(Query.deletePlaylistAudios(len(id)))
            for i in id:
                query.addBindValue(i)
            query.exec()

    def selectPlaylistId(self, name: str) -> int | None:
        query = QSqlQuery(self.data_base)
        query.prepare(Query.selectPlaylistId())
        query.bindValue(":name", name)
        query.exec()
        return query.value(0) if query.next() else None

    def insertPlaylist(self, name: str) -> None:
        query = QSqlQuery(self.data_base)
        query.prepare(Query.insertPlaylist())
        query.bindValue(":name", name)
        query.exec()

    def deletePlaylist(self, id: int) -> None:
        query = QSqlQuery(self.data_base)
        query.prepare(Query.deletePlaylist())
        query.bindValue(":id", id)
        query.exec()
        self.shrink()

    def insertPlaylistAudio(self, playlist_id: str, audio_id: str) -> None:
        query = QSqlQuery(self.data_base)
        query.prepare(Query.insertPlaylistAudio())
        query.bindValue(":playlist_id", playlist_id)
        query.bindValue(":audio_id", audio_id)
        query.exec()

    def deletePlaylistAudio(self, playlist_id: str, audio_id: str) -> None:
        query = QSqlQuery(self.data_base)
        query.prepare(Query.deletePlaylistAudio())
        query.bindValue(":playlist_id", playlist_id)
        query.bindValue(":audio_id", audio_id)
        query.exec()





data_base = DataBase()