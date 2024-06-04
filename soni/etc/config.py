from typing import List, Tuple
import configparser
import os

class Config:
    def __init__(self):
        if not os.path.isdir("./soni/data/"): 
            os.mkdir("./soni/data/")

        self.config = configparser.ConfigParser()
        self.filepath = "./soni/data/config.ini"

        if not os.path.isfile(self.filepath):
            self.create_config()
        
        self.config.read(self.filepath)

    def create_config(self):
        self.config['Theme'] = {
            "dark_mode": "True",
            "main_color": "white"
        }
        
        self.config['Search Panel Standard Parameters'] = {
            "name": "True",
            "playlist_name": "True",
            "album_name": "True",
            "genre_name": "True",
            "performer_name": "True",
            "composer_name": "False",
            "publisher_name": "False",
            "modified_by_name": "False",
            "picture_artist_name": "False",
            "text_author_name": "False",
        }

        self.config["Audio Library Shown Parameters"] = {
            "id": "True",
            "name": "True",
            "album_name": "True",
            "genre_name": "True",
            "performer_name": "True",
            "composer_name": "False",
            "publisher_name": "False",
            "modified_by_name": "False",
            "picture_artist_name": "False",
            "text_author_name": "False",
        }

        with open(self.filepath, 'w') as file:
            self.config.write(file)

    def __getitem__(self, index):
        return self.config[index]
    
    def items(self, section: str) -> List[Tuple[str, str]]:
        return self.config.items(section)
    
    def write(self):
        with open(self.filepath, 'w') as file:
            self.config.write(file)


config = Config()