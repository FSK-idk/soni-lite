from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QDialog,
    QMessageBox
)
from PySide6.QtGui import (
    QScreen,
)

from model.data_base.data_base import data_base

from view.default.push_button_widget import PushButtonWidget
from view.default.v_box_layout_widget import VBoxLayoutWidget
from view.default.h_box_layout_widget import HBoxLayoutWidget

from view.tile.text_edit_tile import TextEditTile
from view.tile.line_edit_tile import LineEditTile

from view.widget.illustration_widget import IllustrationWidget
from view.widget.info_panel_widget import InfoPanelWidget


class AddAudioDialog(QDialog):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)

        # attribute

        self.id = ""

        # widget

        self.save_button = PushButtonWidget(self)
        self.cancel_button = PushButtonWidget(self)

        self.save_button.setText("Save")
        self.save_button.clicked.connect(self.save)
        self.cancel_button.setText("Cancel")
        self.cancel_button.clicked.connect(self.reject)

        # layout

        self.buttons_layout = HBoxLayoutWidget()
        self.buttons_layout.addWidget(self.cancel_button, 1)
        self.buttons_layout.addWidget(self.save_button, 1)

        self.main_layout = VBoxLayoutWidget()
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.addLayout(self.buttons_layout)

        self.setLayout(self.main_layout)
        
        # self

        self.setWindowTitle("Add audio")
        self.setFixedWidth(300)

        # center window
        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geometry = self.geometry()
        geometry.moveCenter(center)
        self.move(geometry.topLeft())
    
    def save(self):
        self.accept()