from PySide6.QtWidgets import QWidget, QSizePolicy
from PySide6.QtCore import Qt, Signal

from view.basic.label_widget import LabelWidget
from view.basic.slider_widget import SliderWidget
from view.basic.v_box_layout_widget import VBoxLayoutWidget


class SliderTile(QWidget):
    valueChanged = Signal(int)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.title = LabelWidget(self)
        self.slider = SliderWidget(self)

        self.slider.setOrientation(Qt.Orientation.Horizontal)
        self.slider.valueChanged.connect(self.valueChanged.emit)

        self.main_layout = VBoxLayoutWidget()
        self.main_layout.addWidget(self.title)
        self.main_layout.addWidget(self.slider)

        self.setLayout(self.main_layout)

        self.setFixedHeight(self.main_layout.minimumSize().height())
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

    def setTitle(self, text: str) -> None:
        self.title.setText(text)

    def setValue(self, value: int) -> None:
        self.slider.setValue(value)

    def value(self) -> int:
        return self.slider.value()
    
    def clearInput(self) -> None:
        self.slider.setValue(self.slider.minimum())