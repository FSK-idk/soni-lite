from typing import List

from PySide6.QtWidgets import QWidget, QSizePolicy
from PySide6.QtCore import Signal

from ui.widgets.pyside.label_widget import LabelWidget
from ui.widgets.pyside.combo_box_widget import ComboBoxWidget
from ui.widgets.pyside.v_box_layout_widget import VBoxLayoutWidget

class ComboBoxTile(QWidget):
    # signals

    textChanged = Signal(str)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        # widgets

        self.title = LabelWidget(self)
        self.combo_box = ComboBoxWidget(self)

        self.combo_box.currentIndexChanged.connect(self.textChanged.emit)

        # layout

        self.main_layout = VBoxLayoutWidget()
        self.main_layout.addWidget(self.title)
        self.main_layout.addWidget(self.combo_box)

        self.setLayout(self.main_layout)

        # self

        self.setFixedHeight(self.main_layout.minimumSize().height())
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

    def setTitle(self, text: str) -> None:
        self.title.setText(text)

    def addItem(self, item: str) -> None:
        self.combo_box.addItem(item)

    def addItems(self, items: List[str]) -> None:
        self.combo_box.addItems(items)

    def text(self) -> str:
        return self.combo_box.currentText()