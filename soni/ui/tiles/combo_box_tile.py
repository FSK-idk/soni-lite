from typing import List

from PySide6.QtWidgets import QWidget, QSizePolicy
from PySide6.QtCore import Signal, QAbstractItemModel

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

    def setEditable(self, editable: bool) -> None:
        self.combo_box.setEditable(editable)

    def setModel(self, model: QAbstractItemModel) -> None:
        self.combo_box.setModel(model)

    def setModelColumn(self, column: int) -> None:
        self.combo_box.setModelColumn(column)

    def setTitle(self, text: str) -> None:
        self.title.setText(text)

    def addItem(self, item: str) -> None:
        self.combo_box.addItem(item)

    def addItems(self, items: List[str]) -> None:
        self.combo_box.addItems(items)

    def text(self) -> str:
        return self.combo_box.currentText()