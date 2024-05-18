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
    QTextEdit,
    QFileDialog,
    QStyleOptionButton,
    QLineEdit,
    QMessageBox
)
from PySide6.QtGui import (
    QScreen,
    QAction,
    QFont,
)
from PySide6.QtCore import (
    Qt,
)
from PySide6.QtSql import (
    QSqlTableModel,
)

from ui.widgets.illustration_widget import IllustrationWidget
from ui.widgets.audio_info_panel_widget import AudioInfoPanelWidget

class NewAudioDialog(QDialog):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)

        # name

        self.setWindowTitle("New audio")

        # geometry

        self.setGeometry(0, 0, 600, 400)
        self.setMinimumSize(400, 400)

        # center window

        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geometry = self.geometry()
        geometry.moveCenter(center)
        self.move(geometry.topLeft())

        # widgets

        self.illustration = IllustrationWidget()
        self.path_line_edit = QLineEdit()
        self.path_button = QPushButton()
        self.audio_text = QTextEdit()
        self.search_panel = AudioInfoPanelWidget()

        self.path_button.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.save_button = QPushButton("Save")
        self.cancel_button = QPushButton("Cancel")

        self.path_button.clicked.connect(self.choose_file)
        self.save_button.clicked.connect(self.save)
        self.cancel_button.clicked.connect(self.cancel)

        # layout

        self.path_layout = QHBoxLayout()
        self.path_layout.addWidget(self.path_line_edit)
        self.path_layout.addWidget(self.path_button)

        self.left_layout = QVBoxLayout()
        self.left_layout.addWidget(self.illustration, 1)
        self.left_layout.addLayout(self.path_layout)
        self.left_layout.addWidget(self.audio_text, 2)

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.addWidget(self.cancel_button, 1)
        self.buttons_layout.addWidget(self.save_button, 1)

        self.right_layout = QVBoxLayout()
        self.right_layout.addWidget(self.search_panel)
        self.right_layout.addLayout(self.buttons_layout)

        self.main_layout = QHBoxLayout()
        self.main_layout.addLayout(self.left_layout, 1)
        self.main_layout.addLayout(self.right_layout, 3)

        self.setLayout(self.main_layout)
    
    def choose_file(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Open file",
            "",
            "audio file (*.mp3 *.aac *.ogg *wav);;All files (*.*)"
        )
        self.path_line_edit.setText(path)

    def save(self):
        info = self.search_panel.getInfo()
        if info.title == "":
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Attention")
            dlg.setText("You have not entered title")
            dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
            dlg.setIcon(QMessageBox.Icon.Warning)
            button = dlg.exec()            
            return
        self.accept()

    def cancel(self):
        self.reject()