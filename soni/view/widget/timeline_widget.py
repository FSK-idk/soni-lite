from PySide6.QtWidgets import (
    QWidget,
)
from PySide6.QtCore import (
    Qt,
)

from model.time import TimeFormat, TimeSpan

from view.default.clickable_label import ClickableLabelWidget
from view.default.slider_widget import SliderWidget
from view.default.v_box_layout_widget import VBoxLayoutWidget
from view.default.h_box_layout_widget import HBoxLayoutWidget


class TimelineWidget(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        
        # attributes
        self.time_span = TimeSpan()
        self.time_reversed = False

        # TODO: for debug
        self.time_span.set_end_time(123456)

        # widgets
        self.current_time = ClickableLabelWidget(self)
        self.current_time.setText(self.time_span.get_current_text())
        self.current_time.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.current_time.clicked.connect(self.setCurrentReversed)

        self.end_time = ClickableLabelWidget(self)
        self.end_time.setText(self.time_span.get_end_text())
        self.end_time.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.timeline = SliderWidget(self)
        self.timeline.setMaximum(self.time_span.end.milliseconds)
        self.timeline.valueChanged.connect(self.setCurrentMilliseconds)

        # layout
        
        self.time_layout = HBoxLayoutWidget()
        self.time_layout.addWidget(self.current_time)
        self.time_layout.addStretch()
        self.time_layout.addWidget(self.end_time)

        self.main_layout = VBoxLayoutWidget()
        self.main_layout.addLayout(self.time_layout)
        self.main_layout.addWidget(self.timeline)

        self.setLayout(self.main_layout)

    def setCurrentMilliseconds(self, milliseconds: int) -> None:
        self.time_span.set_current_time(milliseconds)
        self.current_time.setText(self.time_span.get_current_text())
        self.timeline.setValue(milliseconds)

    def setCurrentReversed(self) -> None:
        self.time_reversed = not self.time_reversed
        self.time_span.set_reversed(self.time_reversed)
        self.current_time.setText(self.time_span.get_current_text())

    def setEndMilliseconds(self, milliseconds: int) -> None:
        self.time_span.set_end_time(milliseconds)
        self.end_time.setText(self.time_span.get_end_text())
        self.timeline.setMaximum(milliseconds)

    def setTimeFormat(self, time_format: TimeFormat) -> None:
        self.time_span.set_time_format(time_format)
        self.current_time.setText(self.time_span.get_current_text())
        self.end_time.setText(self.time_span.get_end_text())

