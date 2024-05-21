from typing import List

from PySide6.QtWidgets import (
    QWidget,
    QStackedLayout
)
from PySide6.QtCore import (
    Signal
)

from model.audio_data import AudioData
from model.config import config

from view.default.push_button_widget import PushButtonWidget
from view.default.v_box_layout_widget import VBoxLayoutWidget
from view.default.scroll_area_widget import ScrollAreaWidget

from view.tile.combo_box_tile import ComboBoxTile
from view.tile.line_edit_tile import LineEditTile

from view.widget.header_settings_widget import HeaderSettingsWidget

class SearchPanelWidget(QWidget):
    headersChanged = Signal()

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        
        # attributes

        self.advanced_open = False

        # widgets

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

        self.header_settings = HeaderSettingsWidget(self)

        self.advanced_button = PushButtonWidget(self)
        self.standard_button = PushButtonWidget(self)
        self.apply_button = PushButtonWidget(self)

        # setup widgets

        self.playlist.setTitle("Playlist")
        self.title.setTitle("Title")
        self.album_title.setTitle("Album title")
        # self.duration
        self.genre.setTitle("Genre")
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
        self.picture_artist.setTitle("Picture artist")
        self.picture_artist.setTable("PictureArtist")
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

        self.clearPanel()

        self.header_settings.headersChanged.connect(self.headersChanged.emit)

        self.advanced_button.setText("Advanced")
        self.advanced_button.clicked.connect(self.openAdvanced)
        self.standard_button.setText("Standard")
        self.standard_button.clicked.connect(self.openAdvanced)
        self.apply_button.setText("Apply")
        self.apply_button.clicked.connect(self.header_settings.apply)

        # grouping

        self.standard_parameters: List[QWidget] = []
        self.advanced_parameters: List[QWidget] = []
        for key, val in config.items('Search Panel Parameters'):
            match val:
                case 'Standard':
                    self.standard_parameters.append(getattr(self, key))
                case 'Advanced':
                    self.advanced_parameters.append(getattr(self, key))

        # layout

        self.standard_layout = VBoxLayoutWidget()
        for parameter in self.standard_parameters:
            self.standard_layout.addWidget(parameter)
        self.standard_layout.addWidget(self.advanced_button)

        self.standard_widget = QWidget(self)
        self.standard_widget.setLayout(self.standard_layout)

        self.standard_scroll_area = ScrollAreaWidget(self)
        self.standard_scroll_area.setWidget(self.standard_widget)

        self.advanced_layout = VBoxLayoutWidget()
        for parameter in self.advanced_parameters:
            self.advanced_layout.addWidget(parameter)
        self.advanced_layout.addWidget(self.header_settings)
        self.advanced_layout.addWidget(self.apply_button)
        self.advanced_layout.addWidget(self.standard_button)

        self.advanced_widget = QWidget(self)
        self.advanced_widget.setLayout(self.advanced_layout)

        self.advanced_scroll_area = ScrollAreaWidget(self)
        self.advanced_scroll_area.setWidget(self.advanced_widget)

        self.main_layout = QStackedLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addWidget(self.standard_scroll_area)
        self.main_layout.addWidget(self.advanced_scroll_area)

        self.setLayout(self.main_layout)

    def openAdvanced(self) -> None:
        self.advanced_open = not self.advanced_open
        self.main_layout.setCurrentIndex(1 if self.advanced_open else 0)

    def updatePanel(self) -> None:
        self.playlist.onTableUpdate()
        self.genre.onTableUpdate()
        self.performer.onTableUpdate()
        self.composer.onTableUpdate()
        self.publisher.onTableUpdate()
        self.modified_by.onTableUpdate()
        self.picture_artist.onTableUpdate()
        self.text_author.onTableUpdate()
        self.original_performer.onTableUpdate()
        self.original_composer.onTableUpdate()
        self.original_publisher.onTableUpdate()
        self.original_text_author.onTableUpdate()

    def clearPanel(self) -> None:
        self.playlist.clearTile()
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
        self.picture_artist.clearTile()
        self.text_author.clearTile()
        self.original_title.clearTile()
        self.original_album_title.clearTile()
        self.original_performer.clearTile()
        self.original_composer.clearTile()
        self.original_publisher.clearTile()
        # self.original_release_date
        self.original_text_author.clearTile()
        self.isrc.clearTile()

    def getSearchData(self) -> AudioData:
        search_data = AudioData()

        search_data.playlist = self.playlist.text()
        search_data.title = self.title.text()
        search_data.album_title = self.album_title.text()
        # info.duration
        search_data.genre = self.genre.text()
        # info.language
        # info.rating
        # info.bpm
        search_data.performer = self.performer.text()
        search_data.composer = self.composer.text()
        search_data.publisher = self.publisher.text()
        search_data.modified_by = self.modified_by.text()
        # info.release_date
        search_data.picture_artist = self.picture_artist.text()
        search_data.text_author = self.text_author.text()
        search_data.original_title = self.original_title.text()
        search_data.original_album_title = self.original_album_title.text()
        search_data.original_performer = self.original_performer.text()
        search_data.original_composer = self.original_composer.text()
        search_data.original_publisher = self.original_publisher.text()
        # info.original_release_date
        search_data.original_text_author = self.original_text_author.text()
        search_data.isrc = self.isrc.text()
        
        return search_data