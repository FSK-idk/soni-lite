from typing import List

from PySide6.QtWidgets import (
    QWidget,
    QScrollArea,
    QStackedLayout
)
from PySide6.QtCore import (
    Qt,
    Signal
)
from PySide6.QtSql import (
    QSqlTableModel,
)

from modules.data_base_default import DataBaseDefault
from modules.audio_info import AudioInfo
from modules.config import config
from modules.data_base import data_base

from ui.tiles.combo_box_tile import ComboBoxTile
from ui.tiles.line_edit_tile import LineEditTile

from ui.widgets.pyside.label_widget import LabelWidget
from ui.widgets.pyside.push_button_widget import PushButtonWidget
from ui.widgets.pyside.check_box_widget import CheckBoxWidget
from ui.widgets.pyside.v_box_layout_widget import VBoxLayoutWidget


class SearchInfoPanelWidget(QWidget):
    # signals

    shownParametersChanged = Signal()

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

        self.parameters_check_boxes = {
            'album_title': CheckBoxWidget(self),
            'duration': CheckBoxWidget(self),
            'genre': CheckBoxWidget(self),
            'language': CheckBoxWidget(self),
            'rating': CheckBoxWidget(self),
            'bpm': CheckBoxWidget(self),
            'performer': CheckBoxWidget(self),
            'composer': CheckBoxWidget(self),
            'publisher': CheckBoxWidget(self),
            'modified_by': CheckBoxWidget(self),
            'release_date': CheckBoxWidget(self),
            'picture_artist': CheckBoxWidget(self),
            'text_author': CheckBoxWidget(self),
            'original_title': CheckBoxWidget(self),
            'original_album_title': CheckBoxWidget(self),
            'original_performer': CheckBoxWidget(self),
            'original_composer': CheckBoxWidget(self),
            'original_publisher': CheckBoxWidget(self),
            'original_release_date': CheckBoxWidget(self),
            'original_text_author': CheckBoxWidget(self),
            'isrc': CheckBoxWidget(self),
        }


        self.advanced_button = PushButtonWidget(self)
        self.standard_button = PushButtonWidget(self)
        self.apply_button = PushButtonWidget(self)

        # setup widgets

        self.playlist.setTitle("Playlist")
        self.title.setTitle("Title")
        self.album_title.setTitle("Album title")

        # self.duration
        self.genre.setTitle("Genre")
        # self.genre.setReadOnly(True)
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
        # self.picture_filepath
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

        self.show_parameters_label.setText("Shown parameters")

        # filepath
        self.parameters_check_boxes['album_title'].setText("Show album title")
        self.parameters_check_boxes['duration'].setText("Show duration")
        self.parameters_check_boxes['genre'].setText("Show genre")
        self.parameters_check_boxes['language'].setText("Show language")
        self.parameters_check_boxes['rating'].setText("Show rating")
        self.parameters_check_boxes['bpm'].setText("Show BPM")
        self.parameters_check_boxes['performer'].setText("Show performer")
        self.parameters_check_boxes['composer'].setText("Show composer")
        self.parameters_check_boxes['publisher'].setText("Show publisher")
        self.parameters_check_boxes['modified_by'].setText("Show modified by")
        self.parameters_check_boxes['release_date'].setText("Show release date")
        self.parameters_check_boxes['picture_artist'].setText("Show picture artist")
        self.parameters_check_boxes['text_author'].setText("Show text author")
        self.parameters_check_boxes['original_title'].setText("Show original title")
        self.parameters_check_boxes['original_album_title'].setText("Show original album title")
        self.parameters_check_boxes['original_performer'].setText("Show original performer")
        self.parameters_check_boxes['original_composer'].setText("Show original composer")
        self.parameters_check_boxes['original_publisher'].setText("Show original publisher")
        self.parameters_check_boxes['original_release_date'].setText("Show original release date")
        self.parameters_check_boxes['original_text_author'].setText("Show original text author")
        self.parameters_check_boxes['isrc'].setText("Show ISRC")

        self.advanced_button.setText("Advanced")
        self.advanced_button.clicked.connect(self.openAdvanced)
        self.standard_button.setText("Standard")
        self.standard_button.clicked.connect(self.openAdvanced)
        self.apply_button.setText("Apply")
        self.apply_button.clicked.connect(self.applyParameters)

        # grouping

        self.standard_parameters: List[QWidget] = []
        self.advanced_parameters: List[QWidget] = []

        # get from config
        for key, val in config.items('Search Panel Parameters'):
            match val:
                case 'Standard':
                    self.standard_parameters.append(getattr(self, key))
                case 'Advanced':
                    self.advanced_parameters.append(getattr(self, key))

        self.shown_parameters: List[CheckBoxWidget] = []

        for parameter, check_box in self.parameters_check_boxes.items():
            match config['Library Shown Parameters'][parameter]:
                case 'True':
                    self.shown_parameters.append(check_box)

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
        for _, check_box in self.parameters_check_boxes.items():
            self.extended_layout.addWidget(check_box)
        self.extended_layout.addWidget(self.apply_button)
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

    def onTableUpdate(self) -> None:
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

    def clearInput(self) -> None:
        self.playlist.clearInput()
        self.title.setText("")
        self.album_title.setText("")
        # self.duration
        self.genre.clearInput()
        # self.language
        # self.rating
        # self.bpm
        self.performer.clearInput()
        self.composer.clearInput()
        self.publisher.clearInput()
        self.modified_by.clearInput()
        # self.release_date
        # self.copyright
        self.picture_artist.clearInput()
        self.text_author.clearInput()
        self.original_title.setText("")
        self.original_album_title.setText("")
        self.original_performer.clearInput()
        self.original_composer.clearInput()
        self.original_publisher.clearInput()
        # self.original_release_date
        self.original_text_author.clearInput()
        self.isrc.setText("")
        # self.website
        # self.copyright_website

    def applyParameters(self) -> None:

        for parameter, check_box in self.parameters_check_boxes.items():
            if check_box.isChecked():
                config['Library Shown Parameters'][parameter] = 'True'
            else:
                config['Library Shown Parameters'][parameter] = 'False'

        config.write()

        self.shownParametersChanged.emit()

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