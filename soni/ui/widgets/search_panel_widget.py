from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QScrollArea,
    QLabel,
    QPushButton,
    QStackedLayout
)
from PySide6.QtGui import (
    QPalette,
)
from PySide6.QtCore import (
    Qt,
)

from modules.data_base_default import DataBaseDefault

from ui.tiles.line_edit_tile import LineEditTile
from ui.tiles.combo_box_tile import ComboBoxTile
from ui.tiles.slider_tile import SliderTile
from ui.tiles.check_box_tile import CheckBoxTile
from ui.tiles.label_tile import LabelTile

# TODO: add functionality
class SearchPanelWidget(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        
        # attributes

        self.extended_open = False

        # widgets

        self.widget = QWidget()

        self.playlist = ComboBoxTile(self)
        self.playlist.setTitle("Playlist")
        self.title = LineEditTile(self)
        self.title.setTitle("Title")
        self.album_title = LineEditTile(self)
        self.album_title.setTitle("Album title")
        # TODO: duration
        self.genre = ComboBoxTile(self)
        self.genre.setTitle("Genre")
        self.genre.addItems(DataBaseDefault.genres)
        self.language = ComboBoxTile(self)
        self.language.setTitle("Language")
        self.language.addItems(list(DataBaseDefault.languages.keys()))
        # TODO: rating
        # TODO: BPM
        self.performer = ComboBoxTile(self)
        self.performer.setTitle("Performer")
        self.composer = ComboBoxTile(self)
        self.composer.setTitle("Composer")
        self.publisher = ComboBoxTile(self)
        self.publisher.setTitle("Publisher")
        self.modified_by = ComboBoxTile(self)
        self.modified_by.setTitle("Modified by")
        # TODO: release date
        self.picture_artist = ComboBoxTile(self)
        self.picture_artist.setTitle("Picture artist")
        self.text_author = ComboBoxTile(self)
        self.text_author.setTitle("Text author")
        self.original_title = LineEditTile(self)
        self.original_title.setTitle("Original title")
        self.original_album_title = LineEditTile(self)
        self.original_album_title.setTitle("Original album title")
        self.original_performer = ComboBoxTile(self)
        self.original_performer.setTitle("Original performer")
        self.original_composer = ComboBoxTile(self)
        self.original_composer.setTitle("Original composer")
        self.original_publisher = ComboBoxTile(self)
        self.original_publisher.setTitle("Original publisher")
        # TODO: original release date
        self.original_text_author = ComboBoxTile(self)
        self.original_text_author.setTitle("Original text author")
        self.isrc = LineEditTile(self)
        self.isrc.setTitle("ISRC")

        self.show_parameters_label = LabelTile(self)
        self.show_parameters_label.setTitle("Show parameters")

        self.show_playlist_check_box = CheckBoxTile(self)
        self.show_playlist_check_box.setTitle("Show playlist")
        self.show_title_check_box = CheckBoxTile(self)
        self.show_title_check_box.setTitle("Show title")
        self.show_album_title_check_box = CheckBoxTile(self)
        self.show_album_title_check_box.setTitle("Show album title")
        # self.show_duration_check_box = CheckBoxTile(self)
        # self.show_duration_check_box.setTitle("Show duration")
        self.show_genre_check_box = CheckBoxTile(self)
        self.show_genre_check_box.setTitle("Show genre")
        self.show_language_check_box = CheckBoxTile(self)
        self.show_language_check_box.setTitle("Show language")
        # self.show_rating_check_box = CheckBoxTile(self)
        # self.show_rating_check_box.setTitle("Show rating")
        # self.show_bpm_check_box = CheckBoxTile(self)
        # self.show_bpm_check_box.setTitle("Show BPM")
        self.show_performer_check_box = CheckBoxTile(self)
        self.show_performer_check_box.setTitle("Show performer")
        self.show_composer_check_box = CheckBoxTile(self)
        self.show_composer_check_box.setTitle("Show composer")
        self.show_publisher_check_box = CheckBoxTile(self)
        self.show_publisher_check_box.setTitle("Show publisher")
        self.show_modified_by_check_box = CheckBoxTile(self)
        self.show_modified_by_check_box.setTitle("Show modified by")
        # self.show_release_date_check_box = CheckBoxTile(self)
        # self.show_release_date_check_box.setTitle("Show release date")
        self.show_picture_artist_check_box = CheckBoxTile(self)
        self.show_picture_artist_check_box.setTitle("Show picture artist")
        self.show_text_author_check_box = CheckBoxTile(self)
        self.show_text_author_check_box.setTitle("Show text author")
        self.show_original_title_check_box = CheckBoxTile(self)
        self.show_original_title_check_box.setTitle("Show original title")
        self.show_original_album_title_check_box = CheckBoxTile(self)
        self.show_original_album_title_check_box.setTitle("Show original album title")
        self.show_original_performer_check_box = CheckBoxTile(self)
        self.show_original_performer_check_box.setTitle("Show original performer")
        self.show_original_composer_check_box = CheckBoxTile(self)
        self.show_original_composer_check_box.setTitle("Show original composer")
        self.show_original_publisher_check_box = CheckBoxTile(self)
        self.show_original_publisher_check_box.setTitle("Show original publisher")
        # self.show_original_release_date_check_box = CheckBoxTile(self)
        # self.show_original_release_date_check_box.setTitle("Show original release date")
        self.show_original_text_author_check_box = CheckBoxTile(self)
        self.show_original_text_author_check_box.setTitle("Show original text author")
        self.show_isrc_check_box = CheckBoxTile(self)
        self.show_isrc_check_box.setTitle("Show ISRC")
        
        self.extended_button = QPushButton(self)
        self.extended_button.setText("Extended")
        self.extended_button.clicked.connect(self.openExtended)

        self.standard_button = QPushButton(self)
        self.standard_button.setText("Standard")
        self.standard_button.clicked.connect(self.openExtended)

        self.standard_parameters = [
            self.playlist,
            self.title,
            self.album_title,
            self.genre,
            self.language,
            self.performer,
            self.text_author,
        ]

        self.extended_parameters = [
            self.composer,
            self.publisher,
            self.modified_by,
            self.picture_artist,
            self.original_title,
            self.original_album_title,
            self.original_performer,
            self.original_composer,
            self.original_publisher,
            self.original_text_author,
            self.isrc,
        ]

        self.check_boxes = [
            self.show_playlist_check_box,
            self.show_title_check_box,
            self.show_album_title_check_box,
            self.show_genre_check_box,
            self.show_language_check_box,
            self.show_performer_check_box,
            self.show_composer_check_box,
            self.show_publisher_check_box,
            self.show_modified_by_check_box,
            self.show_picture_artist_check_box,
            self.show_text_author_check_box,
            self.show_original_title_check_box,
            self.show_original_album_title_check_box,
            self.show_original_performer_check_box,
            self.show_original_composer_check_box,
            self.show_original_publisher_check_box,
            self.show_original_text_author_check_box,
            self.show_isrc_check_box,
        ]

        self.checked_boxes = [
            self.show_playlist_check_box,
            self.show_title_check_box,
            self.show_album_title_check_box,
            self.show_genre_check_box,
            self.show_language_check_box,
            self.show_performer_check_box,
            self.show_text_author_check_box,
        ]

        for check_box in self.checked_boxes:
            check_box.setChecked(True)

        # layout

        self.main_layout = QStackedLayout()
        self.main_layout.setContentsMargins(0,0,0,0)

        self.standard_layout = QVBoxLayout()
        self.standard_layout.setContentsMargins(0,0,0,0)
        self.standard_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        for parameter in self.standard_parameters:
            self.standard_layout.addWidget(parameter)

        self.standard_layout.addWidget(self.extended_button)

        self.extended_layout = QVBoxLayout()
        self.extended_layout.setContentsMargins(0,0,0,0)
        self.extended_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        for parameter in self.extended_parameters:
            self.extended_layout.addWidget(parameter)
        
        for check_box in self.check_boxes:
            self.extended_layout.addWidget(check_box)

        self.extended_layout.addWidget(self.standard_button)

        self.standard_widget = QWidget(self)
        self.standard_widget.setLayout(self.standard_layout)

        self.standard_scroll_area = QScrollArea(self)
        self.standard_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.standard_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.standard_scroll_area.setWidgetResizable(True)
        self.standard_scroll_area.setWidget(self.standard_widget)
        self.main_layout.addWidget(self.standard_scroll_area)

        self.extended_widget = QWidget(self)
        self.extended_widget.setLayout(self.extended_layout)

        self.extended_scroll_area = QScrollArea(self)
        self.extended_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.extended_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.extended_scroll_area.setWidgetResizable(True)
        self.extended_scroll_area.setWidget(self.extended_widget)
        self.main_layout.addWidget(self.extended_scroll_area)

        self.setLayout(self.main_layout)

    def openExtended(self):
        self.extended_open = not self.extended_open
        self.main_layout.setCurrentIndex(1 if self.extended_open else 0)