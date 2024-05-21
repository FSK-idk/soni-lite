from PySide6.QtWidgets import QWidget, QSizePolicy
from PySide6.QtCore import Signal

from view.default.label_widget import LabelWidget
from view.default.line_edit_widget import LineEditWidget
from view.default.v_box_layout_widget import VBoxLayoutWidget

class LineEditTile(QWidget):
    # signals

    textChanged = Signal(str)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        # widgets

        self.title = LabelWidget(self)
        self.line_edit = LineEditWidget(self)

        self.line_edit.textChanged.connect(self.textChanged.emit)

        # layout

        self.main_layout = VBoxLayoutWidget()
        self.main_layout.addWidget(self.title)
        self.main_layout.addWidget(self.line_edit)

        self.setLayout(self.main_layout)

        # geometry

        self.setFixedHeight(self.main_layout.minimumSize().height())
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

    def clearTile(self) -> None:
        self.line_edit.setText("")
        self.line_edit.clearFocus()

    def setTitle(self, text: str) -> None:
        self.title.setText(text)

    def setText(self, text: str) -> None:
        self.line_edit.setText(text)

    def text(self) -> str:
        return self.line_edit.text()