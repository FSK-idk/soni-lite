from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, Signal

from etc.time import TimeFormat, TimeSpan

from view.basic.push_label_widget import PushLabelWidget
from view.basic.label_widget import LabelWidget
from view.basic.slider_widget import SliderWidget
from view.basic.v_box_layout_widget import VBoxLayoutWidget
from view.basic.h_box_layout_widget import HBoxLayoutWidget

import resources.resources_rc


class TimelineWidget(QWidget):
    timeChanged = Signal(int)
    volumeChanged = Signal(int)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        
        self.time_span = TimeSpan()
        self.time_reversed = False

        self.current_time = PushLabelWidget(self)
        self.end_time = PushLabelWidget(self)
        self.timeline = SliderWidget(self)
        self.volume = LabelWidget(self)
        self.volume_pic = LabelWidget(self)
        self.volumeline = SliderWidget(self)

        self.current_time.setText(self.time_span.getCurrentText())
        self.current_time.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.current_time.clicked.connect(self.setCurrentReversed)
        self.current_time.setFixedWidth(50)
        self.end_time.setText(self.time_span.getEndText())
        self.end_time.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.end_time.setFixedWidth(50)
        self.timeline.setMaximum(self.time_span.end.milliseconds)
        self.timeline.valueChanged.connect(self.setCurrentMilliseconds)
        self.timeline.sliderMoved.connect(self.timeChanged.emit)

        self.volume_pic.setFixedWidth(30)
        self.volume_pic.setPixmap(QPixmap(":icon/volume-1-white.svg").scaled(20, 20))
        self.volume_pic.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.volume.setText("50")
        self.volume.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.volume.setFixedWidth(20)
        self.volumeline.setMaximum(100)
        self.volumeline.valueChanged.connect(self.setVolume)
        self.volumeline.sliderMoved.connect(self.volumeChanged.emit)
        self.volumeline.setValue(int(self.volume.text()))
        self.volumeline.setMaximumWidth(100)

        self.top_layout = HBoxLayoutWidget()
        self.top_layout.addWidget(self.current_time)
        self.top_layout.addWidget(self.volumeline)
        self.top_layout.addWidget(self.volume_pic)
        self.top_layout.addWidget(self.volume)
        self.top_layout.addStretch()
        self.top_layout.addWidget(self.end_time)

        self.main_layout = VBoxLayoutWidget()
        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addWidget(self.timeline)

        self.setLayout(self.main_layout)

    def setVolume(self, volume: int) -> None:
        self.volume.setText(str(volume))
        if volume == 0:
            self.volume_pic.setPixmap(QPixmap(":icon/volume-x-white.svg").scaled(20, 20))
        elif volume < 60:
            self.volume_pic.setPixmap(QPixmap(":icon/volume-1-white.svg").scaled(20, 20))
        else:
            self.volume_pic.setPixmap(QPixmap(":icon/volume-2-white.svg").scaled(20, 20))

    def setCurrentMilliseconds(self, milliseconds: int) -> None:
        self.time_span.setCurrentTime(milliseconds)
        self.current_time.setText(self.time_span.getCurrentText())
        self.timeline.setValue(milliseconds)

    def setCurrentReversed(self) -> None:
        self.time_reversed = not self.time_reversed
        self.time_span.setReversed(self.time_reversed)
        self.current_time.setText(self.time_span.getCurrentText())

    def setEndMilliseconds(self, milliseconds: int) -> None:
        self.time_span.setEndTime(milliseconds)
        self.end_time.setText(self.time_span.getEndText())
        self.timeline.setMaximum(milliseconds)

    def setTimeFormat(self, time_format: TimeFormat) -> None:
        self.time_span.setTimeFormat(time_format)
        self.current_time.setText(self.time_span.getCurrentText())
        self.end_time.setText(self.time_span.getEndText())

