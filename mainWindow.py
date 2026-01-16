import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QSlider, QVBoxLayout, QWidget, QHBoxLayout
from tank import TankWidget
from tankSquare import TankWidgetSquare

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Laboratorium: Zbiornik PyQt")
        self.resize(1920, 1080)

        root = QVBoxLayout()
        self.setLayout(root)

        tanks_row = QHBoxLayout()
        self.tank1 = TankWidget()
        self.tank2 = TankWidgetSquare()
        self.tank3 = TankWidgetSquare()
        self.tank4 = TankWidget()
        for tank in (self.tank1, self.tank2, self.tank3, self.tank4):
            tank.setStyleSheet("background-color: #222;")
            tanks_row.addWidget(tank)
        root.addLayout(tanks_row)

        self.slider1 = QSlider(Qt.Horizontal)
        self.slider1.setRange(0, 100)
        self.slider1.setValue(50)
        self.slider1.valueChanged.connect(self.zmien_poziom1)
        root.addWidget(self.slider1)

        self.label1 = QLabel("Poziom 1: 50%")
        self.label1.setAlignment(Qt.AlignCenter)
        root.addWidget(self.label1)

        self.slider2 = QSlider(Qt.Horizontal)
        self.slider2.setRange(0, 100)
        self.slider2.setValue(50)
        self.slider2.valueChanged.connect(self.zmien_poziom2)
        root.addWidget(self.slider2)

        self.label2 = QLabel("Poziom 2: 50%")
        self.label2.setAlignment(Qt.AlignCenter)
        root.addWidget(self.label2)

    def zmien_poziom1(self, value):
        poziom_float = value / 100.0
        self.tank1.setPoziom(poziom_float)
        self.label1.setText(f"Poziom 1: {value}%")

    def zmien_poziom2(self, value):
        poziom_float = value / 100.0
        self.tank2.setPoziom(poziom_float)
        self.label2.setText(f"Poziom 2: {value}%")
