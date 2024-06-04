from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QDialog,
    QMessageBox
)
from PySide6.QtGui import QScreen

from etc.data_base import data_base

from view.basic.push_button_widget import PushButtonWidget
from view.basic.v_box_layout_widget import VBoxLayoutWidget
from view.basic.h_box_layout_widget import HBoxLayoutWidget

from view.tile.line_edit_tile import LineEditTile


class NewPlaylistDialog(QDialog):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)

        self.name = ""

        self.line_edit = LineEditTile(self)
        self.save_button = PushButtonWidget(self)
        self.cancel_button = PushButtonWidget(self)

        self.line_edit.setTitle("Name")
        self.save_button.setText("Save")
        self.save_button.clicked.connect(self.save)
        self.cancel_button.setText("Cancel")
        self.cancel_button.clicked.connect(self.reject)

        self.buttons_layout = HBoxLayoutWidget()
        self.buttons_layout.addWidget(self.save_button, 1)
        self.buttons_layout.addWidget(self.cancel_button, 1)

        self.main_layout = VBoxLayoutWidget()
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.addWidget(self.line_edit)
        self.main_layout.addLayout(self.buttons_layout)

        self.setLayout(self.main_layout)
        
        self.setWindowTitle("new.playlist")
        self.setFixedWidth(300)
        self.setMinimumWidth(200)
        self.setMaximumHeight(self.minimumHeight())

        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geometry = self.geometry()
        geometry.moveCenter(center)
        self.move(geometry.topLeft())
    
    def save(self):
        self.name = self.line_edit.text()
        if self.name == "":
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Attention")
            dlg.setText("You have not entered name")
            dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
            dlg.setIcon(QMessageBox.Icon.Warning)
            dlg.exec()
            return
        id = data_base.selectPlaylistId(self.name)
        if id:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Attention")
            dlg.setText("Playlist already exists")
            dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
            dlg.setIcon(QMessageBox.Icon.Warning)
            dlg.exec()
            return
        data_base.insertPlaylist(self.name)
        self.accept()