class AudioData:
    def __init__(self) -> None:
        self.id = ""
        self.name = ""
        self.filepath = ""
        self.playlist_name = ""
        self.album_name = ""
        self.genre_name = ""
        self.performer_name = ""
        self.composer_name = ""
        self.publisher_name = ""
        self.modified_by_name = ""
        self.picture_png = ""
        self.picture_filepath = ""
        self.picture_artist_name = ""
        self.text = ""
        self.text_author_name = ""
    
    def setData(self, data : list[str]) -> None:
        self.id =                   data[0]
        self.name =                 data[1]
        self.filepath =             data[2]
        self.album_name =           data[3]
        self.genre_name =           data[4]
        self.performer_name =       data[5]
        self.composer_name =        data[6]
        self.publisher_name =       data[7]
        self.modified_by_name =     data[8]
        self.picture_png =              data[9]
        self.picture_artist_name =  data[10]
        self.text =                 data[11]
        self.text_author =          data[12]
        
        