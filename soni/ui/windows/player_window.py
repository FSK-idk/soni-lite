from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QHBoxLayout,
    QVBoxLayout,
    QStackedLayout,
    QSlider,
    QWidget,
    QLabel,
    QPushButton,
    QSizePolicy,
    QMenuBar
)
from PySide6.QtGui import (
    QScreen
)
from PySide6.QtCore import (
    Qt
)

class PlayerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # TODO: rename fields
        # name
        self.setWindowTitle("soni")

        # geometry
        self.setGeometry(0, 0, 800, 400)

        # center window
        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geometry = self.geometry()
        geometry.moveCenter(center)
        self.move(geometry.topLeft())

        # menu
        self.menuBar().addMenu("123")

        # slider
        self.slider = QSlider()
        self.slider.setOrientation(Qt.Orientation.Horizontal)

        # image
        self.label = QLabel("Image")

        # Name
        self.name_label = QLabel("Name")

        # controls
        self.button = QPushButton()
        self.button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        
        # layout
        self.v_box_layout2 = QVBoxLayout()
        self.v_box_layout2.addWidget(self.name_label)
        self.v_box_layout2.addWidget(self.button)

        self.h_box_layout = QHBoxLayout()
        self.h_box_layout.addWidget(self.label)
        self.h_box_layout.addLayout(self.v_box_layout2)

        self.v_box_layout = QVBoxLayout()
        self.v_box_layout.addLayout(self.h_box_layout)
        self.v_box_layout.addWidget(self.slider)

        # set central widget
        self.widget = QWidget()
        self.widget.setLayout(self.v_box_layout)
        self.setCentralWidget(self.widget)

