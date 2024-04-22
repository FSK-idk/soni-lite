import sys

from PySide6.QtWidgets import (
    QApplication,
)

from ui.windows.player_window import PlayerWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    ex = PlayerWindow()
    ex.show()
    sys.exit(app.exec())
