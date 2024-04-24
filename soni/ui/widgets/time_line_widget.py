from PySide6.QtWidgets import (
    QWidget,
    QSlider,
    QHBoxLayout,
    QVBoxLayout,
)
from PySide6.QtCore import (
    Qt,
)

from ui.widgets.clickable_label import ClickableLabel

from modules.time import TimeFormat, TimeSpan


class TimeLineWidget(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        
        # attributes
        self.time_span = TimeSpan()
        self.time_reversed = False

        # TODO: for debug
        self.time_span.set_end_time(12345)

        # widgets
        self.current_time = ClickableLabel(self.time_span.get_current_text(), self)
        self.current_time.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.current_time.clicked.connect(self.setCurrentReversed)

        self.end_time = ClickableLabel(self.time_span.get_end_text(), self)
        self.end_time.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.time_line = QSlider(Qt.Orientation.Horizontal, self)
        self.time_line.setMaximum(self.time_span.end.seconds)
        self.time_line.valueChanged.connect(self.setCurrentSeconds)

        # layout
        self.time_layout = QHBoxLayout()
        self.time_layout.addWidget(self.current_time)
        self.time_layout.addStretch()
        self.time_layout.addWidget(self.end_time)

        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.time_layout)
        self.main_layout.addWidget(self.time_line)

        self.setLayout(self.main_layout)

    def setCurrentSeconds(self, seconds : int) -> None:
        self.time_span.set_current_time(seconds)
        self.current_time.setText(self.time_span.get_current_text())

    def setCurrentReversed(self) -> None:
        self.time_reversed = not self.time_reversed
        self.time_span.set_reversed(self.time_reversed)
        self.current_time.setText(self.time_span.get_current_text())

    def setEndSeconds(self, seconds : int) -> None:
        self.time_span.set_end_time(seconds)
        self.end_time.setText(self.time_span.get_end_text())

    def setTimeFormat(self, time_format : TimeFormat) -> None:
        self.time_span.set_time_format(time_format)
        self.current_time.setText(self.time_span.get_current_text())
        self.end_time.setText(self.time_span.get_end_text())

