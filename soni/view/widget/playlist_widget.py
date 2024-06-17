import random

from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Signal, QItemSelection

from etc.audio_data import AudioData

from model.combo_box_model import ComboBoxModel
from model.playlist_model import PlaylistModel

from view.basic.v_box_layout_widget import VBoxLayoutWidget
from view.basic.h_box_layout_widget import HBoxLayoutWidget
from view.basic.combo_box_widget import ComboBoxWidget
from view.basic.push_button_widget import PushButtonWidget

from view.widget.playlist_audio_table_widget import PlaylistAudioTableWidget

import resources.resources_rc


class PlaylistWidget(QWidget):
    audioChanged = Signal(AudioData)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.current_idx = -1

        self.playlist_model = PlaylistModel()
        self.combo_box_model = ComboBoxModel()

        self.combo_box_model.setTable("Playlist")
        self.combo_box_model.preupdated.connect(self.preupdateComboBox)
        self.combo_box_model.updated.connect(self.updateComboBox)

        self.combo_box = ComboBoxWidget(self)
        self.playlist_audio_table = PlaylistAudioTableWidget(self)
        self.button_up = PushButtonWidget(self)
        self.button_down = PushButtonWidget(self)

        self.combo_box.setModel(self.combo_box_model)
        self.combo_box.setCurrentIndex(-1)
        self.combo_box.lineEdit().setEnabled(False)
        self.combo_box.currentTextChanged.connect(self.playlist_audio_table.setPlaylistName)
        self.combo_box.currentTextChanged.connect(self.combo_box_model.setText)
        self.button_up.setIcon(QPixmap(":icon/chevron-up-white.svg"))
        self.button_up.clicked.connect(self.moveAudioUp)
        self.button_down.setIcon(QPixmap(":icon/chevron-down-white.svg"))
        self.button_down.clicked.connect(self.moveAudioDown)
        self.playlist_audio_table.selectionModel().selectionChanged.connect(self.onSelectionChanged)

        self.button_layout = HBoxLayoutWidget()
        self.button_layout.addWidget(self.button_up)
        self.button_layout.addWidget(self.button_down)

        self.main_layout = VBoxLayoutWidget()
        self.main_layout.addWidget(self.combo_box)
        self.main_layout.addWidget(self.playlist_audio_table)
        self.main_layout.addLayout(self.button_layout)

        self.setLayout(self.main_layout)

    # Need to save text before update
    def preupdateComboBox(self, text) -> None:
        self.temp_text = text

    def updateComboBox(self) -> None:
        self.combo_box.setEditText(self.temp_text)

    def onSelectionChanged(self, selected: QItemSelection, deselected: QItemSelection) -> None:
        self.playlist_model.setPlaylist(self.combo_box.currentText())
        self.current_idx = self.playlist_audio_table.selectionModel().selectedRows()[0].row()
        audio_data = self.playlist_model.audio_datas[self.current_idx]
        self.audioChanged.emit(audio_data)

    def next(self) -> None:
        if self.playlist_model.audio_datas:
            self.current_idx = (self.current_idx + 1) % len(self.playlist_model.audio_datas)
            audio_data = self.playlist_model.audio_datas[self.current_idx]
            self.audioChanged.emit(audio_data)

    def nextRandom(self) -> None:
        if self.playlist_model.audio_datas:
            current_idx = self.current_idx
            while self.current_idx == current_idx:
                self.current_idx = random.randint(0, len(self.playlist_model.audio_datas) - 1)
            audio_data = self.playlist_model.audio_datas[self.current_idx]
            self.audioChanged.emit(audio_data)

    def prev(self) -> None:
        if self.playlist_model.audio_datas:
            self.current_idx = (self.current_idx - 1) % len(self.playlist_model.audio_datas)
            audio_data = self.playlist_model.audio_datas[self.current_idx]
            self.audioChanged.emit(audio_data)

    def moveAudioUp(self) -> None:
        if self.playlist_audio_table.selectionModel().selectedRows() \
            and self.playlist_audio_table.selectionModel().selectedRows()[0].row() > 0:
            self.playlist_audio_table.moveUp()

    def moveAudioDown(self) -> None:
        if self.playlist_audio_table.selectionModel().selectedRows() \
            and self.playlist_audio_table.selectionModel().selectedRows()[0].row() + 1 < self.playlist_audio_table.playlist_audio_table_model.rowCount():
            self.playlist_audio_table.moveDown()
            