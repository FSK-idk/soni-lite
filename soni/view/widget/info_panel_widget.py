from typing import List

from PySide6.QtWidgets import (
    QWidget,
    QScrollArea,
)
from PySide6.QtCore import (
    Qt,
)

from model.audio_data import AudioData

from view.default.v_box_layout_widget import VBoxLayoutWidget

from view.tile.combo_box_tile import ComboBoxTile
from view.tile.line_edit_tile import LineEditTile
from view.tile.file_line_edit_tile import FileLineEditTile


class InfoPanelWidget(QScrollArea):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        
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
        self.genre.setReadOnly(True)
        self.genre.setTable("Genre")
        # self.language
        # self.rating
        # self.bpm
        self.performer.setTitle("Performer")
        self.performer.setTable("Performer")
        self.composer.setTitle("Composer")
        self.composer.setTable("Composer")
        self.publisher.setTitle("Publisher")
        self.publisher.setTable("Publisher")
        self.modified_by.setTitle("Modified by")
        self.modified_by.setTable("ModifiedBy")
        # self.release_date
        # self.copyright
        # self.comments
        self.picture_filepath.setTitle("Picture filepath")
        self.picture_filepath.setFilter("Image files (*.png *.jpeg *.svg);;All files (*.*)")
        self.picture_artist.setTitle("Picture artist")
        self.picture_artist.setTable("PictureArtist")
        # self.text
        self.text_author.setTitle("Text author")
        self.text_author.setTable("TextAuthor")
        self.original_title.setTitle("Original title")
        self.original_album_title.setTitle("Original album title")
        self.original_performer.setTitle("Original performer")
        self.original_performer.setTable("Performer")
        self.original_composer.setTitle("Original composer")
        self.original_composer.setTable("Composer")
        self.original_publisher.setTitle("Original publisher")
        self.original_publisher.setTable("Publisher")
        # self.original_release_date
        self.original_text_author.setTitle("Original text author")
        self.original_text_author.setTable("TextAuthor")
        self.isrc.setTitle("ISRC")
        # self.website
        # self.copyright_website

        self.clearInput()

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

    def clearInput(self) -> None:
        self.filepath.clearTile()
        self.title.clearTile()
        self.album_title.clearTile()
        # self.duration
        self.genre.clearTile()
        # self.language
        # self.rating
        # self.bpm
        self.performer.clearTile()
        self.composer.clearTile()
        self.publisher.clearTile()
        self.modified_by.clearTile()
        # self.release_date
        # self.copyright
        # self.comments
        self.picture_filepath.clearTile()
        self.picture_artist.clearTile()
        # self.text
        self.text_author.clearTile()
        self.original_title.clearTile()
        self.original_album_title.clearTile()
        self.original_performer.clearTile()
        self.original_composer.clearTile()
        self.original_publisher.clearTile()
        # self.original_release_date
        self.original_text_author.clearTile()
        self.isrc.clearTile()
        # self.website
        # self.copyright_website

    def setAudioData(self, audio_data : AudioData) -> None:
        self.filepath.setText(audio_data.filepath) 
        self.title.setText(audio_data.title)
        self.album_title.setText(audio_data.album_title)
        # audio_data.duration
        self.genre.combo_box.setEditText(audio_data.genre)
        # audio_data.language
        # audio_data.rating
        # audio_data.bpm
        self.performer.combo_box.setEditText(audio_data.performer)
        self.composer.combo_box.setEditText(audio_data.composer)
        self.publisher.combo_box.setEditText(audio_data.publisher)
        self.modified_by.combo_box.setEditText(audio_data.modified_by)
        # audio_data.release_date
        # audio_data.copyright
        # audio_data.comments
        self.picture_filepath.setText(audio_data.picture_filepath)
        self.picture_artist.combo_box.setEditText(audio_data.picture_artist)
        self.text_author.combo_box.setEditText(audio_data.text_author)
        self.original_title.setText(audio_data.original_title)
        self.original_album_title.setText(audio_data.original_album_title)
        self.original_performer.combo_box.setEditText(audio_data.original_performer)
        self.original_composer.combo_box.setEditText(audio_data.original_composer)
        self.original_publisher.combo_box.setEditText(audio_data.original_publisher)
        # audio_data.original_release_date
        self.original_text_author.combo_box.setEditText(audio_data.original_text_author)
        self.isrc.setText(audio_data.isrc)
        # audio_data.website
        # audio_data.copyright_website

    def getAudioData(self) -> AudioData:
        audio_data = AudioData()

        audio_data.filepath = self.filepath.text()
        audio_data.title = self.title.text()
        audio_data.album_title = self.album_title.text()
        # audio_data.duration
        audio_data.genre = self.genre.text()
        # audio_data.language
        # audio_data.rating
        # audio_data.bpm
        audio_data.performer = self.performer.text()
        audio_data.composer = self.composer.text()
        audio_data.publisher = self.publisher.text()
        audio_data.modified_by = self.modified_by.text()
        # audio_data.release_date
        # audio_data.copyright
        # audio_data.comments
        audio_data.picture_filepath = self.picture_filepath.text()
        audio_data.picture_artist = self.picture_artist.text()
        audio_data.text_author = self.text_author.text()
        audio_data.original_title = self.original_title.text()
        audio_data.original_album_title = self.original_album_title.text()
        audio_data.original_performer = self.original_performer.text()
        audio_data.original_composer = self.original_composer.text()
        audio_data.original_publisher = self.original_publisher.text()
        # audio_data.original_release_date
        audio_data.original_text_author = self.original_text_author.text()
        audio_data.isrc = self.isrc.text()
        # audio_data.website
        # audio_data.copyright_website

        return audio_data