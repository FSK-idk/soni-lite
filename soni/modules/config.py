from typing import List, Tuple, Dict
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

    def create_config(self):
        self.config['Theme'] = {
            'dark mode': 'True',
            'main color': 'white'
        }
        
        self.config['Database'] = {
            'data base name': './soni/data/library.sqlite',
        }

        self.config['Search Panel Parameters'] = {
            'filepath': 'None',
            'playlist': 'Standard',
            'title': 'Standard',
            'album_title': 'Standard',
            # 'duration'
            'genre': 'Standard',
            # 'language'
            # 'rating'
            # 'bpm'
            'performer': 'Standard',
            'composer': 'Advanced',
            'publisher': 'Advanced',
            'modified_by': 'Advanced',
            # 'release_date'
            # 'copyright'
            # 'comments'
            # 'picture_filepath'
            'picture_artist': 'Advanced',
            # 'text'
            'text_author': 'Standard',
            'original_title': 'Advanced',
            'original_album_title': 'Advanced',
            'original_performer': 'Advanced',
            'original_composer': 'Advanced',
            'original_publisher': 'Advanced',
            # 'original_release_date'
            'original_text_author': 'Advanced',
            'isrc': 'Advanced',
            # 'website'
            # 'copyright_website'
        }

        self.config['Library Shown Parameters'] = {
            'filepath': 'False',
            'playlist': 'True',
            'title': 'True',
            'album_title': 'True',
            # 'duration'
            'genre': 'True',
            # 'language'
            # 'rating'
            # 'bpm'
            'performer': 'True',
            'composer': 'False',
            'publisher': 'False',
            'modified_by': 'False',
            # 'release_date'
            # 'copyright'
            # 'comments'
            # 'picture_filepath'
            'picture_artist': 'False',
            # 'text'
            'text_author': 'True',
            'original_title': 'False',
            'original_album_title': 'False',
            'original_performer': 'False',
            'original_composer': 'False',
            'original_publisher': 'False',
            # 'original_release_date'
            'original_text_author': 'False',
            'isrc': 'False',
            # 'website'
            # 'copyright_website'
        }

        with open(self.filepath, 'w') as file:
            self.config.write(file)

    def get(self, section: str, option: str) -> str:
        self.config.read(self.filepath)
        return self.config.get(section=section, option=option)

    def get_int(self, section: str, option: str) -> int:
        self.config.read(self.filepath)
        return self.config.getint(section=section, option=option)
    
    def get_flaot(self, section: str, option: str) -> float:
        self.config.read(self.filepath)
        return self.config.getfloat(section=section, option=option)
    
    def get_boolean(self, section: str, option: str) -> bool:
        self.config.read(self.filepath)
        return self.config.getboolean(section=section, option=option)

    def items(self, section: str) -> List[Tuple[str, str]]:
        self.config.read(self.filepath)
        return self.config.items(section)


config = Config()