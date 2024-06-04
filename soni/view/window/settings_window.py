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
    QTextEdit,
)
from PySide6.QtGui import (
    QScreen,
    QAction
)
from PySide6.QtCore import (
    Qt
)

from view.basic.push_button_widget import PushButtonWidget
from view.basic.label_widget import LabelWidget
from view.basic.line_edit_widget import LineEditWidget
from view.basic.check_box_widget import CheckBoxWidget
from view.basic.v_box_layout_widget import VBoxLayoutWidget
from view.basic.combo_box_widget import ComboBoxWidget
from view.basic.text_edit_widget import TextEditWidget

from view.tile.push_line_edit_tile import PushLineEditTile


class SettingsWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()


        # TODO: debug

        # widgets

        self.button = PushButtonWidget(self)
        self.button.setText("Button")

        self.label = LabelWidget(self)
        self.label.setText("Label")

        self.line_edit = LineEditWidget(self)
        self.line_edit.setText("Line edit")

        self.check_box = CheckBoxWidget(self)
        self.check_box.setText("Check box")

        self.combo_box = ComboBoxWidget(self)

        self.text_edit = TextEditWidget(self)

        # layout

        self.main_layout = VBoxLayoutWidget()
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.addWidget(self.button)
        self.main_layout.addWidget(self.label)
        self.main_layout.addWidget(self.line_edit)
        self.main_layout.addWidget(self.check_box)
        self.main_layout.addWidget(self.text_edit)
        self.main_layout.addWidget(self.combo_box)

        # print(self.button.height())
        # print(self.label.height())
        # print(self.line_edit.height())
        # print(self.check_box.height())
        # print(self.combo_box.height())

        self.widget = QWidget()
        self.widget.setLayout(self.main_layout)
        self.setCentralWidget(self.widget)

        # self

        self.setWindowTitle("settings")
        self.setGeometry(0, 0, 800, 400)

        # center window
        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geometry = self.geometry()
        geometry.moveCenter(center)
        self.move(geometry.topLeft())
