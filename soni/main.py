import sys

from PySide6.QtWidgets import QApplication

from view.window.audio_player_window import AudioPlayerWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    ex = AudioPlayerWindow()
    ex.show()
    sys.exit(app.exec())
