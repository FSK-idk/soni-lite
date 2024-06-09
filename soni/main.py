import sys

from PySide6.QtWidgets import QApplication, QStyleFactory

from view.window.audio_player_window import AudioPlayerWindow

if __name__ == "__main__":
    app = QApplication(sys.argv + ['-platform', 'windows:darkmode=2'])
    style = QStyleFactory.create("Fusion")
    app.setStyle(style)
    ex = AudioPlayerWindow()
    ex.show()
    sys.exit(app.exec())
