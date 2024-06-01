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

from view.dialog.new_audio_dialog import NewAudioDialog
from view.dialog.modify_audio_dialog import ModifyAudioDialog

from view.default.push_button_widget import PushButtonWidget
from view.default.v_box_layout_widget import VBoxLayoutWidget
from view.default.h_box_layout_widget import HBoxLayoutWidget

from view.widget.search_panel_widget import SearchPanelWidget
from view.widget.audio_table_widget import AudioTableWidget

class PlaylistLibraryWidget(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, Qt.GlobalColor.darkCyan)

        self.setAutoFillBackground(True) 
        self.setPalette(palette)

    def search(self) -> None:
        print("search")
        pass

    def newPlaylist(self) -> None:
        print("new")
        pass

    def deletePlaylist(self) -> None:
        print("delete")
        pass

    def addAudio(self) -> None:
        print("add")
        pass

    def modifyAudio(self) -> None:
        print("modify")
        pass
        
    def removeAudio(self) -> None:
        print("remove")
        pass