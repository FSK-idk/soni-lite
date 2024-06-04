from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
)
from PySide6.QtGui import (
    QScreen,
    QAction,
)

from view.dialog.new_audio_dialog import NewAudioDialog
from view.dialog.modify_audio_dialog import ModifyAudioDialog
from view.dialog.delete_audio_dialog import DeleteAudioDialog

from view.basic.h_box_layout_widget import HBoxLayoutWidget

from view.widget.search_panel_widget import SearchPanelWidget
from view.widget.audio_table_widget import AudioTableWidget


class AudioLibraryWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.audio_table = AudioTableWidget()
        self.search_panel = SearchPanelWidget(self)

        self.search_panel.headerChanged.connect(self.audio_table.updateTable)
        self.search_panel.searchClicked.connect(self.audio_table.search)

        self.main_layout = HBoxLayoutWidget()
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.addWidget(self.search_panel, 1)
        self.main_layout.addWidget(self.audio_table, 3)

        self.setLayout(self.main_layout)

        self.widget = QWidget(self)
        self.widget.setLayout(self.main_layout)
        self.setCentralWidget(self.widget)

        self.new_audio_action = QAction("new", self)
        self.new_audio_action.triggered.connect(self.newAudio)
        self.menuBar().addAction(self.new_audio_action)
        self.modify_audio_action = QAction("modify", self)
        self.modify_audio_action.triggered.connect(self.modifyAudio)
        self.menuBar().addAction(self.modify_audio_action)
        self.delete_audio_action = QAction("delete", self)
        self.delete_audio_action.triggered.connect(self.deleteAudio)
        self.menuBar().addAction(self.delete_audio_action)

        self.setWindowTitle("audio.library")
        self.setGeometry(0, 0, 800, 400)

        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geometry = self.geometry()
        geometry.moveCenter(center)
        self.move(geometry.topLeft())

    def newAudio(self) -> None:
        dialog = NewAudioDialog(self)
        if dialog.exec():
            self.audio_table.updateTable()
            self.search_panel.updatePanel()

    def modifyAudio(self) -> None:
        if self.audio_table.selectionModel().selectedRows():
            dialog = ModifyAudioDialog(self.audio_table.selectionModel().selectedRows()[0].data(), self)
            if dialog.exec():
                self.audio_table.updateTable()
                self.search_panel.updatePanel()
        
    def deleteAudio(self) -> None:
        if self.audio_table.selectionModel().selectedRows():
            dialog = DeleteAudioDialog(self.audio_table.selectionModel().selectedRows()[0].data(), self)
            if dialog.exec():
                self.audio_table.updateTable()
                self.search_panel.updatePanel()