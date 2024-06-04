from PySide6.QtWidgets import QStackedLayout


class StackedLayoutWidget(QStackedLayout):
    def __init__(self) -> None:
        super().__init__()

        self.setContentsMargins(0, 0, 0, 0)


