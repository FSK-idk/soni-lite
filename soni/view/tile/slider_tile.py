from PySide6.QtWidgets import QWidget, QSizePolicy
from PySide6.QtCore import Qt, Signal

from view.default.label_widget import LabelWidget
from view.default.slider_widget import SliderWidget
from view.default.v_box_layout_widget import VBoxLayoutWidget

class SliderTile(QWidget):
    # signals

    valueChanged = Signal(str)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        # widgets

        self.title = LabelWidget(self)

        self.slider = SliderWidget(self)
        self.slider.setOrientation(Qt.Orientation.Horizontal)

        # layout

        self.main_layout = VBoxLayoutWidget()
        self.main_layout.addWidget(self.title)
        self.main_layout.addWidget(self.slider)

        self.setLayout(self.main_layout)

        # geometry

        self.setFixedHeight(self.main_layout.minimumSize().height())
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

    def setTitle(self, text: str) -> None:
        self.title.setText(text)

    def value(self) -> int:
        return self.slider.value()