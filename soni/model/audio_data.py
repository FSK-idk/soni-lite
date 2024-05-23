class AudioData:
    def __init__(self) -> None:
        self.filepath = ""
        self.title = ""
        self.album_title = ""
        # self.duration
        self.genre = ""
        # self.language
        # self.rating
        # self.bpm
        self.performer = ""
        self.composer = ""
        self.publisher = ""
        self.modified_by = ""
        # self.release_date
        # self.copyright
        # self.comments
        self.picture_filepath = ""
        self.picture_artist = ""
        self.text = ""
        self.text_author = ""
        self.original_title = ""
        self.original_album_title = ""
        self.original_performer = ""
        self.original_composer = ""
        self.original_publisher = ""
        # self.original_release_date
        self.original_text_author = ""
        self.isrc = ""
        # self.website
        # self.copyright_website
    
    def setData(self, data : list) -> None:
        attributes = [
            self.filepath,
            self.title,
            self.album_title,
            # self.duration,
            self.genre,
            # self.language,
            # self.rating,
            # self.bpm,
            self.performer,
            self.composer,
            self.publisher,
            self.modified_by,
            # self.release_date,
            # self.copyright,
            # self.comments,
            self.picture_artist,
            self.text,
            self.text_author,
            self.original_title,
            self.original_album_title,
            self.original_performer,
            self.original_composer,
            self.original_publisher,
            # self.original_release_date,
            self.original_text_author,
            self.isrc,
            # self.website,
            # self.copyright_website,
        ]
        
        self.filepath = data[0]
        self.title = data[1]
        self.album_title = data[2]
        # self.duration = data[]
        self.genre = data[3]
        # self.language = data[]
        # self.rating = data[]
        # self.bpm = data[]
        self.performer = data[4]
        self.composer = data[5]
        self.publisher = data[6]
        self.modified_by = data[7]
        # self.release_date = data[]
        # self.copyright = data[]
        # self.comments = data[]
        self.picture_artist = data[8]
        self.text = data[9]
        self.text_author = data[10]
        self.original_title = data[11]
        self.original_album_title = data[12]
        self.original_performer = data[13]
        self.original_composer = data[14]
        self.original_publisher = data[15]
        # self.original_release_date = data[]
        self.original_text_author = data[16]
        self.isrc = data[17]
        # self.website = data[]
        # self.copyright_website = data[]
        
        