class DataBaseQuery:
    create_table_audio = """
        CREATE TABLE IF NOT EXISTS Audio (
            id                      integer     PRIMARY KEY,
            title                   text,
            album_id                integer,
            duration                integer,
            genre_id                integer,
            language_id             integer,
            rating                  integer,
            bpm                     integer,
            performer_id            integer,
            composer_id             integer,
            publisher_id            integer,
            modified_by_id          integer,
            release_date            text,
            copyright               text,
            comments                text,
            picture                 blob,
            picture_mime_type_id    integer,
            picture_artist_id       integer,
            text                    text,
            text_author_id          integer,
            original_album_id       integer,
            original_performer_id   integer,
            original_release_date   text,
            original_text_author_id integer,
            isrc                    text        UNIQUE,
            website                 text,
            copyright_website       text
        )
    """

    create_table_album = """
        CREATE TABLE IF NOT EXISTS Album (
            id      integer PRIMARY KEY,
            name    text
        )
    """

    create_table_genre = """
        CREATE TABLE IF NOT EXISTS Genre (
            id      integer PRIMARY KEY,
            name    text    UNIQUE
        )
    """

    create_table_language = """
        CREATE TABLE IF NOT EXISTS Language (
            id      integer PRIMARY KEY,
            name    text,
            code    text    UNIQUE
        )
    """

    create_table_performer = """
        CREATE TABLE IF NOT EXISTS Performer (
            id      integer PRIMARY KEY,
            name    text    UNIQUE,
            website text
        )
    """

    create_table_composer = """
        CREATE TABLE IF NOT EXISTS Composer (
            id      integer PRIMARY KEY,
            name    text    UNIQUE,
            website text
        )
    """

    create_table_publisher = """
        CREATE TABLE IF NOT EXISTS Publisher (
            id      integer PRIMARY KEY,
            name    text    UNIQUE,
            website text
        )
    """

    create_table_modified_by = """
        CREATE TABLE IF NOT EXISTS ModifiedBy (
            id      integer PRIMARY KEY,
            name    text    UNIQUE,
            website text
        )
    """

    create_table_picture_mime_type = """
        CREATE TABLE IF NOT EXISTS PictureMimeType (
            id      integer PRIMARY KEY,
            type    text    UNIQUE
        )
    """

    create_table_picture_artist = """
        CREATE TABLE IF NOT EXISTS PictureArtist (
            id      integer PRIMARY KEY,
            name    text    UNIQUE,
            website text
        )
    """

    create_table_text_author = """
        CREATE TABLE IF NOT EXISTS TextAuthor (
            id      integer PRIMARY KEY,
            name    text    UNIQUE,
            website text
        )
    """

    insert_genre = """
        INSERT OR IGNORE INTO Genre (name)
        VALUES (
            :name
        )
    """

    insert_language = """
        INSERT OR IGNORE INTO Language (name, code)
        VALUES (
            :name,
            :code
        )
    """

    insert_picture_mime_type = """
        INSERT OR IGNORE INTO PictureMimeType (type)
        VALUES (
            :type
        )
    """




