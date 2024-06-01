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

class AudioLibraryWidget(QWidget):
    # signals

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        # widgets

        self.table = AudioTableWidget()
        self.search_panel = SearchPanelWidget(self)
        self.search_button = PushButtonWidget(self)
        self.clear_button = PushButtonWidget(self)

        self.search_button.setText("Search")
        self.search_panel.headersChanged.connect(self.table.updateHeaders)
        self.search_button.clicked.connect(self.search)
        self.clear_button.setText("Clear")
        self.clear_button.clicked.connect(self.search_panel.clearPanel)

        self.table.updateHeaders()

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

        self.setLayout(self.main_layout)

    def search(self) -> None:
        self.table.search(self.search_panel.getSearchData())

    def newAudio(self) -> None:
        dialog = NewAudioDialog(self)
        if dialog.exec():
            data_base.insert_audio(dialog.info)
            self.table.updateTable()
            self.search_panel.updatePanel()

    def modifyAudio(self) -> None:
        if self.table.selectionModel().selectedRows():
            dialog = ModifyAudioDialog(self.table.selectionModel().selectedRows()[0].data(), self)
            if dialog.exec():
                data_base.update_audio(dialog.new_info, dialog.audio_id)
                self.table.updateTable()
                self.search_panel.updatePanel()
        
    def deleteAudio(self) -> None:
        if self.table.selectionModel().selectedRows():
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Delete audio")
            dlg.setText("Are you sure?")
            dlg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.No)
            dlg.setIcon(QMessageBox.Icon.Warning)
            btn = dlg.exec()
            if btn == QMessageBox.StandardButton.Ok:
                data_base.delete_audio(self.table.selectionModel().selectedRows()[0].data())
                self.table.updateTable()
                self.search_panel.updatePanel()

