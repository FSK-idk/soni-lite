from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QToolBar
from PySide6.QtGui import QScreen, QAction, QPixmap
from PySide6.QtCore import Qt

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

import resources.resources_rc


class PlaylistLibraryWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.playlist_panel = PlaylistPanelWidget(self)
        self.playlist_audio_table = PlaylistAudioTableWidget(self)
        self.button_up = PushButtonWidget(self)
        self.button_down = PushButtonWidget(self)

        self.playlist_panel.changedPlaylist.connect(self.playlist_audio_table.setPlaylistId)
        self.button_up.setIcon(QPixmap(":icon/chevron-up-white.svg"))
        self.button_up.clicked.connect(self.moveAudioUp)
        self.button_down.setIcon(QPixmap(":icon/chevron-down-white.svg"))
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

        self.toolbar = QToolBar(self)
        self.toolbar.setFloatable(False)
        self.toolbar.setMovable(False)
        self.addToolBar(self.toolbar)
        self.toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.new_playlist_action = QAction(QPixmap(":icon/folder-plus-white.svg"), "new", self)
        self.new_playlist_action.triggered.connect(self.newPlaylist)
        self.toolbar.addAction(self.new_playlist_action)
        self.delete_playlist_action = QAction(QPixmap(":icon/folder-x-white.svg"), "delete", self)
        self.delete_playlist_action.triggered.connect(self.deletePlaylist)
        self.toolbar.addAction(self.delete_playlist_action)
        self.add_audio_action = QAction(QPixmap(":icon/file-plus-white.svg"), "add", self)
        self.add_audio_action.triggered.connect(self.addAudio)
        self.toolbar.addAction(self.add_audio_action)
        self.modify_audio_action = QAction(QPixmap(":icon/pencil-white.svg"), "modify", self)
        self.modify_audio_action.triggered.connect(self.modifyAudio)
        self.toolbar.addAction(self.modify_audio_action)
        self.remove_audio_action = QAction(QPixmap(":icon/file-minus-white.svg"), "remove", self)
        self.remove_audio_action.triggered.connect(self.removeAudio)
        self.toolbar.addAction(self.remove_audio_action)

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

    def moveAudioDown(self) -> None:
        if self.playlist_audio_table.selectionModel().selectedRows() \
            and self.playlist_audio_table.selectionModel().selectedRows()[0].row() + 1 < self.playlist_audio_table.playlist_audio_table_model.rowCount():
            self.playlist_audio_table.moveDown()

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