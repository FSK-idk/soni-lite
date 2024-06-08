from etc.config import config

table_header_attributes = {
    "id":                       "Audio.id",
    "name":                     "Audio.name",
    "album_name":               "Album.name",
    "genre_name":               "Genre.name",
    "performer_name":           "Performer.name",
    "composer_name":            "Composer.name",
    "publisher_name":           "Publisher.name",
    "modified_by_name":         "ModifiedBy.name",
    "picture_artist_name":      "PictureArtist.name",
    "text_author_name":         "TextAuthor.name",
}

audio_attributes = [
    "Audio.id",
    "Audio.name",
    "Audio.filepath",
    "Album.name",
    "Genre.name",
    "Performer.name",
    "Composer.name",
    "Publisher.name",
    "ModifiedBy.name",
    "Audio.picture_png",
    "PictureArtist.name",
    "Audio.text",
    "TextAuthor.name",
]


class Query:

    # create table

    @staticmethod
    def createAudioTable() -> str:
        return """
            CREATE TABLE IF NOT EXISTS Audio (
                id                  integer     PRIMARY KEY,
                filepath            text,
                name                text,
                album_id            integer,
                genre_id            integer,
                performer_id        integer,
                composer_id         integer,
                publisher_id        integer,
                modified_by_id      integer,
                picture_png         blob,
                picture_artist_id   integer,
                text                text,
                text_author_id      integer
            )
        """

    @staticmethod
    def createAlbumTable() -> str:
        return """
            CREATE TABLE IF NOT EXISTS Album (
                id                  integer     PRIMARY KEY,
                name                text        CHECK(name != '') UNIQUE
            )
        """
    
    @staticmethod
    def createGenreTable() -> str:
        return """
            CREATE TABLE IF NOT EXISTS Genre (
                id                  integer     PRIMARY KEY,
                name                text        CHECK(name != '') UNIQUE
            )
        """
    
    @staticmethod
    def createPerformerTable() -> str:
        return """
            CREATE TABLE IF NOT EXISTS Performer (
                id                  integer     PRIMARY KEY,
                name                text        CHECK(name != '') UNIQUE
            )
        """
    
    @staticmethod
    def createComposerTable() -> str:
        return """
            CREATE TABLE IF NOT EXISTS Composer (
                id                  integer     PRIMARY KEY,
                name                text        CHECK(name != '') UNIQUE
            )
        """

    @staticmethod
    def createPublisherTable() -> str:
        return """
            CREATE TABLE IF NOT EXISTS Publisher (
                id                  integer     PRIMARY KEY,
                name                text        CHECK(name != '') UNIQUE
            )
        """
    
    @staticmethod
    def createModifiedByTable() -> str:
        return """
            CREATE TABLE IF NOT EXISTS ModifiedBy (
                id                  integer     PRIMARY KEY,
                name                text        CHECK(name != '') UNIQUE
            )
        """
    
    @staticmethod
    def createPictureArtistTable() -> str:
        return """
            CREATE TABLE IF NOT EXISTS PictureArtist (
                id                  integer     PRIMARY KEY,
                name                text        CHECK(name != '') UNIQUE
            )
        """

    @staticmethod
    def createTextAuthorTable() -> str:
        return """
            CREATE TABLE IF NOT EXISTS TextAuthor (
                id                  integer     PRIMARY KEY,
                name                text        CHECK(name != '') UNIQUE
            )
        """

    @staticmethod
    def createPlaylistTable() -> str:
        return """
            CREATE TABLE IF NOT EXISTS Playlist (
                id                  integer     PRIMARY KEY,
                name                text        CHECK(name != '') UNIQUE
            )
        """

    @staticmethod
    def createPlaylistAudioTable() -> str:
        return """
            CREATE TABLE IF NOT EXISTS PlaylistAudio (
                id                  integer     PRIMARY KEY,
                playlist_id         integer,
                audio_id            integer,
                serial              integer
            )
        """

    # insert

    @staticmethod
    def insertAlbum() -> str:
        return """
            INSERT OR IGNORE INTO Album (name)
            VALUES (:name)
        """

    @staticmethod
    def insertGenre() -> str:
        return """
            INSERT OR IGNORE INTO Genre (name)
            VALUES (:name)
        """

    @staticmethod
    def insertPerformer() -> str:
        return """
            INSERT OR IGNORE INTO Performer (name)
            VALUES (:name)
        """

    @staticmethod
    def insertComposer() -> str:
        return """
            INSERT OR IGNORE INTO Composer (name)
            VALUES (:name)
        """

    @staticmethod
    def insertPublisher() -> str:
        return """
            INSERT OR IGNORE INTO Publisher (name)
            VALUES (:name)
        """

    @staticmethod
    def insertModifiedBy() -> str:
        return """
            INSERT OR IGNORE INTO ModifiedBy (name)
            VALUES (:name)
        """

    @staticmethod
    def insertPictureArtist() -> str:
        return """
            INSERT OR IGNORE INTO PictureArtist (name)
            VALUES (:name)
        """

    @staticmethod
    def insertTextAuthor() -> str:
        return """
            INSERT OR IGNORE INTO TextAuthor (name)
            VALUES (:name)
        """

    @staticmethod
    def insertAudio() -> str:
        return """
            INSERT OR IGNORE INTO Audio (
                name,
                filepath,
                album_id,
                genre_id,
                performer_id,
                composer_id,
                publisher_id,
                modified_by_id,
                picture_png,
                picture_artist_id,
                text,
                text_author_id
            )
            VALUES (
                :name,
                :filepath,
                :album_id,
                :genre_id,
                :performer_id,
                :composer_id,
                :publisher_id,
                :modified_by_id,
                :picture_png,
                :picture_artist_id,
                :text,
                :text_author_id
            )
        """

    @staticmethod
    def insertPlaylist() -> str:
        return """
            INSERT OR IGNORE INTO Playlist (name)
            VALUES (:name)
        """

    @staticmethod
    def insertPlaylistAudio() -> str:
        return """
            INSERT OR IGNORE INTO PlaylistAudio (playlist_id, audio_id, serial)
            VALUES (:playlist_id, :audio_id, :serial)
        """
    
    # update

    @staticmethod
    def updateAudio() -> str:
        return """
            UPDATE Audio
            SET name = :name,
                filepath = :filepath,
                album_id = :album_id,
                genre_id = :genre_id,
                performer_id = :performer_id,
                composer_id = :composer_id,
                publisher_id = :publisher_id,
                modified_by_id = :modified_by_id,
                picture_png = :picture_png,
                picture_artist_id = :picture_artist_id,
                text = :text,
                text_author_id = :text_author_id
            WHERE id = :id
        """

    @staticmethod
    def updatePlaylistAudioSerial() -> str:
        return """
            UPDATE PlaylistAudio
            SET serial = :serial
            WHERE id = :id
        """




    # select

    @staticmethod
    def selectGenreNames(descending: bool = True) -> str:
        order = "DESC" if descending else "ASC"
        return f"""
            SELECT Genre.name
            FROM Genre
            ORDER BY Genre.name {order} NULLS LAST
        """

    @staticmethod
    def selectPerformerNames(descending: bool = True) -> str:
        order = "DESC" if descending else "ASC"
        return f"""
            SELECT Performer.name
            FROM Performer
            ORDER BY Performer.name {order} NULLS LAST
        """

    @staticmethod
    def selectComposerNames(descending: bool = True) -> str:
        order = "DESC" if descending else "ASC"
        return f"""
            SELECT Composer.name
            FROM Composer
            ORDER BY Composer.name {order} NULLS LAST
        """

    @staticmethod
    def selectPublisherNames(descending: bool = True) -> str:
        order = "DESC" if descending else "ASC"
        return f"""
            SELECT Publisher.name
            FROM Publisher
            ORDER BY Publisher.name {order} NULLS LAST
        """

    @staticmethod
    def selectModifiedByNames(descending: bool = True) -> str:
        order = "DESC" if descending else "ASC"
        return f"""
            SELECT ModifiedBy.name
            FROM ModifiedBy
            ORDER BY ModifiedBy.name {order} NULLS LAST
        """

    @staticmethod
    def selectPictureArtistNames(descending: bool = True) -> str:
        order = "DESC" if descending else "ASC"
        return f"""
            SELECT PictureArtist.name
            FROM PictureArtist
            ORDER BY PictureArtist.name {order} NULLS LAST
        """

    @staticmethod
    def selectTextAuthorNames(descending: bool = True) -> str:
        order = "DESC" if descending else "ASC"
        return f"""
            SELECT TextAuthor.name
            FROM TextAuthor
            ORDER BY TextAuthor.name {order} NULLS LAST
        """

    @staticmethod
    def selectPlaylistNames(descending: bool = True) -> str:
        order = "DESC" if descending else "ASC"
        return f"""
            SELECT Playlist.name
            FROM Playlist
            ORDER BY Playlist.name {order} NULLS LAST
        """

    @staticmethod
    def selectAlbumId() -> str:
        return f"""
            SELECT Album.id
            FROM Album
            WHERE Album.name = :name
            LIMIT 1
        """
    
    @staticmethod
    def selectGenreId() -> str:
        return f"""
            SELECT Genre.id
            FROM Genre
            WHERE Genre.name = :name
            LIMIT 1
        """

    @staticmethod
    def selectPerformerId() -> str:
        return f"""
            SELECT Performer.id
            FROM Performer
            WHERE Performer.name = :name
            LIMIT 1
        """

    @staticmethod
    def selectComposerId() -> str:
        return f"""
            SELECT Composer.id
            FROM Composer
            WHERE Composer.name = :name
            LIMIT 1
        """
    
    @staticmethod
    def selectPublisherId() -> str:
        return f"""
            SELECT Publisher.id
            FROM Publisher
            WHERE Publisher.name = :name
            LIMIT 1
        """
    
    @staticmethod
    def selectModifiedById() -> str:
        return f"""
            SELECT ModifiedBy.id
            FROM ModifiedBy
            WHERE ModifiedBy.name = :name
            LIMIT 1
        """
    
    @staticmethod
    def selectPictureArtistId() -> str:
        return f"""
            SELECT PictureArtist.id
            FROM PictureArtist
            WHERE PictureArtist.name = :name
            LIMIT 1
        """
    
    @staticmethod
    def selectTextAuthorId() -> str:
        return f"""
            SELECT TextAuthor.id
            FROM TextAuthor
            WHERE TextAuthor.name = :name
            LIMIT 1
        """

    @staticmethod
    def selectPlaylistId() -> str:
        return f"""
            SELECT Playlist.id
            FROM Playlist
            WHERE Playlist.name = :name
            LIMIT 1
        """

    @staticmethod
    def selectPlaylistIds() -> str:
        return f"""
            SELECT Playlist.id
            FROM Playlist
        """

    @staticmethod
    def selectPlaylistAudioId() -> str:
        return f"""
            SELECT PlaylistAudio.id
            FROM PlaylistAudio
            LEFT JOIN Audio ON PlaylistAudio.audio_id = Audio.id
            LEFT JOIN Playlist ON PlaylistAudio.playlist_id = Playlist.id
            WHERE Playlist.id = :playlist_id
            AND Audio.id = :audio_id
            LIMIT 1
        """

    @staticmethod
    def selectPlaylistAudioIdsSerals() -> str:
        return f"""
            SELECT PlaylistAudio.id, PlaylistAudio.serial
            FROM PlaylistAudio
            LEFT JOIN Audio ON PlaylistAudio.audio_id = Audio.id
            LEFT JOIN Playlist ON PlaylistAudio.playlist_id = Playlist.id
            WHERE Playlist.id = :playlist_id
        """
    
    @staticmethod
    def selectPlaylistAudioSerial() -> str:
        return f"""
            SELECT PlaylistAudio.serial
            FROM PlaylistAudio
            LEFT JOIN Audio ON PlaylistAudio.audio_id = Audio.id
            LEFT JOIN Playlist ON PlaylistAudio.playlist_id = Playlist.id
            WHERE Playlist.id = :playlist_id
            AND Audio.id = :audio_id
            LIMIT 1
        """

    @staticmethod
    def selectPlaylistAudioIdBySerial() -> str:
        return f"""
            SELECT PlaylistAudio.id
            FROM PlaylistAudio
            WHERE PlaylistAudio.playlist_id = :playlist_id
            AND PlaylistAudio.serial = :serial
            LIMIT 1
        """

    @staticmethod
    def selectAudioData() -> str:
        return f"""
            SELECT {', '.join(audio_attributes)}
            FROM Audio
            LEFT JOIN Album ON Audio.album_id = Album.id
            LEFT JOIN Genre ON Audio.genre_id = Genre.id
            LEFT JOIN Performer ON Audio.performer_id = Performer.id
            LEFT JOIN Composer ON Audio.composer_id = Composer.id
            LEFT JOIN Publisher ON Audio.publisher_id = Publisher.id
            LEFT JOIN ModifiedBy ON Audio.modified_by_id = ModifiedBy.id
            LEFT JOIN PictureArtist ON Audio.picture_artist_id = PictureArtist.id
            LEFT JOIN TextAuthor ON Audio.text_author_id = TextAuthor.id
            WHERE Audio.id = :id
            LIMIT 1
        """

    @staticmethod
    def selectAudioTable(descending: bool = True, sort_column: int = 0) -> str:
        attributes = []
        for parameter, checked in config.items("Audio Library Shown Parameters"):
            if checked == "True":
                attributes.append(table_header_attributes[parameter])
        order = "DESC" if descending else "ASC"
        return f"""
            SELECT {', '.join(attributes)}
            FROM Audio
            LEFT JOIN Album ON Audio.album_id = Album.id
            LEFT JOIN Genre ON Audio.genre_id = Genre.id
            LEFT JOIN Performer ON Audio.performer_id = Performer.id
            LEFT JOIN Composer ON Audio.composer_id = Composer.id
            LEFT JOIN Publisher ON Audio.publisher_id = Publisher.id
            LEFT JOIN ModifiedBy ON Audio.modified_by_id = ModifiedBy.id
            LEFT JOIN PictureArtist ON Audio.picture_artist_id = PictureArtist.id
            LEFT JOIN TextAuthor ON Audio.text_author_id = TextAuthor.id
            WHERE (:name == '' OR Audio.name LIKE :name || '%')
            AND (:album_name == '' OR Album.name LIKE :album_name || '%')
            AND (:genre_name == '' OR Genre.name == :genre_name) 
            AND (:performer_name == '' OR Performer.name LIKE :performer_name || '%')
            AND (:composer_name == '' OR Composer.name LIKE :composer_name || '%')
            AND (:publisher_name == '' OR Publisher.name LIKE :publisher_name || '%')
            AND (:modified_by_name == '' OR ModifiedBy.name LIKE :modified_by_name || '%')
            AND (:picture_artist_name == '' OR PictureArtist.name LIKE :picture_artist_name || '%')
            AND (:text_author_name == '' OR TextAuthor.name LIKE :text_author_name || '%')
            ORDER BY {attributes[sort_column]} {order} NULLS LAST
        """

    @staticmethod
    def selectUnusedAlbumIds() -> str:
        return """
            SELECT Album.id
            FROM Album
            LEFT JOIN Audio ON Audio.album_id = Album.id
            WHERE Audio.album_id IS NULL
        """

    @staticmethod
    def selectUnusedPerformerIds() -> str:
        return """
            SELECT Performer.id
            FROM Performer
            LEFT JOIN Audio ON Audio.performer_id = Performer.id
            WHERE Audio.performer_id IS NULL
        """
    
    @staticmethod
    def selectUnusedComposerIds() -> str:
        return """
            SELECT Composer.id
            FROM Composer
            LEFT JOIN Audio ON Audio.composer_id = Composer.id
            WHERE Audio.composer_id IS NULL
        """
    
    @staticmethod
    def selectUnusedPublisherIds() -> str:
        return """
            SELECT Publisher.id
            FROM Publisher
            LEFT JOIN Audio ON Audio.publisher_id = Publisher.id
            WHERE Audio.publisher_id IS NULL
        """

    @staticmethod
    def selectUnusedModifiedByIds() -> str:
        return """
            SELECT ModifiedBy.id
            FROM ModifiedBy
            LEFT JOIN Audio ON Audio.modified_by_id = ModifiedBy.id
            WHERE Audio.modified_by_id IS NULL
        """

    @staticmethod
    def selectUnusedPictureArtistIds() -> str:
        return """
            SELECT PictureArtist.id
            FROM PictureArtist
            LEFT JOIN Audio ON Audio.picture_artist_id = PictureArtist.id
            WHERE Audio.picture_artist_id IS NULL
        """
    
    @staticmethod
    def selectUnusedTextAuthorIds() -> str:
        return """
            SELECT TextAuthor.id
            FROM TextAuthor
            LEFT JOIN Audio ON Audio.text_author_id = TextAuthor.id
            WHERE Audio.text_author_id IS NULL
        """

    @staticmethod
    def selectPlaylistTable(descending: bool = True, sort_column: int = 0) -> str:
        attributes = ["Playlist.id", "Playlist.name"]
        order = "DESC" if descending else "ASC"
        return f"""
            SELECT {', '.join(attributes)}
            FROM Playlist
            WHERE (:name == '' OR Playlist.name LIKE :name || '%')
            ORDER BY {attributes[sort_column]} {order} NULLS LAST
        """

    @staticmethod
    def selectPlaylistAudioTable(descending: bool = True, sort_column: int = 0) -> str:
        attributes = ["Audio.id", "Audio.name", "PlaylistAudio.serial"]
        order = "DESC" if descending else "ASC"
        return f"""
            SELECT {', '.join(attributes)}
            FROM PlaylistAudio
            LEFT JOIN Audio ON Audio.id = PlaylistAudio.audio_id
            WHERE PlaylistAudio.playlist_id = :id
            ORDER BY {attributes[sort_column]} {order} NULLS LAST
        """

