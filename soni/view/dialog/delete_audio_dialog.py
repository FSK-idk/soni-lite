from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QDialog,
)
from PySide6.QtGui import (
    QScreen,
)
from PySide6.QtCore import Qt

from etc.data_base import data_base

from view.basic.push_button_widget import PushButtonWidget
from view.basic.label_widget import LabelWidget
from view.basic.v_box_layout_widget import VBoxLayoutWidget
from view.basic.h_box_layout_widget import HBoxLayoutWidget


class DeleteAudioDialog(QDialog):
    def __init__(self, id: int, parent: QWidget | None = None):
        super().__init__(parent)

        self.id = id

        self.label = LabelWidget(self)
        self.yes_button = PushButtonWidget(self)
        self.no_button = PushButtonWidget(self)

        self.label.setText("Are you sure?")
        self.yes_button.setText("Yes")
        self.yes_button.clicked.connect(self.yes)
        self.no_button.setText("No")
        self.no_button.clicked.connect(self.reject)

        self.buttons_layout = HBoxLayoutWidget()
        self.buttons_layout.addWidget(self.yes_button, 1)
        self.buttons_layout.addWidget(self.no_button, 1)

        self.main_layout = VBoxLayoutWidget()
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.addWidget(self.label)
        self.main_layout.addLayout(self.buttons_layout)

        self.setLayout(self.main_layout)
        
        self.setWindowTitle("Delete audio")
        self.setFixedWidth(300)
        self.setMinimumWidth(200)
        self.setMaximumHeight(self.minimumHeight())

        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geometry = self.geometry()
        geometry.moveCenter(center)
        self.move(geometry.topLeft())
    
    def yes(self):
        data_base.deleteAudio(self.id)
        self.accept()