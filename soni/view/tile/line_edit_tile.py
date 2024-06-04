from PySide6.QtWidgets import QWidget, QSizePolicy

from view.basic.label_widget import LabelWidget
from view.basic.line_edit_widget import LineEditWidget
from view.basic.v_box_layout_widget import VBoxLayoutWidget


class LineEditTile(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.title = LabelWidget(self)
        self.line_edit = LineEditWidget(self)

        self.main_layout = VBoxLayoutWidget()
        self.main_layout.addWidget(self.title)
        self.main_layout.addWidget(self.line_edit)

        self.setLayout(self.main_layout)

        self.setFixedHeight(self.main_layout.minimumSize().height())
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

    def setTitle(self, text: str) -> None:
        self.title.setText(text)

    def setText(self, text: str) -> None:
        self.line_edit.setText(text)

    def text(self) -> str:
        return self.line_edit.text()
    
    def clearInput(self) -> None:
        self.line_edit.setText("")
        self.line_edit.clearFocus()