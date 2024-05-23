from typing import List, Dict

from model.audio_data import AudioData
from model.config import config

selection_attributes = {
    # 'title':                    'Audio.title',
    'album_title':              'Album.name',
    'duration':                 'Audio.duration',
    'genre':                    'Genre.name',
    'language':                 'Language.name',
    'rating':                   'Audio.rating',
    'bpm':                      'Audio.bpm',
    'performer':                'Performer.name',
    'composer':                 'Composer.name',
    'publisher':                'Publisher.name',
    'modified_by':              'ModifiedBy.name',
    'release_date':             'Audio.release_date',
    'picture_artist':           'PictureArtist.name',
    'text_author':              'TextAuthor.name',
    'original_title':           'Audio.original_title',
    'original_album_title':     'OriginalAlbum.name',
    'original_performer':       'OriginalPerformer.name',
    'original_composer':        'OriginalComposer.name',
    'original_publisher':       'OriginalPublisher.name',
    'original_release_date':    'Audio.original_release_date',
    'original_text_author':     'OriginalTextAuthor.name',
    'isrc':                     'Audio.isrc',
}

audio_info_attributes = {
        'filepath' :                    'Audio.filepath',
        'title' :                       'Audio.title',
        'album_title' :                 'Album.name',
        # 'duration'                    'Audio.duration',
        'genre' :                       'Genre.name',
        # 'language' :                  'Language.name',
        # 'rating' :                    'Audio.rating',
        # 'bpm' :                       'Audio.bpm',
        'performer' :                   'Performer.name',
        'composer' :                    'Composer.name',
        'publisher' :                   'Publisher.name',
        'modified_by' :                 'ModifiedBy.name',
        # 'release_date' :              'Audio.release_date',
        # 'copyright' :                 
        # 'comments' :                  
        # 'picture_filepath' :          ?
        'picture_artist' :              'PictureArtist.name',
        'text' :                        'Audio.text',
        'text_author' :                 'TextAuthor.name',
        'original_title' :              'Audio.original_title',
        'original_album_title' :        'OriginalAlbum.name',
        'original_performer' :          'OriginalPerformer.name',
        'original_composer' :           'OriginalComposer.name',
        'original_publisher' :          'OriginalPublisher.name',
        # 'original_release_date' :     'Audio.original_release_date',
        'original_text_author' :        'OriginalTextAuthor.name',
        'isrc' :                        'Audio.isrc',
        # 'website' :                   'Audio.website'
        # 'copyright_website' :         'Audio.copyright_website'
}

