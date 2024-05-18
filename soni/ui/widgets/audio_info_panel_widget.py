from typing import List

from PySide6.QtWidgets import (
    QWidget,
    QScrollArea,
)
from PySide6.QtCore import (
    Qt,
)

from modules.data_base_default import DataBaseDefault
from modules.audio_info import AudioInfo

from ui.tiles.combo_box_tile import ComboBoxTile
from ui.tiles.line_edit_tile import LineEditTile
from ui.tiles.file_line_edit_tile import FileLineEditTile

from ui.widgets.pyside.v_box_layout_widget import VBoxLayoutWidget


class AudioInfoPanelWidget(QScrollArea):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        
        # attributes

        self.advanced_open = False

        # widgets

        self.filepath = FileLineEditTile(self)
        self.title =  LineEditTile(self)
        self.album_title = LineEditTile(self)
        # self.duration
        self.genre = ComboBoxTile(self)
        # self.language
        # self.rating
        # self.bpm
        self.performer = ComboBoxTile(self)
        self.composer = ComboBoxTile(self)
        self.publisher = ComboBoxTile(self)
        self.modified_by = ComboBoxTile(self)
        # self.release_date
        # self.copyright
        # self.comments
        self.picture_filepath = FileLineEditTile(self)
        self.picture_artist = ComboBoxTile(self)
        # self.text
        self.text_author = ComboBoxTile(self)
        self.original_title = LineEditTile(self)
        self.original_album_title = LineEditTile(self)
        self.original_performer = ComboBoxTile(self)
        self.original_composer = ComboBoxTile(self)
        self.original_publisher = ComboBoxTile(self)
        # self.original_release_date
        self.original_text_author = ComboBoxTile(self)
        self.isrc = LineEditTile(self)
        # self.website
        # self.copyright_website

        # setup widgets

        self.filepath.setTitle("Filepath")
        self.filepath.setFilter("Audio files (*.mp3 *.aac *.ogg *wav);;All files (*.*)")
        self.title.setTitle("Title")
        self.album_title.setTitle("Album title")
        # self.duration
        self.genre.setTitle("Genre")
        self.genre.addItems(DataBaseDefault.genres) # TODO: From db
        # self.language
        # self.rating
        # self.bpm
        self.performer.setTitle("Performer")
        self.composer.setTitle("Composer")
        self.publisher.setTitle("Publisher")
        self.modified_by.setTitle("Modified by")
        # self.release_date
        # self.copyright
        # self.comments
        self.picture_filepath.setTitle("Picture filepath")
        self.picture_filepath.setFilter("Image files (*.png *.jpeg *.svg);;All files (*.*)")
        self.picture_artist.setTitle("Picture artist")
        # self.text
        self.text_author.setTitle("Text author")
        self.original_title.setTitle("Original title")
        self.original_album_title.setTitle("Original album title")
        self.original_performer.setTitle("Original performer")
        self.original_composer.setTitle("Original composer")
        self.original_publisher.setTitle("Original publisher")
        # self.original_release_date
        self.original_text_author.setTitle("Original text author")
        self.isrc.setTitle("ISRC")
        # self.website
        # self.copyright_website

        # grouping

        self.parameters: List[QWidget] = [
            self.filepath,
            self.title,
            self.album_title,
            # self.duration
            self.genre,
            # self.language
            # self.rating
            # self.bpm
            self.performer,
            self.composer,
            self.publisher,
            self.modified_by,
            # self.release_date
            # self.copyright
            # self.comments
            self.picture_filepath,
            self.picture_artist,
            self.text_author,
            self.original_title,
            self.original_album_title,
            self.original_performer,
            self.original_composer,
            self.original_publisher,
            # self.original_release_date
            self.original_text_author,
            self.isrc,
            # self.website
            # self.copyright_website
        ]

        # layout

        self.main_layout = VBoxLayoutWidget()
        for parameter in self.parameters:
            self.main_layout.addWidget(parameter)

        self.setWidget(QWidget())
        self.widget().setLayout(self.main_layout)

        # scroll bar

        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)

    def getAudioInfo(self) -> AudioInfo:
        info = AudioInfo()

        info.filepath = self.filepath.text()
        info.title = self.title.text()
        info.album_title = self.album_title.text()
        # info.duration
        info.genre = self.genre.text()
        # info.language
        # info.rating
        # info.bpm
        info.performer = self.performer.text()
        info.composer = self.composer.text()
        info.publisher = self.publisher.text()
        info.modified_by = self.modified_by.text()
        # info.release_date
        # info.copyright
        # info.comments
        info.picture_filepath = self.picture_filepath.text()
        info.picture_artist = self.picture_artist.text()
        info.text_author = self.text_author.text()
        info.original_title = self.original_title.text()
        info.original_album_title = self.original_album_title.text()
        info.original_performer = self.original_performer.text()
        info.original_composer = self.original_composer.text()
        info.original_publisher = self.original_publisher.text()
        # info.original_release_date
        info.original_text_author = self.original_text_author.text()
        info.isrc = self.isrc.text()
        # info.website
        # info.copyright_website

        return info