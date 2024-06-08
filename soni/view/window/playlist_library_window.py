from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QDialog
)
from PySide6.QtGui import QScreen, QAction

from view.dialog.new_playlist_dialog import NewPlaylistDialog
from view.dialog.delete_playlist_dialog import DeletePlaylistDialog
from view.dialog.add_audio_dialog import AddAudioDialog
from view.dialog.modify_audio_dialog import ModifyAudioDialog
from view.dialog.remove_audio_dialog import RemoveAudioDialog

from view.basic.h_box_layout_widget import HBoxLayoutWidget
from view.basic.v_box_layout_widget import VBoxLayoutWidget
from view.basic.push_button_widget import PushButtonWidget

from view.widget.playlist_panel_widget import PlaylistPanelWidget
from view.widget.playlist_audio_table_widget import PlaylistAudioTableWidget

class PlaylistLibraryWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.playlist_panel = PlaylistPanelWidget(self)
        self.playlist_audio_table = PlaylistAudioTableWidget(self)
        self.button_up = PushButtonWidget(self)
        self.button_down = PushButtonWidget(self)

        self.playlist_panel.changedPlaylist.connect(self.playlist_audio_table.setPlaylist)
        self.button_up.setText("up")
        self.button_up.clicked.connect(self.moveAudioUp)
        self.button_down.setText("down")
        self.button_down.clicked.connect(self.moveAudioDown)

        self.button_layout = HBoxLayoutWidget()
        self.button_layout.addWidget(self.button_up)
        self.button_layout.addWidget(self.button_down)

        self.right_layout = VBoxLayoutWidget()
        self.right_layout.addWidget(self.playlist_audio_table)
        self.right_layout.addLayout(self.button_layout)

        self.main_layout = HBoxLayoutWidget()
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.addWidget(self.playlist_panel, 1)
        self.main_layout.addLayout(self.right_layout, 3)

        self.widget = QWidget(self)
        self.widget.setLayout(self.main_layout)
        self.setCentralWidget(self.widget)

        self.new_playlist_action = QAction("new", self)
        self.new_playlist_action.triggered.connect(self.newPlaylist)
        self.menuBar().addAction(self.new_playlist_action)
        self.delete_playlist_action = QAction("delete", self)
        self.delete_playlist_action.triggered.connect(self.deletePlaylist)
        self.menuBar().addAction(self.delete_playlist_action)
        self.add_audio_action = QAction("add", self)
        self.add_audio_action.triggered.connect(self.addAudio)
        self.menuBar().addAction(self.add_audio_action)
        self.modify_audio_action = QAction("modify", self)
        self.modify_audio_action.triggered.connect(self.modifyAudio)
        self.menuBar().addAction(self.modify_audio_action)
        self.remove_audio_action = QAction("remove", self)
        self.remove_audio_action.triggered.connect(self.removeAudio)
        self.menuBar().addAction(self.remove_audio_action)

        self.setWindowTitle("playlist.library")
        self.setGeometry(0, 0, 800, 400)

        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geometry = self.geometry()
        geometry.moveCenter(center)
        self.move(geometry.topLeft())

    def moveAudioUp(self) -> None:
        if self.playlist_audio_table.selectionModel().selectedRows() \
            and self.playlist_audio_table.selectionModel().selectedRows()[0].row() > 0:
            self.playlist_audio_table.moveUp()
            # self.playlist_audio_table.updateTable()

    def moveAudioDown(self) -> None:
        if self.playlist_audio_table.selectionModel().selectedRows() \
            and self.playlist_audio_table.selectionModel().selectedRows()[0].row() + 1 < self.playlist_audio_table.playlist_audio_table_model.rowCount():
            self.playlist_audio_table.moveDown()
            # self.playlist_audio_table.updateTable()

    def newPlaylist(self) -> None:
        dialog = NewPlaylistDialog(self)
        if dialog.exec():
            self.playlist_audio_table.updateTable()
            self.playlist_panel.updatePanel()

    def deletePlaylist(self) -> None:
        if self.playlist_panel.playlist_table.selectionModel().selectedRows():
            dialog = DeletePlaylistDialog(self.playlist_panel.playlist_table.selectionModel().selectedRows()[0].data(), self)
            if dialog.exec():
                self.playlist_audio_table.updateTable()
                self.playlist_panel.updatePanel()

    def addAudio(self) -> None:
        if self.playlist_panel.playlist_table.selectionModel().selectedRows():
            dialog = AddAudioDialog(self.playlist_panel.playlist_table.selectionModel().selectedRows()[0].data(), self)
            if dialog.exec():
                self.playlist_audio_table.updateTable()
                self.playlist_panel.updatePanel()

    def modifyAudio(self) -> None:
        if self.playlist_audio_table.selectionModel().selectedRows():
            dialog = ModifyAudioDialog(self.playlist_audio_table.selectionModel().selectedRows()[0].data(), self)
            if dialog.exec():
                self.playlist_audio_table.updateTable()
                self.playlist_panel.updatePanel()

    def removeAudio(self) -> None:
        if self.playlist_audio_table.selectionModel().selectedRows() \
            and self.playlist_panel.playlist_table.selectionModel().selectedRows():
            dialog = RemoveAudioDialog(self.playlist_panel.playlist_table.selectionModel().selectedRows()[0].data(),
                                       self.playlist_audio_table.selectionModel().selectedRows()[0].data(), self)
            if dialog.exec():
                self.playlist_audio_table.updateTable()
                self.playlist_panel.updatePanel()