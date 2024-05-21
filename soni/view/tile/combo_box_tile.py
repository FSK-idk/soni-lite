from PySide6.QtWidgets import QWidget, QSizePolicy
from PySide6.QtCore import Signal
from PySide6.QtCore import Qt
from PySide6.QtSql import QSqlQuery, QSqlQueryModel

from model.data_base.data_base import data_base
from model.data_base.query import Queries

from view.default.label_widget import LabelWidget
from view.default.combo_box_widget import ComboBoxWidget
from view.default.v_box_layout_widget import VBoxLayoutWidget

class ComboBoxTile(QWidget):
    # signals

    textChanged = Signal(str)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        # attributes

        self.model = QSqlQueryModel(self)

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

    def clearTile(self) -> None:
        self.combo_box.setCurrentIndex(-1)
        self.combo_box.clearFocus()

    def setTable(self, table_name: str) -> None:
        self.model.setQuery(Queries.select_all(table_name, ["name"]), data_base.data_base)
        self.model.sort(0, Qt.SortOrder.AscendingOrder)
        self.combo_box.setModel(self.model)
        self.combo_box.setModelColumn(0)

    def setReadOnly(self, read_only: bool):
        self.combo_box.lineEdit().setReadOnly(read_only)

    def onTableUpdate(self) -> None:
        text = self.combo_box.currentText()
        query = QSqlQuery(self.model.query().executedQuery(), data_base.data_base)
        self.model.setQuery(query)
        self.combo_box.clearFocus()
        self.combo_box.setCurrentText(text)

    def setCurrentIndex(self, index: int) -> None:
        self.combo_box.setCurrentIndex(index)

    def setEditable(self, editable: bool) -> None:
        self.combo_box.setEditable(editable)

    def setTitle(self, text: str) -> None:
        self.title.setText(text)

    def text(self) -> str:
        return self.combo_box.currentText()