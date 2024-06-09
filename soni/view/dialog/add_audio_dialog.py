from PySide6.QtWidgets import QApplication, QWidget, QDialog, QMessageBox
from PySide6.QtGui import QScreen, QPixmap
from PySide6.QtCore import Qt

from etc.data_base import data_base

from view.basic.push_button_widget import PushButtonWidget
from view.basic.v_box_layout_widget import VBoxLayoutWidget
from view.basic.h_box_layout_widget import HBoxLayoutWidget

from view.widget.search_panel_widget import SearchPanelWidget
from view.widget.audio_table_widget import AudioTableWidget

import resources.resources_rc


class AddAudioDialog(QDialog):
    def __init__(self, playlist_id: str, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.playlist_id = playlist_id

        self.audio_table = AudioTableWidget()
        self.search_panel = SearchPanelWidget(self)
        self.add_button = PushButtonWidget(self)
        self.cancel_button = PushButtonWidget(self)

        self.search_panel.headerChanged.connect(self.audio_table.updateTable)
        self.search_panel.searchClicked.connect(self.audio_table.search)

        self.add_button.setIcon(QPixmap(":icon/save-white.svg"))
        self.add_button.setText("add")
        self.add_button.clicked.connect(self.add)
        self.cancel_button.setIcon(QPixmap(":icon/ban-white.svg"))
        self.cancel_button.setText("cancel")
        self.cancel_button.clicked.connect(self.reject)

        self.buttons_layout = HBoxLayoutWidget()
        self.buttons_layout.addWidget(self.add_button)
        self.buttons_layout.addWidget(self.cancel_button)

        self.right_layout = VBoxLayoutWidget()
        self.right_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.right_layout.addWidget(self.audio_table)
        self.right_layout.addLayout(self.buttons_layout)

        self.main_layout = HBoxLayoutWidget()
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.addWidget(self.search_panel, 1)
        self.main_layout.addLayout(self.right_layout, 3)

        self.setLayout(self.main_layout)
        
        self.setWindowTitle("add.audio")
        self.setWindowIcon(QPixmap(":image/icon-s.png"))
        self.setGeometry(0, 0, 800, 400)

        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geometry = self.geometry()
        geometry.moveCenter(center)
        self.move(geometry.topLeft())
    
    def add(self) -> None:
        if not self.audio_table.selectionModel().selectedRows():
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Attention")
            dlg.setText("You have not chosen audio")
            dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
            dlg.setIcon(QMessageBox.Icon.Warning)
            dlg.exec()
            return
        
        if data_base.findPlaylistAudio(self.playlist_id, self.audio_table.selectionModel().selectedRows()[0].data()):
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Attention")
            dlg.setText("Audio already exists")
            dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
            dlg.setIcon(QMessageBox.Icon.Warning)
            dlg.exec()
            return

        data_base.insertPlaylistAudio(self.playlist_id, self.audio_table.selectionModel().selectedRows()[0].data())
        self.accept()