# DO I NEED IT? IF UP IS THE SAME
    @staticmethod
    def selectPlaylistAudios(descending: bool = True, sort_column: int = 0) -> str:
        attributes = ["PlaylistAudio.id", "Audio.id", "Audio.name"]
        order = "DESC" if descending else "ASC"
        return f"""
            SELECT {', '.join(attributes)}
            FROM PlaylistAudio
            LEFT JOIN Audio ON PlaylistAudio.audio_id = Audio.id
            LEFT JOIN Playlist ON PlaylistAudio.playlist_id = Playlist.id
            WHERE Playlist.name = :name
            ORDER BY {attributes[sort_column]} {order} NULLS LAST
        """

    @staticmethod
    def selectUnusedPlaylistAudioIds() -> str:
        return """
            SELECT PlaylistAudio.id
            FROM PlaylistAudio
            LEFT JOIN Audio ON Audio.id = PlaylistAudio.audio_id
            LEFT JOIN Playlist ON Playlist.id = PlaylistAudio.playlist_id
            WHERE Playlist.id IS NULL
            OR Audio.id IS NULL
        """


    @staticmethod
    def selectUnusedPlaylistAudioIds1() -> str:
        return """
            SELECT PlaylistAudio.id
            FROM PlaylistAudio
            LEFT JOIN Audio ON Audio.id = PlaylistAudio.audio_id
            WHERE Audio.id IS NULL
        """

    # delete

    @staticmethod
    def deleteAlbums(count: int) -> str:
        return f"""
            DELETE
            FROM Album
            WHERE Album.id IN ({', '.join('?' * count)})
        """

    @staticmethod
    def deletePerformers(count: int) -> str:
        return f"""
            DELETE
            FROM Performer
            WHERE Performer.id IN ({', '.join('?' * count)})
        """
    
    @staticmethod
    def deleteComposers(count: int) -> str:
        return f"""
            DELETE
            FROM Composer
            WHERE Composer.id IN ({', '.join('?' * count)})
        """    
    
    @staticmethod
    def deletePublishers(count: int) -> str:
        return f"""
            DELETE
            FROM Publisher
            WHERE Publisher.id IN ({', '.join('?' * count)})
        """
        
    @staticmethod
    def deleteModifiedBys(count: int) -> str:
        return f"""
            DELETE
            FROM ModifiedBy
            WHERE ModifiedBy.id IN ({', '.join('?' * count)})
        """
     
    @staticmethod
    def deletePictureArtists(count: int) -> str:
        return f"""
            DELETE
            FROM PictureArtist
            WHERE PictureArtist.id IN ({', '.join('?' * count)})
        """
     
    @staticmethod
    def deleteTextAuthors(count: int) -> str:
        return f"""
            DELETE
            FROM TextAuthor
            WHERE TextAuthor.id IN ({', '.join('?' * count)})
        """

    @staticmethod
    def deleteAudio() -> str:
        return """
            DELETE
            FROM Audio
            WHERE Audio.id = :id
        """

    @staticmethod
    def deletePlaylist() -> str:
        return """
            DELETE
            FROM Playlist
            WHERE Playlist.id = :id
        """

    @staticmethod
    def deletePlaylistAudio() -> str:
        return """
            DELETE
            FROM PlaylistAudio
            WHERE PlaylistAudio.playlist_id = :playlist_id
            AND PlaylistAudio.audio_id = :audio_id
        """

    @staticmethod
    def deletePlaylistAudios(count: int) -> str:
        return f"""
            DELETE
            FROM PlaylistAudio
            WHERE PlaylistAudio.id IN ({', '.join('?' * count)})
        """

    # count

    @staticmethod
    def countPlaylistAudios() -> str:
        return f"""
            SELECT COUNT(*)
            FROM PlaylistAudio
            LEFT JOIN Playlist ON Playlist.id = PlaylistAudio.playlist_id
            WHERE Playlist.id = :id
        """


























