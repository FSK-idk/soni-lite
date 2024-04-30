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
)
from PySide6.QtGui import (
    QScreen,
    QAction,
)
from PySide6.QtCore import (
    Qt,
)
from PySide6.QtSql import (
    QSqlTableModel,
)

from modules.data_base import DataBase

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

        self.setCentralWidget(self.table)

        # menu
        self.modify_track_action = QAction("modify", self)
        self.modify_track_action.triggered.connect(self.modifyTrack)
        self.menuBar().addAction(self.modify_track_action)

    def modifyTrack(self):
        pass