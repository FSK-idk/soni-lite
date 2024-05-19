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
)
from PySide6.QtGui import (
    QScreen,
    QAction,
    QFont
)
from PySide6.QtCore import (
    Qt,
    Signal
)
from PySide6.QtSql import (
    QSqlTableModel,
)

from modules.data_base import data_base

from ui.dialogs.new_audio_dialog import NewAudioDialog
from ui.dialogs.modify_audio_dialog import ModifyAudioDialog

from ui.widgets.pyside.push_button_widget import PushButtonWidget
from ui.widgets.pyside.v_box_layout_widget import VBoxLayoutWidget
from ui.widgets.pyside.h_box_layout_widget import HBoxLayoutWidget

from ui.widgets.search_info_panel_widget import SearchInfoPanelWidget
from ui.widgets.audio_table_widget import AudioTableWidget

class LibraryWindow(QMainWindow):
    # signals

    audioAdded = Signal()
    audioModified = Signal()

    def __init__(self) -> None:
        super().__init__()

        # widgets

        self.table = AudioTableWidget()
        self.search_panel = SearchInfoPanelWidget(self)
        self.search_button = PushButtonWidget(self)
        self.clear_button = PushButtonWidget(self)

        self.search_button.setText("Search")
        self.search_panel.shownParametersChanged.connect(self.table.onShownParametersChanged)
        self.clear_button.setText("Clear")
        self.clear_button.clicked.connect(self.search_panel.clearInput)

        self.table.onShownParametersChanged()

        # layout

        self.buttons_layout = HBoxLayoutWidget()
        self.buttons_layout.addWidget(self.search_button, 3)
        self.buttons_layout.addWidget(self.clear_button, 1)

        self.search_layout = VBoxLayoutWidget()
        self.search_layout.addWidget(self.search_panel)
        self.search_layout.addLayout(self.buttons_layout)

        self.main_layout = HBoxLayoutWidget()
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.addLayout(self.search_layout, 1)
        self.main_layout.addWidget(self.table, 3)

        self.widget = QWidget(self)
        self.widget.setLayout(self.main_layout)
        self.setCentralWidget(self.widget)

        # menu

        self.show_audio_action = QAction("audio", self)
        self.show_audio_action.triggered.connect(self.showAudio)
        self.menuBar().addAction(self.show_audio_action)

        self.show_playlist_action = QAction("playlist", self)
        self.show_playlist_action.triggered.connect(self.showPlaylist)
        self.menuBar().addAction(self.show_playlist_action)

        self.new_audio_action = QAction("new", self)
        self.new_audio_action.triggered.connect(self.newAudio)
        self.menuBar().addAction(self.new_audio_action)

        self.modify_audio_action = QAction("modify", self)
        self.modify_audio_action.triggered.connect(self.modifyAudio)
        self.menuBar().addAction(self.modify_audio_action)

        self.delete_audio_action = QAction("delete", self)
        self.delete_audio_action.triggered.connect(self.deleteAudio)
        self.menuBar().addAction(self.delete_audio_action)

        # self

        self.setWindowTitle("soni.library")
        self.setGeometry(0, 0, 800, 400)

        # center window
        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geometry = self.geometry()
        geometry.moveCenter(center)
        self.move(geometry.topLeft())

    def showAudio(self) -> None:
        pass

    def showPlaylist(self) -> None:
        pass

    def newAudio(self) -> None:
        dialog = NewAudioDialog(self)
        if dialog.exec():
            data_base.insert_audio(dialog.info)
            self.audioAdded.emit()
            self.table.onTableUpdate()
            self.search_panel.onTableUpdate()

    def modifyAudio(self) -> None:
        pass
        # dialog = ModifyAudioDialog(self)
        # if dialog.exec():
        #     print("OK")
        
    def deleteAudio(self) -> None:
        pass