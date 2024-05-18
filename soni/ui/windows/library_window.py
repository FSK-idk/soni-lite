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
    QDialog
)
from PySide6.QtGui import (
    QScreen,
    QAction,
    QFont
)
from PySide6.QtCore import (
    Qt,
)
from PySide6.QtSql import (
    QSqlTableModel,
)

from modules.data_base import data_base

from ui.dialogs.new_audio_dialog import NewAudioDialog

from ui.widgets.search_info_panel_widget import SearchInfoPanelWidget

class LibraryWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        # attributes

        self.model = QSqlTableModel(self, data_base.data_base)
        self.model.setTable('Audio')
        self.model.select()

        self.table = QTableView()
        self.table.setModel(self.model)
        self.table.horizontalHeader().setFont(QFont(":/fonts/NotoSans.ttf",10))
        
        self.search_panel = SearchInfoPanelWidget()
        self.search_button = QPushButton("Search")

        self.search_layout = QVBoxLayout()
        self.search_layout.addWidget(self.search_panel)
        self.search_layout.addWidget(self.search_button)

        # layout

        self.main_layout = QHBoxLayout()
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.addLayout(self.search_layout, 1)
        self.main_layout.addWidget(self.table, 3)

        self.widget = QWidget(self)
        self.widget.setLayout(self.main_layout)
        self.setCentralWidget(self.widget)

        # menu

        self.new_track_action = QAction("new", self)
        self.new_track_action.triggered.connect(self.newAudio)
        self.menuBar().addAction(self.new_track_action)

        self.modify_track_action = QAction("modify", self)
        self.modify_track_action.triggered.connect(self.modifyTrack)
        self.menuBar().addAction(self.modify_track_action)
        
        # self

        self.setWindowTitle("soni.library")
        self.setGeometry(0, 0, 800, 400)

        # center window
        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geometry = self.geometry()
        geometry.moveCenter(center)
        self.move(geometry.topLeft())

    def modifyTrack(self) -> None:
        pass

    def newAudio(self) -> None:
        dlg = NewAudioDialog(self)
        if dlg.exec():
            print ("OK")