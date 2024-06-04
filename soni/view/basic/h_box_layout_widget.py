from PySide6.QtWidgets import QHBoxLayout


class HBoxLayoutWidget(QHBoxLayout):
    def __init__(self) -> None:
        super().__init__()

        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(2)

