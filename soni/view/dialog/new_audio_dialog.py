from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QDialog,
    QMessageBox
)
from PySide6.QtGui import (
    QScreen,
)
from PySide6.QtCore import Qt

from etc.data_base import data_base
from etc.audio_data import AudioData

from view.basic.push_button_widget import PushButtonWidget
from view.basic.v_box_layout_widget import VBoxLayoutWidget
from view.basic.h_box_layout_widget import HBoxLayoutWidget

from view.tile.text_edit_tile import TextEditTile

from view.widget.illustration_widget import IllustrationWidget
from view.widget.audio_panel_widget import AudioPanelWidget


class NewAudioDialog(QDialog):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)

        self.audio_data = AudioData()

        self.illustration = IllustrationWidget(self)
        self.text = TextEditTile(self)
        self.audio_panel = AudioPanelWidget(self)
        self.save_button = PushButtonWidget(self)
        self.cancel_button = PushButtonWidget(self)

        self.text.setTitle("Text")
        self.save_button.setText("Save")
        self.save_button.clicked.connect(self.save)
        self.cancel_button.setText("Cancel")
        self.cancel_button.clicked.connect(self.reject)

        self.left_layout = VBoxLayoutWidget()
        self.left_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.left_layout.addWidget(self.illustration, 1)
        self.left_layout.addWidget(self.text, 2)

        self.buttons_layout = HBoxLayoutWidget()
        self.buttons_layout.addWidget(self.save_button, 1)
        self.buttons_layout.addWidget(self.cancel_button, 1)

        self.right_layout = VBoxLayoutWidget()
        self.right_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.right_layout.addWidget(self.audio_panel)
        self.right_layout.addLayout(self.buttons_layout)
        
        self.main_layout = HBoxLayoutWidget()
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.addLayout(self.left_layout, 2)
        self.main_layout.addLayout(self.right_layout, 3)

        self.setLayout(self.main_layout)
        
        self.setWindowTitle("New audio")
        self.setGeometry(0, 0, 600, 400)
        self.setMinimumSize(400, 400)

        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geometry = self.geometry()
        geometry.moveCenter(center)
        self.move(geometry.topLeft())
    
    def save(self):
        self.audio_data = self.audio_panel.audioData()
        self.audio_data.text = self.text.text()
        if self.audio_data.name == "":
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Attention")
            dlg.setText("You have not entered the title")
            dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
            dlg.setIcon(QMessageBox.Icon.Warning)
            dlg.exec()
            return
        data_base.insertAudio(self.audio_data)
        self.accept()