from PySide6.QtWidgets import QWidget, QSizePolicy

from model.combo_box_model import ComboBoxModel

from view.basic.label_widget import LabelWidget
from view.basic.combo_box_widget import ComboBoxWidget
from view.basic.v_box_layout_widget import VBoxLayoutWidget


class ComboBoxTile(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.combo_box_model = ComboBoxModel(self)

        self.combo_box_model.preupdated.connect(self.preupdateComboBox)
        self.combo_box_model.updated.connect(self.updateComboBox)

        self.title = LabelWidget(self)
        self.combo_box = ComboBoxWidget(self)

        self.combo_box.setModel(self.combo_box_model)
        self.combo_box.editTextChanged.connect(self.combo_box_model.setText)

        self.main_layout = VBoxLayoutWidget()
        self.main_layout.addWidget(self.title)
        self.main_layout.addWidget(self.combo_box)

        self.setLayout(self.main_layout)

        self.setFixedHeight(self.main_layout.minimumSize().height())
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

    # Need to save text before update
    def preupdateComboBox(self, text) -> None:
        self.temp_text = text

    def updateComboBox(self) -> None:
        self.combo_box.setEditText(self.temp_text)

    def setTable(self, table_name: str) -> None:
        self.combo_box_model.setTable(table_name)

    def setReadOnly(self, read_only: bool) -> None:
        self.combo_box.lineEdit().setReadOnly(read_only)

    def setEditable(self, editable: bool) -> None:
        self.combo_box.setEditable(editable)

    def setTitle(self, text: str) -> None:
        self.title.setText(text)

    def setText(self, text: str) -> None:
        self.combo_box.setEditText(text)

    def text(self) -> str:
        return self.combo_box.currentText()
    
    def clearInput(self) -> None:
        self.combo_box.setCurrentIndex(-1)
        self.combo_box.clearFocus()