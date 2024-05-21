from PySide6.QtWidgets import QWidget, QSizePolicy

from view.default.label_widget import LabelWidget
from view.default.text_edit_widget import TextEditWidget
from view.default.v_box_layout_widget import VBoxLayoutWidget

class TextEditTile(QWidget):
    # signals

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        # widgets

        self.title = LabelWidget(self)
        self.text_edit = TextEditWidget(self)

        # layout

        self.main_layout = VBoxLayoutWidget()
        self.main_layout.addWidget(self.title)
        self.main_layout.addWidget(self.text_edit)

        self.setLayout(self.main_layout)

        # geometry

        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

    def clearTile(self) -> None:
        self.text_edit.setText("")
        self.text_edit.clearFocus()

    def setTitle(self, text: str) -> None:
        self.title.setText(text)

    def text(self) -> str:
        return self.text_edit.toPlainText()