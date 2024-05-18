from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QDialog,
    QMessageBox
)
from PySide6.QtGui import (
    QScreen,
)

from modules.audio_info import AudioInfo

from ui.widgets.pyside.push_button_widget import PushButtonWidget
from ui.widgets.pyside.v_box_layout_widget import VBoxLayoutWidget
from ui.widgets.pyside.h_box_layout_widget import HBoxLayoutWidget

from ui.widgets.illustration_widget import IllustrationWidget
from ui.widgets.audio_info_panel_widget import AudioInfoPanelWidget

from ui.tiles.text_edit_tile import TextEditTile

class NewAudioDialog(QDialog):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)

        # attributes

        self.info = AudioInfo()

        # widgets

        self.illustration = IllustrationWidget()
        self.text = TextEditTile()
        self.search_panel = AudioInfoPanelWidget()
        self.save_button = PushButtonWidget(self)
        self.cancel_button = PushButtonWidget(self)

        self.text.setTitle("Text")
        self.save_button.setText("Save")
        self.save_button.clicked.connect(self.save)
        self.cancel_button.setText("Cancel")
        self.cancel_button.clicked.connect(self.cancel)

        # layout

        self.left_layout = VBoxLayoutWidget()
        self.left_layout.addWidget(self.illustration, 1)
        self.left_layout.addWidget(self.text, 2)

        self.buttons_layout = HBoxLayoutWidget()
        self.buttons_layout.addWidget(self.cancel_button, 1)
        self.buttons_layout.addWidget(self.save_button, 1)

        self.right_layout = VBoxLayoutWidget()
        self.right_layout.addWidget(self.search_panel)
        self.right_layout.addLayout(self.buttons_layout)

        self.main_layout = HBoxLayoutWidget()
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.addLayout(self.left_layout, 2)
        self.main_layout.addLayout(self.right_layout, 3)

        self.setLayout(self.main_layout)
        
        # self

        self.setWindowTitle("New audio")
        self.setGeometry(0, 0, 600, 400)
        self.setMinimumSize(400, 400)

        # center window
        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geometry = self.geometry()
        geometry.moveCenter(center)
        self.move(geometry.topLeft())
    
    def save(self):
        self.info = self.search_panel.getAudioInfo()
        if self.info.title == "":
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Attention")
            dlg.setText("You have not entered title")
            dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
            dlg.setIcon(QMessageBox.Icon.Warning)
            button = dlg.exec()            
            return
        self.info.text = self.text.text()
        self.accept()

    def cancel(self):
        self.reject()