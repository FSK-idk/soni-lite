from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal

from etc.config import config

from view.basic.label_widget import LabelWidget
from view.basic.push_button_widget import PushButtonWidget
from view.basic.check_box_widget import CheckBoxWidget
from view.basic.v_box_layout_widget import VBoxLayoutWidget


check_box_text = {
        "album_name":               "Show album title",
        "genre_name":               "Show genre",
        "performer_name":           "Show performer",
        "composer_name":            "Show composer",
        "publisher_name":           "Show publisher",
        "modified_by_name":         "Show modified by",
        "picture_artist_name":      "Show picture artist",
        "text_author_name":         "Show text author",
}


class AudioTableHeaderSettingsWidget(QWidget):
    headerChanged = Signal()

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.title = LabelWidget(self)
        self.parameter_check_box = { check_box: CheckBoxWidget(self) for check_box, _ in check_box_text.items()}
        self.apply_button = PushButtonWidget(self)

        self.title.setText("Shown parameters")
        for parameter, checked in config.items("Audio Library Shown Parameters"):
            if parameter in check_box_text:
                self.parameter_check_box[parameter].setText(check_box_text[parameter])
                self.parameter_check_box[parameter].setChecked(checked == "True")
        self.apply_button.setText("Apply")
        self.apply_button.clicked.connect(self.apply)

        self.main_layout = VBoxLayoutWidget()
        self.main_layout.addWidget(self.title)
        for _, check_box in self.parameter_check_box.items():
            self.main_layout.addWidget(check_box)
        self.main_layout.addWidget(self.apply_button)

        self.setLayout(self.main_layout)

    def apply(self) -> None:
        for parameter, check_box in self.parameter_check_box.items():
            config["Audio Library Shown Parameters"][parameter] = "True" if check_box.isChecked() else "False"
        config.write()

        self.headerChanged.emit()