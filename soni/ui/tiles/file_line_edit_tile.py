from PySide6.QtWidgets import QWidget, QSizePolicy, QFileDialog
from PySide6.QtCore import Signal

from ui.widgets.pyside.label_widget import LabelWidget
from ui.widgets.pyside.push_button_widget import PushButtonWidget
from ui.widgets.pyside.line_edit_widget import LineEditWidget
from ui.widgets.pyside.v_box_layout_widget import VBoxLayoutWidget
from ui.widgets.pyside.h_box_layout_widget import HBoxLayoutWidget

class FileLineEditTile(QWidget):
    # signals

    textChanged = Signal(str)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        # attributes
        
        self.filter = ""

        # widgets

        self.title = LabelWidget(self)
        self.line_edit = LineEditWidget(self)
        self.button = PushButtonWidget(self)

        self.line_edit.textChanged.connect(self.textChanged.emit)
        self.button.setText("...")
        self.button.setFixedWidth(30)
        self.button.clicked.connect(self.chooseFile)

        # layout

        self.bottom_layout = HBoxLayoutWidget()
        self.bottom_layout.addWidget(self.line_edit)
        self.bottom_layout.addWidget(self.button)

        self.main_layout = VBoxLayoutWidget()
        self.main_layout.addWidget(self.title)
        self.main_layout.addLayout(self.bottom_layout)

        self.setLayout(self.main_layout)

        # geometry

        self.setFixedHeight(self.main_layout.minimumSize().height())
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

    def setFilter(self, filter: str):
        self.filter = filter

    def chooseFile(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Open file",
            "",
            self.filter
        )
        self.line_edit.setText(path)

    def setTitle(self, text: str) -> None:
        self.title.setText(text)

    def setText(self, text: str) -> None:
        self.line_edit.setText(text)

    def text(self) -> str:
        return self.line_edit.text()