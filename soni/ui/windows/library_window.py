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
    QScrollArea
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

from modules.data_base import DataBase
from ui.widgets.search_panel_widget import SearchPanelWidget

class LibraryWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # name
        self.setWindowTitle("soni.library")

        # geometry
        self.setGeometry(0, 0, 800, 400)

        # center window
        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geometry = self.geometry()
        geometry.moveCenter(center)
        self.move(geometry.topLeft())

        # attributes
        self.data_base = DataBase()
        self.model = QSqlTableModel(self, self.data_base.data_base)
        self.model.setTable('Audio')
        self.model.select()

        self.table = QTableView()
        self.table.setModel(self.model)
        self.table.horizontalHeader().setFont(QFont(":/fonts/NotoSans.ttf",10))
        
        self.search_panel = SearchPanelWidget()
        self.search_button = QPushButton("Search")

        self.search_layout = QVBoxLayout()
        self.search_layout.addWidget(self.search_panel)
        self.search_layout.addWidget(self.search_button)

        # layout
        self.main_layout = QHBoxLayout()
        self.main_layout.addLayout(self.search_layout, 1)
        self.main_layout.addWidget(self.table, 3)

        # set layout
        self.widget = QWidget(self)
        self.widget.setLayout(self.main_layout)
        self.setCentralWidget(self.widget)

        # menu
        self.modify_track_action = QAction("modify", self)
        self.modify_track_action.triggered.connect(self.modifyTrack)
        self.menuBar().addAction(self.modify_track_action)

    def modifyTrack(self):
        pass