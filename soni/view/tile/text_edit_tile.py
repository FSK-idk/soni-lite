from PySide6.QtWidgets import QWidget, QSizePolicy

from view.basic.label_widget import LabelWidget
from view.basic.text_edit_widget import TextEditWidget
from view.basic.v_box_layout_widget import VBoxLayoutWidget


class TextEditTile(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.title = LabelWidget(self)
        self.text_edit = TextEditWidget(self)

        self.main_layout = VBoxLayoutWidget()
        self.main_layout.addWidget(self.title)
        self.main_layout.addWidget(self.text_edit)

        self.setLayout(self.main_layout)

        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

    def setTitle(self, text: str) -> None:
        self.title.setText(text)

    def text(self) -> str:
        return self.text_edit.toPlainText()

    def clearInput(self) -> None:
        self.text_edit.setText("")
        self.text_edit.clearFocus()
