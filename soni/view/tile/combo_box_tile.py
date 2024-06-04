from PySide6.QtWidgets import QWidget, QSizePolicy

from model.combo_box_model import ComboBoxModel

from view.basic.label_widget import LabelWidget
from view.basic.combo_box_widget import ComboBoxWidget
from view.basic.v_box_layout_widget import VBoxLayoutWidget


class ComboBoxTile(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.combo_box_model = ComboBoxModel(self)

        self.title = LabelWidget(self)
        self.combo_box = ComboBoxWidget(self)

        self.combo_box.setModel(self.combo_box_model)

        self.main_layout = VBoxLayoutWidget()
        self.main_layout.addWidget(self.title)
        self.main_layout.addWidget(self.combo_box)

        self.setLayout(self.main_layout)

        self.setFixedHeight(self.main_layout.minimumSize().height())
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

    def setTable(self, table_name: str) -> None:
        self.combo_box_model.setTable(table_name)
        # self.combo_box.setModelColumn(0) # TODO: CHECK IF NEED

    def setReadOnly(self, read_only: bool):
        self.combo_box.lineEdit().setReadOnly(read_only)

    def setEditable(self, editable: bool) -> None:
        self.combo_box.setEditable(editable)

    def updateTable(self) -> None:
        current_text = self.combo_box.currentText()
        self.combo_box_model.updateTable()
        self.combo_box.clearFocus()
        self.combo_box.setCurrentText(current_text)

    def setTitle(self, text: str) -> None:
        self.title.setText(text)

    def setText(self, text: str) -> None:
        self.combo_box.setEditText(text)

    def text(self) -> str:
        return self.combo_box.currentText()
    
    def clearInput(self) -> None:
        self.combo_box.setCurrentIndex(-1)
        self.combo_box.clearFocus()