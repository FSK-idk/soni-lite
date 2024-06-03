from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QHBoxLayout,
    QVBoxLayout,
    QStackedLayout,
    QSlider,
    QWidget,
    QLabel,
    QPushButton,
    QSizePolicy,
    QMenuBar,
    QTableView,
    QScrollArea,
    QDialog,
    QAbstractItemView,
    QMessageBox
)
from PySide6.QtGui import (
    QScreen,
    QAction,
    QPalette,
    QFont
)
from PySide6.QtCore import (
    Qt,
    Signal
)
from PySide6.QtSql import (
    QSqlTableModel,
)

from model.data_base.data_base import data_base

from view.dialog.new_playlist_dialog import NewPlaylistDialog
from view.dialog.add_audio_dialog import AddAudioDialog
from view.dialog.modify_audio_dialog import ModifyAudioDialog

from view.default.push_button_widget import PushButtonWidget
from view.default.v_box_layout_widget import VBoxLayoutWidget
from view.default.h_box_layout_widget import HBoxLayoutWidget

from view.widget.playlist_panel_widget import PlaylistPanelWidget
from view.widget.playlist_audio_table_widget import PlaylistAudioTableWidget


class PlaylistLibraryWidget(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        # widget

        self.playlist_panel = PlaylistPanelWidget(self)
        self.audio_table = PlaylistAudioTableWidget(self)

        self.playlist_panel.changedPlaylist.connect(self.audio_table.setPlaylist)

        # layout

        self.main_layout = HBoxLayoutWidget()
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.addWidget(self.playlist_panel, 1)
        self.main_layout.addWidget(self.audio_table, 3)

        self.setLayout(self.main_layout)


        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, Qt.GlobalColor.darkCyan)

        self.setAutoFillBackground(True) 
        self.setPalette(palette)

    def newPlaylist(self) -> None:
        dialog = NewPlaylistDialog(self)
        if dialog.exec():
            data_base.insert_playlist(dialog.name)
            self.playlist_panel.updatePanel()

    def deletePlaylist(self) -> None:
        if self.playlist_panel.table.selectionModel().selectedRows():
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Delete playlist")
            dlg.setText("Are you sure?")
            dlg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.No)
            dlg.setIcon(QMessageBox.Icon.Warning)
            btn = dlg.exec()
            if btn == QMessageBox.StandardButton.Ok:
                data_base.delete_playlist(self.playlist_panel.table.selectionModel().selectedRows()[0].data())
                self.playlist_panel.updatePanel()
                self.audio_table.updateTable()

    def addAudio(self) -> None:
        print("add")
        if self.playlist_panel.table.selectionModel().selectedRows():
            dialog = AddAudioDialog(self)
            if dialog.exec():
                # data_base.insert_playlist_audio(self.playlist_panel.table.selectionModel().selectedRows()[0].data())
                # self.playlist_panel.updatePanel()
                # self.audio_table.updateTable()
                pass

    def modifyAudio(self) -> None:
        print("modify")
        pass
        
    def removeAudio(self) -> None:
        print("remove")
        pass