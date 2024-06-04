from typing import List

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, Signal

from etc.audio_data import AudioData
from etc.config import config

from view.basic.push_button_widget import PushButtonWidget
from view.basic.v_box_layout_widget import VBoxLayoutWidget
from view.basic.h_box_layout_widget import HBoxLayoutWidget
from view.basic.stacked_layout_widget import StackedLayoutWidget
from view.basic.scroll_area_widget import ScrollAreaWidget

from view.tile.combo_box_tile import ComboBoxTile
from view.tile.line_edit_tile import LineEditTile

from view.widget.audio_table_header_settings_widget import AudioTableHeaderSettingsWidget


class SearchPanelWidget(QWidget):
    searchClicked = Signal(AudioData)
    headerChanged = Signal()

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        
        self.name =  LineEditTile(self)
        self.playlist_name = ComboBoxTile(self)
        self.album_name = LineEditTile(self)
        self.genre_name = ComboBoxTile(self)
        self.performer_name = ComboBoxTile(self)
        self.composer_name = ComboBoxTile(self)
        self.publisher_name = ComboBoxTile(self)
        self.modified_by_name = ComboBoxTile(self)
        self.picture_artist_name = ComboBoxTile(self)
        self.text_author_name = ComboBoxTile(self)

        self.header_settings = AudioTableHeaderSettingsWidget(self)

        self.advanced_button = PushButtonWidget(self)
        self.standard_button = PushButtonWidget(self)

        self.search_button = PushButtonWidget(self)
        self.clear_button = PushButtonWidget(self)

        self.name.setTitle("Title")
        self.playlist_name.setTitle("Playlist")
        self.playlist_name.setTable("Playlist")
        self.album_name.setTitle("Album")
        self.genre_name.setTitle("Genre")
        self.genre_name.setTable("Genre")
        self.performer_name.setTitle("Performer")
        self.performer_name.setTable("Performer")
        self.composer_name.setTitle("Composer")
        self.composer_name.setTable("Composer")
        self.publisher_name.setTitle("Publisher")
        self.publisher_name.setTable("Publisher")
        self.modified_by_name.setTitle("Modified by")
        self.modified_by_name.setTable("ModifiedBy")
        self.picture_artist_name.setTitle("Picture artist")
        self.picture_artist_name.setTable("PictureArtist")
        self.text_author_name.setTitle("Text author")
        self.text_author_name.setTable("TextAuthor")

        self.clearInput()

        self.header_settings.headerChanged.connect(self.headerChanged.emit)

        self.advanced_button.setText("Advanced")
        self.advanced_button.clicked.connect(self.openAdvancedPanel)
        self.standard_button.setText("Standard")
        self.standard_button.clicked.connect(self.openStandardPanel)

        self.search_button.setText("Search")
        self.search_button.clicked.connect(self.onSearchClicked)
        self.clear_button.setText("Clear")
        self.clear_button.clicked.connect(self.clearInput)

        self.standard_parameters: List[QWidget] = []
        self.advanced_parameters: List[QWidget] = []
        for key, val in config.items('Search Panel Standard Parameters'):
            match val:
                case "True":
                    self.standard_parameters.append(getattr(self, key))
                case "False":
                    self.advanced_parameters.append(getattr(self, key))

        self.standard_layout = VBoxLayoutWidget()
        self.standard_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        for parameter in self.standard_parameters:
            self.standard_layout.addWidget(parameter)
        self.standard_layout.addWidget(self.advanced_button)
        self.standard_widget = QWidget(self)
        self.standard_widget.setLayout(self.standard_layout)
        self.standard_scroll_area = ScrollAreaWidget(self)
        self.standard_scroll_area.setWidget(self.standard_widget)

        self.advanced_layout = VBoxLayoutWidget()
        self.advanced_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        for parameter in self.advanced_parameters:
            self.advanced_layout.addWidget(parameter)
        self.advanced_layout.addWidget(self.header_settings)
        self.advanced_layout.addWidget(self.standard_button)
        self.advanced_widget = QWidget(self)
        self.advanced_widget.setLayout(self.advanced_layout)
        self.advanced_scroll_area = ScrollAreaWidget(self)
        self.advanced_scroll_area.setWidget(self.advanced_widget)

        self.stacked_layout = StackedLayoutWidget()
        self.stacked_layout.addWidget(self.standard_scroll_area)
        self.stacked_layout.addWidget(self.advanced_scroll_area)

        self.buttons_layout = HBoxLayoutWidget()
        self.buttons_layout.addWidget(self.search_button, 3)
        self.buttons_layout.addWidget(self.clear_button, 1)

        self.main_layout = VBoxLayoutWidget()
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.main_layout.addLayout(self.stacked_layout)
        self.main_layout.addLayout(self.buttons_layout)

        self.setLayout(self.main_layout)

    def openStandardPanel(self) -> None:
        self.stacked_layout.setCurrentIndex(0)

    def openAdvancedPanel(self) -> None:
        self.stacked_layout.setCurrentIndex(1)

    def updatePanel(self) -> None:
        self.playlist_name.updateTable()
        self.genre_name.updateTable()
        self.performer_name.updateTable()
        self.composer_name.updateTable()
        self.publisher_name.updateTable()
        self.modified_by_name.updateTable()
        self.picture_artist_name.updateTable()
        self.text_author_name.updateTable()

    def clearInput(self) -> None:
        self.name.clearInput()
        self.playlist_name.clearInput()
        self.album_name.clearInput()
        self.genre_name.clearInput()
        self.performer_name.clearInput()
        self.composer_name.clearInput()
        self.publisher_name.clearInput()
        self.modified_by_name.clearInput()
        self.picture_artist_name.clearInput()
        self.text_author_name.clearInput()

    def onSearchClicked(self) -> None:
        self.searchClicked.emit(self.searchData())

    def searchData(self) -> AudioData:
        search_data = AudioData()
        search_data.name = self.name.text()
        search_data.playlist_name = self.playlist_name.text()
        search_data.album_name = self.album_name.text()
        search_data.genre_name = self.genre_name.text()
        search_data.performer_name = self.performer_name.text()
        search_data.composer_name = self.composer_name.text()
        search_data.publisher_name = self.publisher_name.text()
        search_data.modified_by_name = self.modified_by_name.text()
        search_data.picture_artist_name = self.picture_artist_name.text()
        search_data.text_author_name = self.text_author_name.text()
        return search_data