class Queries:
    # ! DANGER ZONE: F-STRING

    @staticmethod
    def create_table(table_name: str, attributes: List[str], data_types: List[str], constraints: List[str]):
        return f"""
            CREATE TABLE IF NOT EXISTS {table_name} ({', '.join([' '.join(col) for col in zip(attributes, data_types, constraints)])})
        """

    @staticmethod
    def insert(table_name: str, attributes: List[str], parameters: List[str]) -> str:
        return f"""
            INSERT OR IGNORE INTO {table_name} ({', '.join(attributes)})
            VALUES ({', '.join(parameters)})
        """

    @staticmethod
    def select_all(table_name: str, attributes: List[str], ascending: bool = True, order_column: int = 0) -> str:
        order = 'ASC' if ascending else 'DESC'
        return f"""
            SELECT {', '.join(attributes)} FROM {table_name} ORDER BY {attributes[order_column]} {order} NULLS LAST
        """

    @staticmethod
    def select_audio(ascending: bool = True, order_column: int = 0) -> str:
        attributes = ['Audio.id', 'Audio.title']
        for key, val in config.items("Library Shown Parameters"):
            if val == 'True':
                attributes.append(selection_attributes[key])
        order = 'ASC' if ascending else 'DESC'
        return f"""
            SELECT {', '.join(attributes)}
            FROM Audio
            LEFT JOIN Album ON (Audio.album_id = Album.id)
            LEFT JOIN Genre ON Audio.genre_id = Genre.id
            LEFT JOIN Language ON Audio.language_id = Language.id
            LEFT JOIN Performer ON Audio.performer_id = Performer.id
            LEFT JOIN Composer ON Audio.composer_id = Composer.id
            LEFT JOIN Publisher ON Audio.publisher_id = Publisher.id
            LEFT JOIN ModifiedBy ON Audio.modified_by_id = ModifiedBy.id
            LEFT JOIN PictureArtist ON Audio.picture_artist_id = PictureArtist.id
            LEFT JOIN TextAuthor ON Audio.text_author_id = TextAuthor.id
            LEFT JOIN Album AS OriginalAlbum ON (Audio.original_album_id = OriginalAlbum.id)
            LEFT JOIN Performer AS OriginalPerformer ON (Audio.original_performer_id = OriginalPerformer.id)
            LEFT JOIN Composer AS OriginalComposer ON (Audio.original_composer_id = OriginalComposer.id)
            LEFT JOIN Publisher AS OriginalPublisher ON (Audio.original_publisher_id = OriginalPublisher.id)
            LEFT JOIN TextAuthor AS OriginalTextAuthor ON (Audio.original_text_author_id = OriginalTextAuthor.id)
            WHERE (:title == '' OR Audio.title LIKE :title || '%')
            AND (:album_title == '' OR Album.name LIKE :album_title || '%')
            AND (:duration == '') /* Audio.duration */
            AND (:genre == '' OR Genre.name == :genre) 
            AND (:language == '') /* Language.name */
            AND (:rating == '') /* Audio.rating*/
            AND (:bpm == '') /* Audio.bpm */
            AND (:performer == '' OR Performer.name LIKE :performer || '%')
            AND (:composer == '' OR Composer.name LIKE :composer || '%')
            AND (:publisher == '' OR Publisher.name LIKE :publisher || '%')
            AND (:modified_by == '' OR ModifiedBy.name LIKE :modified_by || '%')
            AND (:release_date == '') /* Audio.release_date */
            AND (:picture_artist == '' OR PictureArtist.name LIKE :picture_artist || '%')
            AND (:text_author == '' OR TextAuthor.name LIKE :text_author || '%')
            AND (:original_title == '' OR Audio.original_title LIKE :original_title || '%')
            AND (:original_album_title == '' OR OriginalAlbum.name LIKE :original_album_title || '%')
            AND (:original_performer == '' OR OriginalPerformer.name LIKE :original_performer || '%')
            AND (:original_composer == '' OR OriginalComposer.name LIKE :original_composer || '%')
            AND (:original_publisher == '' OR OriginalPublisher.name LIKE :original_publisher || '%')
            AND (:original_release_date == '') /* Audio.original_release_date */
            AND (:original_text_author == '' OR OriginalTextAuthor.name LIKE :original_text_author || '%')
            AND (:isrc == '' OR Audio.isrc LIKE :isrc || '%')
            ORDER BY {attributes[order_column]} {order} NULLS LAST
        """
    
    @staticmethod
    def select_one_audio() -> str:
        attributes = []
        for _, attribute in audio_info_attributes.items():
            attributes.append(attribute)
        return f"""
            SELECT {', '.join(attributes)}
            FROM Audio
            LEFT JOIN Album ON (Audio.album_id = Album.id)
            LEFT JOIN Genre ON Audio.genre_id = Genre.id
            LEFT JOIN Language ON Audio.language_id = Language.id
            LEFT JOIN Performer ON Audio.performer_id = Performer.id
            LEFT JOIN Composer ON Audio.composer_id = Composer.id
            LEFT JOIN Publisher ON Audio.publisher_id = Publisher.id
            LEFT JOIN ModifiedBy ON Audio.modified_by_id = ModifiedBy.id
            LEFT JOIN PictureArtist ON Audio.picture_artist_id = PictureArtist.id
            LEFT JOIN TextAuthor ON Audio.text_author_id = TextAuthor.id
            LEFT JOIN Album AS OriginalAlbum ON (Audio.original_album_id = OriginalAlbum.id)
            LEFT JOIN Performer AS OriginalPerformer ON (Audio.original_performer_id = OriginalPerformer.id)
            LEFT JOIN Composer AS OriginalComposer ON (Audio.original_composer_id = OriginalComposer.id)
            LEFT JOIN Publisher AS OriginalPublisher ON (Audio.original_publisher_id = OriginalPublisher.id)
            LEFT JOIN TextAuthor AS OriginalTextAuthor ON (Audio.original_text_author_id = OriginalTextAuthor.id)
            WHERE Audio.id = :id
        """

    @staticmethod
    def create_table_audio() -> str:
        table_name = "Audio"
        columns = [
            ["id",                      "integer",      "PRIMARY KEY"],
            ["filepath",                "text",         ""],
            ["title",                   "text",         ""],
            ["album_id",                "integer",      ""],
            ["duration",                "integer",      ""],
            ["genre_id",                "integer",      ""],
            ["language_id",             "integer",      ""],
            ["rating",                  "integer",      ""],
            ["bpm",                     "integer",      ""],
            ["performer_id",            "integer",      ""],
            ["composer_id",             "integer",      ""],
            ["publisher_id",            "integer",      ""],
            ["modified_by_id",          "integer",      ""],
            ["release_date",            "text",         ""],
            ["copyright",               "text",         ""],
            ["comments",                "text",         ""],
            ["picture",                 "blob",         ""],
            ["picture_mime_type_id",    "integer",      ""],
            ["picture_artist_id",       "integer",      ""],
            ["text",                    "text",         ""],
            ["text_author_id",          "integer",      ""],
            ["original_title",          "text",         ""],
            ["original_album_id",       "integer",      ""],
            ["original_performer_id",   "integer",      ""],
            ["original_composer_id",    "integer",      ""],
            ["original_publisher_id",   "integer",      ""],
            ["original_release_date",   "text",         ""],
            ["original_text_author_id", "integer",      ""],
            ["isrc",                    "text",         "UNIQUE"],
            ["website",                 "text",         ""],
            ["copyright_website",       "text",         ""],
        ]
        columns = list(map(list, zip(*columns)))
        return Queries.create_table(table_name, columns[0], columns[1], columns[2])

    @staticmethod
    def create_table_album() -> str:
        table_name = "Album"
        columns = [
            ["id",      "integer",  "PRIMARY KEY"],
            ["name",    "text",     "CHECK(name != '') UNIQUE"],
        ]
        columns = list(map(list, zip(*columns)))
        return Queries.create_table(table_name, columns[0], columns[1], columns[2])

    @staticmethod
    def create_table_genre() -> str:
        table_name = "Genre"
        columns = [
            ["id",      "integer",  "PRIMARY KEY"],
            ["name",    "text",     "CHECK(name != '') UNIQUE"],
        ]
        columns = list(map(list, zip(*columns)))
        return Queries.create_table(table_name, columns[0], columns[1], columns[2])

    @staticmethod
    def create_table_language() -> str:
        table_name = "Language"
        columns = [
            ["id",      "integer",  "PRIMARY KEY"],
            ["name",    "text",     "CHECK(name != '') UNIQUE"],
            ["code",    "text",     "CHECK(code != '') UNIQUE"],
        ]
        columns = list(map(list, zip(*columns)))
        return Queries.create_table(table_name, columns[0], columns[1], columns[2])

    @staticmethod
    def create_table_performer() -> str:
        table_name = "Performer"
        columns = [
            ["id",      "integer",  "PRIMARY KEY"],
            ["name",    "text",     "CHECK(name != '') UNIQUE"],
            ["website", "text",     ""],
        ]
        columns = list(map(list, zip(*columns)))
        return Queries.create_table(table_name, columns[0], columns[1], columns[2])

    @staticmethod
    def create_table_composer() -> str:
        table_name = "Composer"
        columns = [
            ["id",      "integer",  "PRIMARY KEY"],
            ["name",    "text",     "CHECK(name != '') UNIQUE"],
            ["website", "text",     ""],
        ]
        columns = list(map(list, zip(*columns)))
        return Queries.create_table(table_name, columns[0], columns[1], columns[2])

    @staticmethod
    def create_table_publisher() -> str:
        table_name = "Publisher"
        columns = [
            ["id",      "integer",  "PRIMARY KEY"],
            ["name",    "text",     "CHECK(name != '') UNIQUE"],
            ["website", "text",     ""],
        ]
        columns = list(map(list, zip(*columns)))
        return Queries.create_table(table_name, columns[0], columns[1], columns[2])

    @staticmethod
    def create_table_modified_by() -> str:
        table_name = "ModifiedBy"
        columns = [
            ["id",      "integer",  "PRIMARY KEY"],
            ["name",    "text",     "CHECK(name != '') UNIQUE"],
            ["website", "text",     ""],
        ]
        columns = list(map(list, zip(*columns)))
        return Queries.create_table(table_name, columns[0], columns[1], columns[2])

    @staticmethod
    def create_table_picture_mime_type() -> str:
        table_name = "PictureMimeType"
        columns = [
            ["id",      "integer",  "PRIMARY KEY"],
            ["type",    "text",     "CHECK(name != '') UNIQUE"],
        ]
        columns = list(map(list, zip(*columns)))
        return Queries.create_table(table_name, columns[0], columns[1], columns[2])

    @staticmethod
    def create_table_picture_artist() -> str:
        table_name = "PictureArtist"
        columns = [
            ["id",      "integer",  "PRIMARY KEY"],
            ["name",    "text",     "CHECK(name != '') UNIQUE"],
            ["website", "text",     ""],
        ]
        columns = list(map(list, zip(*columns)))
        return Queries.create_table(table_name, columns[0], columns[1], columns[2])

    @staticmethod
    def create_table_text_author() -> str:
        table_name = "TextAuthor"
        columns = [
            ["id",      "integer",  "PRIMARY KEY"],
            ["name",    "text",     "CHECK(name != '') UNIQUE"],
            ["website", "text",     ""],
        ]
        columns = list(map(list, zip(*columns)))
        return Queries.create_table(table_name, columns[0], columns[1], columns[2])

    @staticmethod
    def create_table_playlist() -> str:
        table_name = "Playlist"
        columns = [
            ["id",      "integer",  "PRIMARY KEY"],
            ["name",    "text",     "CHECK(name != '') UNIQUE"],
        ]
        columns = list(map(list, zip(*columns)))
        return Queries.create_table(table_name, columns[0], columns[1], columns[2])

    @staticmethod
    def create_table_playlist_audio() -> str:
        table_name = "PlaylistAudio"
        columns = [
            ["audio_id",        "integer",  "UNIQUE"],
            ["playlist_id",     "integer",     "UNIQUE"],
        ]
        columns = list(map(list, zip(*columns)))
        return Queries.create_table(table_name, columns[0], columns[1], columns[2])

    @staticmethod
    def insert_album() -> str:
        return Queries.insert("Album", ["name"], [":name"])

    @staticmethod
    def insert_genre() -> str:
        return Queries.insert("Genre", ["name"], [":name"])

    @staticmethod
    def insert_language() -> str:
        return Queries.insert("Language", ["name", "code"], [":name", ":code"])

    @staticmethod
    def insert_performer() -> str:
        return Queries.insert("Performer", ["name"], [":name"])

    @staticmethod
    def insert_composer() -> str:
        return Queries.insert("Composer", ["name"], [":name"])

    @staticmethod
    def insert_publisher() -> str:
        return Queries.insert("Publisher", ["name"], [":name"])

    @staticmethod
    def insert_modified_by() -> str:
        return Queries.insert("ModifiedBy", ["name"], [":name"])

    @staticmethod
    def insert_picture_mime_type() -> str:
        return Queries.insert("PictureMimeType", ["type"], [":type"])

    @staticmethod
    def insert_picture_artist() -> str:
        return Queries.insert("PictureArtist", ["name"], [":name"])

    @staticmethod
    def insert_text_author() -> str:
        return Queries.insert("TextAuthor", ["name"], [":name"])




    select_album_id = """
        SELECT Album.id
        FROM Album
        WHERE Album.name = :name
        LIMIT 1
    """

    select_genre_id = """
        SELECT Genre.id
        FROM Genre
        WHERE Genre.name = :name
        LIMIT 1
    """

    select_performer_id = """
        SELECT Performer.id
        FROM Performer
        WHERE Performer.name = :name
        LIMIT 1
    """

    select_composer_id = """
        SELECT Composer.id
        FROM Composer
        WHERE Composer.name = :name
        LIMIT 1
    """
    select_publisher_id = """
        SELECT Publisher.id
        FROM Publisher
        WHERE Publisher.name = :name
        LIMIT 1
    """

    select_modified_by_id = """
        SELECT ModifiedBy.id
        FROM ModifiedBy
        WHERE ModifiedBy.name = :name
        LIMIT 1
    """

    select_picture_mime_type_id = """
        SELECT PictureMimeType.id
        FROM PictureMimeType
        WHERE PictureMimeType.type = :type
        LIMIT 1
    """


    select_picture_artist_id = """
        SELECT PictureArtist.id
        FROM PictureArtist
        WHERE PictureArtist.name = :name
        LIMIT 1
    """

    select_text_author_id = """
        SELECT TextAuthor.id
        FROM TextAuthor
        WHERE TextAuthor.name = :name
        LIMIT 1
    """
    insert_audio = """
        INSERT INTO Audio (
            filepath,
            title,
            album_id,
            duration,
            genre_id,
            language_id,
            rating,
            bpm,
            performer_id,
            composer_id,
            publisher_id,
            modified_by_id,
            release_date,
            copyright,
            comments,
            picture,
            picture_mime_type_id,
            picture_artist_id,
            text,
            text_author_id,
            original_title,
            original_album_id,
            original_performer_id,
            original_composer_id,
            original_publisher_id,
            original_release_date,
            original_text_author_id,
            isrc,
            website,
            copyright_website
        )
        VALUES (
            :filepath,
            :title,
            :album_id,
            :duration,
            :genre_id,
            :language_id,
            :rating,
            :bpm,
            :performer_id,
            :composer_id,
            :publisher_id,
            :modified_by_id,
            :release_date,
            :copyright,
            :comments,
            :picture,
            :picture_mime_type_id,
            :picture_artist_id,
            :text,
            :text_author_id,
            :original_title,
            :original_album_id,
            :original_performer_id,
            :original_composer_id,
            :original_publisher_id,
            :original_release_date,
            :original_text_author_id,
            :isrc,
            :website,
            :copyright_website
        )
    """



