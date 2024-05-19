from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QHBoxLayout,
    QVBoxLayout,
    QStackedLayout,
    QSlider,
    QWidget,
    QLabel,
    QPushButton,
    QSizePolicy,
    QMenuBar,
    QTableView,
    QScrollArea,
    QDialog,
    QAbstractItemView,
)
from PySide6.QtGui import (
    QScreen,
    QAction,
    QFont
)
from PySide6.QtCore import (
    Qt,
    Signal
)
from PySide6.QtSql import (
    QSqlTableModel,
    QSqlRelationalTableModel,
    QSqlRelation,
    QSqlQuery,
    QSqlQueryModel
)

from modules.data_base import data_base
from modules.config import config

from ui.dialogs.new_audio_dialog import NewAudioDialog
from ui.dialogs.modify_audio_dialog import ModifyAudioDialog

from ui.widgets.pyside.push_button_widget import PushButtonWidget
from ui.widgets.pyside.v_box_layout_widget import VBoxLayoutWidget
from ui.widgets.pyside.h_box_layout_widget import HBoxLayoutWidget

from ui.widgets.search_info_panel_widget import SearchInfoPanelWidget

class AudioTableWidget(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        # attributes
    
        self.model = QSqlQueryModel(self)
        query = QSqlQuery("SELECT * FROM Audio", data_base.data_base)
        self.model.setQuery(query)

        # widgets
        
        self.table = QTableView(self)

        self.table.setModel(self.model)
        self.table.horizontalHeader().setFont(QFont(":/fonts/NotoSans.ttf",10))
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.verticalHeader().hide()

        self.setColumns()
        # layout

        self.main_layout = VBoxLayoutWidget()
        self.main_layout.addWidget(self.table)

        self.setLayout(self.main_layout)

    def onTableUpdate(self):
        query = QSqlQuery(self.model.query().executedQuery(), data_base.data_base)
        self.model.clear()
        self.model.query().clear()
        self.model.setQuery(query)

    def setColumns(self):
        return
        for parameter, shown in config.items('Library Shown Parameters'):
            match shown:
                case 'True':
                    self.table.showColumn(self.model.fieldIndex(parameter))
                case 'False':
                    self.table.hideColumn(self.model.fieldIndex(parameter))
