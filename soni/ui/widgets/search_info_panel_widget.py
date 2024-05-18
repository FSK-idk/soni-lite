from typing import List

from PySide6.QtWidgets import (
    QWidget,
    QScrollArea,
    QStackedLayout
)
from PySide6.QtCore import (
    Qt,
)

from modules.data_base_default import DataBaseDefault
from modules.audio_info import AudioInfo
from modules.config import config

from ui.tiles.combo_box_tile import ComboBoxTile
from ui.tiles.line_edit_tile import LineEditTile

from ui.widgets.pyside.label_widget import LabelWidget
from ui.widgets.pyside.push_button_widget import PushButtonWidget
from ui.widgets.pyside.check_box_widget import CheckBoxWidget
from ui.widgets.pyside.v_box_layout_widget import VBoxLayoutWidget


class SearchInfoPanelWidget(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        
        # attributes

        self.advanced_open = False

        # widgets

        self.widget = QWidget()
        
        self.playlist = ComboBoxTile(self)
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
        self.picture_artist = ComboBoxTile(self)
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

        self.show_parameters_label = LabelWidget(self)

        # self.filepath_check_box
        self.playlist_check_box = CheckBoxWidget(self)
        self.title_check_box = CheckBoxWidget(self)
        self.album_title_check_box = CheckBoxWidget(self)
        # self.duration_check_box
        self.genre_check_box = CheckBoxWidget(self)
        # self.language_check_box
        # self.rating_check_box
        # self.bpm_check_box
        self.performer_check_box = CheckBoxWidget(self)
        self.composer_check_box = CheckBoxWidget(self)
        self.publisher_check_box = CheckBoxWidget(self)
        self.modified_by_check_box = CheckBoxWidget(self)
        # self.release_date_check_box
        # self.copyright_check_box
        # self.comments_check_box
        # self.picture_filepath_check_box
        self.picture_artist_check_box = CheckBoxWidget(self)
        # self.text_check_box
        self.text_author_check_box = CheckBoxWidget(self)
        self.original_title_check_box = CheckBoxWidget(self)
        self.original_album_title_check_box = CheckBoxWidget(self)
        self.original_performer_check_box = CheckBoxWidget(self)
        self.original_composer_check_box = CheckBoxWidget(self)
        self.original_publisher_check_box = CheckBoxWidget(self)
        # self.original_release_date_check_box
        self.original_text_author_check_box = CheckBoxWidget(self)
        self.isrc_check_box = CheckBoxWidget(self)
        # self.website_check_box
        # self.copyright_website_check_box

        self.advanced_button = PushButtonWidget(self)
        self.standard_button = PushButtonWidget(self)

        # setup widgets

        self.playlist.setTitle("Playlist")
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
        # self.picture_filepath
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

        self.show_parameters_label.setText("Shown parameters")

        # self.filepath_check_box
        self.playlist_check_box.setText("Show playlist")
        self.title_check_box.setText("Show title")
        self.album_title_check_box.setText("Show album title")
        # self.duration_check_box
        self.genre_check_box.setText("Show genre")
        # self.language_check_box
        # self.rating_check_box
        # self.bpm_check_box
        self.performer_check_box.setText("Show performer")
        self.composer_check_box.setText("Show composer")
        self.publisher_check_box.setText("Show publisher")
        self.modified_by_check_box.setText("Show modified by")
        # self.release_date_check_box
        # self.copyright_check_box
        # self.comments_check_box
        # self.picture_filepath_check_box
        self.picture_artist_check_box.setText("Show picture artist")
        # self.text_check_box
        self.text_author_check_box.setText("Show text author")
        self.original_title_check_box.setText("Show original title")
        self.original_album_title_check_box.setText("Show original album title")
        self.original_performer_check_box.setText("Show original performer")
        self.original_composer_check_box.setText("Show original composer")
        self.original_publisher_check_box.setText("Show original publisher")
        # self.original_release_date_check_box
        self.original_text_author_check_box.setText("Show original text author")
        self.isrc_check_box.setText("Show ISRC")
        # self.website_check_box
        # self.copyright_website_check_box


        self.advanced_button.setText("Advanced")
        self.advanced_button.clicked.connect(self.openAdvanced)
        self.standard_button.setText("Standard")
        self.standard_button.clicked.connect(self.openAdvanced)

        # grouping

        self.standard_parameters: List[QWidget] = []
        self.advanced_parameters: List[QWidget] = []

        # get from config
        config_data = config.items('Search Panel Parameters')
        for key, value in config_data:
            match value:
                case 'Standard':
                    self.standard_parameters.append(getattr(self, key))
                case 'Advanced':
                    self.advanced_parameters.append(getattr(self, key))

        self.shown_parameters: List[CheckBoxWidget] = []

        config_data = config.items('Library Shown Parameters')
        for key, value in config_data:
            match value:
                case 'True':
                    self.shown_parameters.append(getattr(self, key + '_check_box'))

        self.parameters_check_boxes = [
            # self.filepath_check_box,
            self.playlist_check_box,
            self.title_check_box,
            self.album_title_check_box,
            # self.duration_check_box,
            self.genre_check_box,
            # self.language_check_box,
            # self.rating_check_box,
            # self.bpm_check_box,
            self.performer_check_box,
            self.composer_check_box,
            self.publisher_check_box,
            self.modified_by_check_box,
            # self.release_date_check_box,
            # self.copyright_check_box,
            # self.comments_check_box,
            # self.picture_filepath_check_box,
            self.picture_artist_check_box,
            # self.text_check_box,
            self.text_author_check_box,
            self.original_title_check_box,
            self.original_album_title_check_box,
            self.original_performer_check_box,
            self.original_composer_check_box,
            self.original_publisher_check_box,
            # self.original_release_date_check_box,
            self.original_text_author_check_box,
            self.isrc_check_box,
            # self.website_check_box,
            # self.copyright_website_check_box,
        ]

        for check_box in self.shown_parameters:
            check_box.setChecked(True)

        # layout

        self.main_layout = QStackedLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.standard_layout = VBoxLayoutWidget()
        for parameter in self.standard_parameters:
            self.standard_layout.addWidget(parameter)
        self.standard_layout.addWidget(self.advanced_button)

        self.extended_layout = VBoxLayoutWidget()
        for parameter in self.advanced_parameters:
            self.extended_layout.addWidget(parameter)
        self.extended_layout.addWidget(self.show_parameters_label)
        for check_box in self.parameters_check_boxes:
            self.extended_layout.addWidget(check_box)
        self.extended_layout.addWidget(self.standard_button)

        self.standard_widget = QWidget(self)
        self.standard_widget.setLayout(self.standard_layout)

        self.standard_scroll_area = QScrollArea(self)
        self.standard_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.standard_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.standard_scroll_area.setWidgetResizable(True)
        self.standard_scroll_area.setWidget(self.standard_widget)
        self.main_layout.addWidget(self.standard_scroll_area)

        self.advanced_widget = QWidget(self)
        self.advanced_widget.setLayout(self.extended_layout)

        self.advanced_scroll_area = QScrollArea(self)
        self.advanced_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.advanced_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.advanced_scroll_area.setWidgetResizable(True)
        self.advanced_scroll_area.setWidget(self.advanced_widget)
        self.main_layout.addWidget(self.advanced_scroll_area)

        self.setLayout(self.main_layout)

    def openAdvanced(self) -> None:
        self.advanced_open = not self.advanced_open
        self.main_layout.setCurrentIndex(1 if self.advanced_open else 0)

    def getAudioInfo(self) -> AudioInfo:
        info = AudioInfo()

        info.playlist = self.playlist.text()
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