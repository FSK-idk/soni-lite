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
)
from PySide6.QtGui import (
    QScreen,
    QAction
)
from PySide6.QtCore import (
    Qt
)


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

        # menu
        self.modify_track_action = QAction("modify", self)
        self.modify_track_action.triggered.connect(self.modify_track)
        self.menuBar().addAction(self.modify_track_action)

    def modify_track(self):
        pass