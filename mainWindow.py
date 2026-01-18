import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSlider,
    QVBoxLayout,
    QWidget,
)
from tanksArea import TanksArea
from visualizationController import VisualizationController

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Laboratorium: Zbiornik PyQt")
        self.resize(1500, 1080)

        root = QVBoxLayout()
        self.setLayout(root)

        self.tanks_area = TanksArea(self)
        root.addWidget(self.tanks_area)
        self.tank1 = self.tanks_area.tank1
        self.tank2 = self.tanks_area.tank2
        self.visualization = VisualizationController(self.tanks_area)
        self.visualization.sync_pipe_flow()

        self.slider1 = QSlider(Qt.Horizontal)
        self.slider1.setRange(0, 100)
        self.slider1.setValue(50)
        self.slider1.valueChanged.connect(self.zmien_poziom1)
        self.checkbox1 = QCheckBox("Auto")
        self.checkbox1.setChecked(True)
        self.checkbox1.toggled.connect(lambda checked: self.slider1.setEnabled(not checked))
        self.slider1.setEnabled(not self.checkbox1.isChecked())
        row1 = QHBoxLayout()
        row1.addWidget(self.slider1, 1)
        row1.addWidget(self.checkbox1)
        root.addLayout(row1)

        self.label1 = QLabel("Poziom 1: 50%")
        self.label1.setAlignment(Qt.AlignCenter)
        root.addWidget(self.label1)

        self.slider2 = QSlider(Qt.Horizontal)
        self.slider2.setRange(0, 100)
        self.slider2.setValue(50)
        self.slider2.valueChanged.connect(self.zmien_poziom2)
        self.btn = QPushButton("Start / Stop", self)
        self.btn.setGeometry(50, 550, 100, 30)
        self.btn.setStyleSheet("background-color: #444; color: white;")
        self.btn.clicked.connect(self.visualization.toogle_pump)
        row2 = QVBoxLayout()
        row2.addWidget(self.slider2, 1)
        row2.addWidget(self.btn)
        root.addLayout(row2)

        self.label2 = QLabel("Poziom 2: 50%")
        self.label2.setAlignment(Qt.AlignCenter)
        root.addWidget(self.label2)

    def zmien_poziom1(self, value):
        poziom_float = value / 100.0
        self.visualization.set_tank_level(self.tank1, poziom_float)
        self.label1.setText(f"Poziom 1: {value}%")

    def zmien_poziom2(self, value):
        poziom_float = value / 100.0
        self.visualization.set_tank_level(self.tank2, poziom_float)
        self.label2.setText(f"Poziom 2: {value}%")
