from PySide6.QtWidgets import (
    QWidget,
    QTableView,
    QAbstractItemView,
    QHeaderView,
)
from PySide6.QtGui import QFont ,QPalette
from PySide6.QtCore import Qt, Signal, QItemSelection

from etc.audio_data import AudioData

from model.combo_box_model import ComboBoxModel
from model.playlist_model import PlaylistModel, LoopFormat

from view.basic.v_box_layout_widget import VBoxLayoutWidget
from view.basic.h_box_layout_widget import HBoxLayoutWidget
from view.basic.combo_box_widget import ComboBoxWidget
from view.basic.push_button_widget import PushButtonWidget

from view.widget.playlist_audio_table_widget import PlaylistAudioTableWidget


class PlaylistWidget(QWidget):
    audioChanged = Signal(AudioData)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.random = False
        self.loop_format = LoopFormat.loop_none
        self.current_idx = -1

        self.playlist_model = PlaylistModel()
        self.combo_box_model = ComboBoxModel()


        self.combo_box_model.setTable("Playlist")

        self.combo_box = ComboBoxWidget(self)
        self.playlist_audio_table = PlaylistAudioTableWidget(self)
        self.button_up = PushButtonWidget(self)
        self.button_down = PushButtonWidget(self)

        self.combo_box.setModel(self.combo_box_model)
        self.combo_box.setCurrentIndex(-1)
        self.combo_box.lineEdit().setEnabled(False)
        self.combo_box.currentTextChanged.connect(self.playlist_model.setPlaylist)
        self.button_up.setText("up")
        self.button_up.clicked.connect(self.moveAudioUp)
        self.button_down.setText("down")
        self.button_down.clicked.connect(self.moveAudioDown)
        self.playlist_model.playlistChanged.connect(self.playlist_audio_table.setPlaylist)
        self.playlist_audio_table.selectionModel().selectionChanged.connect(self.onSelectionChanged)

        self.button_layout = HBoxLayoutWidget()
        self.button_layout.addWidget(self.button_up)
        self.button_layout.addWidget(self.button_down)

        self.main_layout = VBoxLayoutWidget()
        self.main_layout.addWidget(self.combo_box)
        self.main_layout.addWidget(self.playlist_audio_table)
        self.main_layout.addLayout(self.button_layout)

        self.setLayout(self.main_layout)

    def onSelectionChanged(self, selected: QItemSelection, deselected: QItemSelection) -> None:
        self.current_idx = self.playlist_audio_table.selectionModel().selectedRows(2)[0].data() - 1
        audio_data = self.playlist_model.audio_datas[self.current_idx]
        self.audioChanged.emit(audio_data)

    def next(self) -> AudioData:
        audio_data = AudioData()
        if self.current_idx != -1:
            match self.loop_format:
                case LoopFormat.loop_none:
                    audio_data = self.playlist_model.audio_datas[self.current_idx]
                case LoopFormat.loop_playlist:
                    self.current_idx += 1
                    self.current_idx %= len(self.playlist_model.audio_datas)
                    audio_data = self.playlist_model.audio_datas[self.current_idx]
                case LoopFormat.loop_audio:
                    self.current_idx += 1
                    if self.current_idx >= len(self.playlist_model.audio_datas):
                        self.current_idx = -1
                    else:
                        audio_data = self.playlist_model.audio_datas[self.current_idx]
        return audio_data

    def moveAudioUp(self) -> None:
        if self.playlist_audio_table.selectionModel().selectedRows() \
            and self.playlist_audio_table.selectionModel().selectedRows()[0].row() > 0:
            self.playlist_audio_table.moveUp()

    def moveAudioDown(self) -> None:
        if self.playlist_audio_table.selectionModel().selectedRows() \
            and self.playlist_audio_table.selectionModel().selectedRows()[0].row() + 1 < self.playlist_audio_table.playlist_audio_table_model.rowCount():
            self.playlist_audio_table.moveDown()

    def text(self, st: str = "!@3") -> None:
        print("test", st)
        
        
        pass