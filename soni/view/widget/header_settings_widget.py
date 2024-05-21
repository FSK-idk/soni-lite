from PySide6.QtWidgets import (
    QWidget,
)
from PySide6.QtCore import (
    Signal
)

from model.config import config

from view.default.label_widget import LabelWidget
from view.default.push_button_widget import PushButtonWidget
from view.default.check_box_widget import CheckBoxWidget
from view.default.v_box_layout_widget import VBoxLayoutWidget


check_box_text = {
        "album_title":              "Show album title",
        "duration":                 "Show duration",
        "genre":                    "Show genre",
        "language":                 "Show language",
        "rating":                   "Show rating",
        "bpm":                      "Show BPM",
        "performer":                "Show performer",
        "composer":                 "Show composer",
        "publisher":                "Show publisher",
        "modified_by":              "Show modified by",
        "release_date":             "Show release date",
        "picture_artist":           "Show picture artist",
        "text_author":              "Show text author",
        "original_title":           "Show original title",
        "original_album_title":     "Show original album title",
        "original_performer":       "Show original performer",
        "original_composer":        "Show original composer",
        "original_publisher":       "Show original publisher",
        "original_release_date":    "Show original release date",
        "original_text_author":     "Show original text author",
        "isrc":                     "Show ISRC",
}


class HeaderSettingsWidget(QWidget):
    headersChanged = Signal()

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.title = LabelWidget(self)
        self.parameter_check_box = { check_box: CheckBoxWidget(self) for check_box, _ in check_box_text.items()}

        self.title.setText("Shown parameters")

        for parameter, checked in config.items("Library Shown Parameters"):
            self.parameter_check_box[parameter].setText(check_box_text[parameter])
            self.parameter_check_box[parameter].setChecked(checked == 'True')

        self.main_layout = VBoxLayoutWidget()
        self.main_layout.addWidget(self.title)
        for _, check_box in self.parameter_check_box.items():
            self.main_layout.addWidget(check_box)

        self.setLayout(self.main_layout)

    def apply(self) -> None:
        for parameter, check_box in self.parameter_check_box.items():
            config['Library Shown Parameters'][parameter] = 'True' if check_box.isChecked() else 'False'
        config.write()

        self.headersChanged.emit()