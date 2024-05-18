class DataBaseQuery:
    create_table_audio = """
        CREATE TABLE IF NOT EXISTS Audio (
            id                      integer     PRIMARY KEY,
            filepath                text,
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
            original_title          text,
            original_album_id       integer,
            original_performer_id   integer,
            original_composer_id    integer,
            original_publisher_id   integer,
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
            name    text    CHECK(name <> "") UNIQUE
        )
    """

    create_table_genre = """
        CREATE TABLE IF NOT EXISTS Genre (
            id      integer PRIMARY KEY,
            name    text    CHECK(name <> "") UNIQUE
        )
    """

    create_table_language = """
        CREATE TABLE IF NOT EXISTS Language (
            id      integer PRIMARY KEY,
            name    text,
            code    text    CHECK(name <> "") UNIQUE
        )
    """

    create_table_performer = """
        CREATE TABLE IF NOT EXISTS Performer (
            id      integer PRIMARY KEY,
            name    text    CHECK(name <> "") UNIQUE,
            website text
        )
    """

    create_table_composer = """
        CREATE TABLE IF NOT EXISTS Composer (
            id      integer PRIMARY KEY,
            name    text    CHECK(name <> "") UNIQUE,
            website text
        )
    """

    create_table_publisher = """
        CREATE TABLE IF NOT EXISTS Publisher (
            id      integer PRIMARY KEY,
            name    text    CHECK(name <> "") UNIQUE,
            website text
        )
    """

    create_table_modified_by = """
        CREATE TABLE IF NOT EXISTS ModifiedBy (
            id      integer PRIMARY KEY,
            name    text    CHECK(name <> "") UNIQUE,
            website text
        )
    """

    create_table_picture_mime_type = """
        CREATE TABLE IF NOT EXISTS PictureMimeType (
            id      integer PRIMARY KEY,
            type    text    CHECK(type <> "") UNIQUE
        )
    """

    create_table_picture_artist = """
        CREATE TABLE IF NOT EXISTS PictureArtist (
            id      integer PRIMARY KEY,
            name    text    CHECK(name <> "") UNIQUE,
            website text
        )
    """

    create_table_text_author = """
        CREATE TABLE IF NOT EXISTS TextAuthor (
            id      integer PRIMARY KEY,
            name    text    CHECK(name <> "") UNIQUE,
            website text
        )
    """

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




