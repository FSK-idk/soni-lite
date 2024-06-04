from PySide6.QtWidgets import (
    QWidget,
    QScrollArea,
    QFileDialog
)
from PySide6.QtCore import Qt, Signal

from etc.audio_data import AudioData

from view.basic.v_box_layout_widget import VBoxLayoutWidget

from view.tile.combo_box_tile import ComboBoxTile
from view.tile.line_edit_tile import LineEditTile
from view.tile.push_line_edit_tile import PushLineEditTile


class AudioPanelWidget(QScrollArea):
    pictureChanged = Signal(str)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        
        self.name =  LineEditTile(self)
        self.filepath = PushLineEditTile(self)
        self.album_name = LineEditTile(self)
        self.genre_name = ComboBoxTile(self)
        self.performer_name = ComboBoxTile(self)
        self.composer_name = ComboBoxTile(self)
        self.publisher_name = ComboBoxTile(self)
        self.modified_by_name = ComboBoxTile(self)
        self.picture_png = ""
        self.picture_filepath = PushLineEditTile(self)
        self.picture_artist_name = ComboBoxTile(self)
        self.text_author_name = ComboBoxTile(self)

        self.name.setTitle("Title")
        self.filepath.setTitle("Filepath")
        self.filepath.setReadOnly(True)
        self.filepath.setButtonText("...")
        self.filepath.clicked.connect(self.chooseAudioFile)
        self.album_name.setTitle("Album title")
        self.genre_name.setTitle("Genre")
        self.genre_name.setReadOnly(True)
        self.genre_name.setTable("Genre")
        self.performer_name.setTitle("Performer")
        self.performer_name.setTable("Performer")
        self.composer_name.setTitle("Composer")
        self.composer_name.setTable("Composer")
        self.publisher_name.setTitle("Publisher")
        self.publisher_name.setTable("Publisher")
        self.modified_by_name.setTitle("Modified by")
        self.modified_by_name.setTable("ModifiedBy")
        self.picture_filepath.setTitle("Picture filepath")
        self.picture_filepath.setReadOnly(True)
        self.picture_filepath.setButtonText("...")
        self.picture_filepath.clicked.connect(self.chooseImageFile)
        self.picture_artist_name.setTitle("Picture artist")
        self.picture_artist_name.setTable("PictureArtist")
        self.text_author_name.setTitle("Text author")
        self.text_author_name.setTable("TextAuthor")

        self.clearInput()

        self.main_layout = VBoxLayoutWidget()
        self.main_layout.addWidget(self.name)
        self.main_layout.addWidget(self.filepath)
        self.main_layout.addWidget(self.album_name)
        self.main_layout.addWidget(self.genre_name)
        self.main_layout.addWidget(self.performer_name)
        self.main_layout.addWidget(self.composer_name)
        self.main_layout.addWidget(self.publisher_name)
        self.main_layout.addWidget(self.modified_by_name)
        self.main_layout.addWidget(self.picture_filepath)
        self.main_layout.addWidget(self.picture_artist_name)
        self.main_layout.addWidget(self.text_author_name)

        self.setWidget(QWidget())
        self.widget().setLayout(self.main_layout)

        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)

    def chooseAudioFile(self) -> None:
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Open file",
            "",
            "Audio files (*.mp3 *.aac *.ogg *wav);;All files (*.*)"
        )
        if path != "":
            self.filepath.setText(path)

    def chooseImageFile(self) -> None:
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Open file",
            "",
            "Image files (*.png);;All files (*.*)"
        )
        if path != "":
            self.picture_filepath.setText(path)
            self.pictureChanged.emit(path)

    def clearInput(self) -> None:
        self.name.clearInput()
        self.filepath.clearInput()
        self.album_name.clearInput()
        self.genre_name.clearInput()
        self.performer_name.clearInput()
        self.composer_name.clearInput()
        self.publisher_name.clearInput()
        self.modified_by_name.clearInput()
        self.picture_filepath.clearInput()
        self.picture_artist_name.clearInput()
        self.text_author_name.clearInput()

    def setAudioData(self, audio_data : AudioData) -> None:
        self.name.setText(audio_data.name)
        self.filepath.setText(audio_data.filepath) 
        self.album_name.setText(audio_data.album_name)
        self.genre_name.setText(audio_data.genre_name)
        self.performer_name.setText(audio_data.performer_name)
        self.composer_name.setText(audio_data.composer_name)
        self.publisher_name.setText(audio_data.publisher_name)
        self.modified_by_name.setText(audio_data.modified_by_name)
        self.picture_png = audio_data.picture_png
        self.picture_filepath.setText(audio_data.picture_filepath)
        self.picture_artist_name.setText(audio_data.picture_artist_name)
        self.text_author_name.setText(audio_data.text_author_name)

    def audioData(self) -> AudioData:
        audio_data = AudioData()
        audio_data.name = self.name.text()
        audio_data.filepath = self.filepath.text()
        audio_data.album_name = self.album_name.text()
        audio_data.genre_name = self.genre_name.text()
        audio_data.performer_name = self.performer_name.text()
        audio_data.composer_name = self.composer_name.text()
        audio_data.publisher_name = self.publisher_name.text()
        audio_data.modified_by_name = self.modified_by_name.text()
        audio_data.picture_filepath = self.picture_filepath.text()
        audio_data.picture_artist_name = self.picture_artist_name.text()
        audio_data.text_author_name = self.text_author_name.text()
        return audio_data