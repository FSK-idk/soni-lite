from typing import List, Dict

from modules.query_objects import CreateTableObject
from modules.config import config

# attribute select join
selection_attributes = {
    'title':                   ('Audio.title',                  ''),
    'album_title':             ('Album.name',                   'LEFT JOIN Album ON (Audio.album_id = Album.id)'),
    'duration':                ('Audio.duration',               ''),
    'genre':                   ('Genre.name',                   'LEFT JOIN Genre ON Audio.genre_id = Genre.id'),
    'language':                ('Language.name',                'LEFT JOIN Language ON Audio.language_id = Language.id'),
    'rating':                  ('Audio.rating',                 ''),
    'bpm':                     ('Audio.bpm',                    ''),
    'performer':               ('Performer.name',               'LEFT JOIN Performer ON Audio.performer_id = Performer.id'),
    'composer':                ('Composer.name',                'LEFT JOIN Composer ON Audio.composer_id = Composer.id'),
    'publisher':               ('Publisher.name',               'LEFT JOIN Publisher ON Audio.publisher_id = Publisher.id'),
    'modified_by':             ('ModifiedBy.name',              'LEFT JOIN ModifiedBy ON Audio.modified_by_id = ModifiedBy.id'),
    'release_date':            ('Audio.release_date',           ''),
    'picture_artist':          ('PictureArtist.name',           'LEFT JOIN PictureArtist ON Audio.picture_artist_id = PictureArtist.id'),
    'text_author':             ('TextAuthor.name',              'LEFT JOIN TextAuthor ON Audio.text_author_id = TextAuthor.id'),
    'original_title':          ('Audio.original_title',         ''),
    'original_album_title':    ('OriginalAlbum.name',           'LEFT JOIN Album AS OriginalAlbum ON (Audio.original_album_id = OriginalAlbum.id)'),
    'original_performer':      ('OriginalPerformer.name',       'LEFT JOIN Performer AS OriginalPerformer ON (Audio.original_performer_id = OriginalPerformer.id)'),
    'original_composer':       ('OriginalComposer.name',        'LEFT JOIN Composer AS OriginalComposer ON (Audio.original_composer_id = OriginalComposer.id)'),
    'original_publisher':      ('OriginalPublisher.name',       'LEFT JOIN Publisher AS OriginalPublisher ON (Audio.original_publisher_id = OriginalPublisher.id)'),
    'original_release_date':   ('Audio.original_release_date',  ''),
    'original_text_author':    ('OriginalTextAuthor.name',      'LEFT JOIN TextAuthor AS OriginalTextAuthor ON (Audio.original_text_author_id = OriginalTextAuthor.id)'),
    'isrc':                    ('Audio.isrc',                   ''),
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
    def select_all(table_name: str, attributes: List[str]) -> str:
        return f"""
            SELECT {', '.join(attributes)} FROM {table_name}
        """

    @staticmethod
    def select_audio() -> str:
        attributes = ['Audio.id', 'Audio.title']
        joins = []
        for key, val in config.items("Library Shown Parameters"):
            if val == 'True':
                attributes.append(selection_attributes[key][0])
                joins.append(selection_attributes[key][1])
        
        return f"""
            SELECT {', '.join(attributes)}
            FROM Audio
            {'\n'.join(joins)}
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
            ["name",    "text",     "CHECK(name <> \"\") UNIQUE"],
        ]
        columns = list(map(list, zip(*columns)))
        return Queries.create_table(table_name, columns[0], columns[1], columns[2])

    @staticmethod
    def create_table_genre() -> str:
        table_name = "Genre"
        columns = [
            ["id",      "integer",  "PRIMARY KEY"],
            ["name",    "text",     "CHECK(name <> \"\") UNIQUE"],
        ]
        columns = list(map(list, zip(*columns)))
        return Queries.create_table(table_name, columns[0], columns[1], columns[2])

    @staticmethod
    def create_table_language() -> str:
        table_name = "Language"
        columns = [
            ["id",      "integer",  "PRIMARY KEY"],
            ["name",    "text",     "CHECK(name <> \"\") UNIQUE"],
            ["code",    "text",     "CHECK(name <> \"\") UNIQUE"],
        ]
        columns = list(map(list, zip(*columns)))
        return Queries.create_table(table_name, columns[0], columns[1], columns[2])

    @staticmethod
    def create_table_performer() -> str:
        table_name = "Performer"
        columns = [
            ["id",      "integer",  "PRIMARY KEY"],
            ["name",    "text",     "CHECK(name <> \"\") UNIQUE"],
            ["website", "text",     ""],
        ]
        columns = list(map(list, zip(*columns)))
        return Queries.create_table(table_name, columns[0], columns[1], columns[2])

    @staticmethod
    def create_table_composer() -> str:
        table_name = "Composer"
        columns = [
            ["id",      "integer",  "PRIMARY KEY"],
            ["name",    "text",     "CHECK(name <> \"\") UNIQUE"],
            ["website", "text",     ""],
        ]
        columns = list(map(list, zip(*columns)))
        return Queries.create_table(table_name, columns[0], columns[1], columns[2])

    @staticmethod
    def create_table_publisher() -> str:
        table_name = "Publisher"
        columns = [
            ["id",      "integer",  "PRIMARY KEY"],
            ["name",    "text",     "CHECK(name <> \"\") UNIQUE"],
            ["website", "text",     ""],
        ]
        columns = list(map(list, zip(*columns)))
        return Queries.create_table(table_name, columns[0], columns[1], columns[2])

    @staticmethod
    def create_table_modified_by() -> str:
        table_name = "ModifiedBy"
        columns = [
            ["id",      "integer",  "PRIMARY KEY"],
            ["name",    "text",     "CHECK(name <> \"\") UNIQUE"],
            ["website", "text",     ""],
        ]
        columns = list(map(list, zip(*columns)))
        return Queries.create_table(table_name, columns[0], columns[1], columns[2])

    @staticmethod
    def create_table_picture_mime_type() -> str:
        table_name = "PictureMimeType"
        columns = [
            ["id",      "integer",  "PRIMARY KEY"],
            ["type",    "text",     "CHECK(name <> \"\") UNIQUE"],
        ]
        columns = list(map(list, zip(*columns)))
        return Queries.create_table(table_name, columns[0], columns[1], columns[2])

    @staticmethod
    def create_table_picture_artist() -> str:
        table_name = "PictureArtist"
        columns = [
            ["id",      "integer",  "PRIMARY KEY"],
            ["name",    "text",     "CHECK(name <> \"\") UNIQUE"],
            ["website", "text",     ""],
        ]
        columns = list(map(list, zip(*columns)))
        return Queries.create_table(table_name, columns[0], columns[1], columns[2])

    @staticmethod
    def create_table_text_author() -> str:
        table_name = "TextAuthor"
        columns = [
            ["id",      "integer",  "PRIMARY KEY"],
            ["name",    "text",     "CHECK(name <> \"\") UNIQUE"],
            ["website", "text",     ""],
        ]
        columns = list(map(list, zip(*columns)))
        return Queries.create_table(table_name, columns[0], columns[1], columns[2])

    create_table_playlist = """
        CREATE TABLE IF NOT EXISTS Playlist (
            id      integer PRIMARY KEY,
            name    text    CHECK(name <> "") UNIQUE
        )
    """

    insert_album = """
        INSERT OR IGNORE INTO Album (name)
        VALUES (
            :name
        )
    """

    select_album_id = """
        SELECT Album.id
        FROM Album
        WHERE Album.name = :name
        LIMIT 1
    """

    insert_genre = """
        INSERT OR IGNORE INTO Genre (name)
        VALUES (
            :name
        )
    """

    select_genre_id = """
        SELECT Genre.id
        FROM Genre
        WHERE Genre.name = :name
        LIMIT 1
    """

    insert_language = """
        INSERT OR IGNORE INTO Language (name, code)
        VALUES (
            :name,
            :code
        )
    """

    insert_performer = """
        INSERT OR IGNORE INTO Performer (name)
        VALUES (
            :name
        )
    """

    select_performer_id = """
        SELECT Performer.id
        FROM Performer
        WHERE Performer.name = :name
        LIMIT 1
    """

    insert_composer = """
        INSERT OR IGNORE INTO Composer (name)
        VALUES (
            :name
        )
    """

    select_composer_id = """
        SELECT Composer.id
        FROM Composer
        WHERE Composer.name = :name
        LIMIT 1
    """
    
    insert_publisher = """
        INSERT OR IGNORE INTO Publisher (name)
        VALUES (
            :name
        )
    """

    select_publisher_id = """
        SELECT Publisher.id
        FROM Publisher
        WHERE Publisher.name = :name
        LIMIT 1
    """

    insert_modified_by = """
        INSERT OR IGNORE INTO ModifiedBy (name)
        VALUES (
            :name
        )
    """

    select_modified_by_id = """
        SELECT ModifiedBy.id
        FROM ModifiedBy
        WHERE ModifiedBy.name = :name
        LIMIT 1
    """

    insert_picture_mime_type = """
        INSERT OR IGNORE INTO PictureMimeType (type)
        VALUES (
            :type
        )
    """

    select_picture_mime_type_id = """
        SELECT PictureMimeType.id
        FROM PictureMimeType
        WHERE PictureMimeType.type = :type
        LIMIT 1
    """

    insert_picture_artist = """
        INSERT OR IGNORE INTO PictureArtist (name)
        VALUES (
            :name
        )
    """

    select_picture_artist_id = """
        SELECT PictureArtist.id
        FROM PictureArtist
        WHERE PictureArtist.name = :name
        LIMIT 1
    """

    insert_text_author = """
        INSERT OR IGNORE INTO TextAuthor (name)
        VALUES (
            :name
        )
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



