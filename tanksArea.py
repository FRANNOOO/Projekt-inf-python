from PyQt5.QtWidgets import QWidget
from tank import TankWidget
from tankSquare import TankWidgetSquare
from pipe import PipeWidget
from pump import PumpWidget
from heater import HeaterWidget
from valve import ValveWidget
from tanksLabels import TanksLabels


class TanksArea(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(1500, 900)
        self.build_pipes()
        self.build_devices()
        self.build_tanks()
        self.build_labels()

    def build_pipes(self):
        punkty1 = [(0, 10), (350, 10), (350, 50)]
        self.pipe1 = PipeWidget(punkty1, parent=self)
        self.pipe1.ustaw_przeplyw(True)
        self.pipe1.setFixedSize(600, 400)
        self.pipe1.move(0, 0)

        punkty2 = [(350, 0), (350, 170), (350, 130), (950, 130), (950, 220)]
        self.pipe2 = PipeWidget(punkty2, parent=self)
        self.pipe2.ustaw_przeplyw(True)
        self.pipe2.setFixedSize(1200, 400)
        self.pipe2.move(0, 320)

        punkty3 = [(350, 170), (350, 220)]
        self.pipe3 = PipeWidget(punkty3, parent=self)
        self.pipe3.ustaw_przeplyw(True)
        self.pipe3.setFixedSize(1200, 400)
        self.pipe3.move(0, 320)

        punkty4 = [
            (1000, 50),
            (520, 50),
            (520, 80),
            (580, 80),
            (580, 110),
            (520, 110),
            (520, 140),
            (580, 140),
            (580, 170),
            (520, 170),
            (520, 200),
            (580, 200),
            (580, 230),
            (520, 230),
            (520, 260),
            (1000, 260),
        ]
        self.pipe4 = PipeWidget(punkty4, parent=self)
        self.pipe4.setFixedSize(1200, 600)
        self.pipe4.move(0, 0)

    def build_devices(self):
        self.pump = PumpWidget(parent=self)
        self.pump.setFixedSize(60, 60)
        self.pump.move(800, 20)

        self.heater = HeaterWidget(parent=self)
        self.heater.setFixedSize(45, 300)
        self.heater.move(1300, 20)

        self.valve = ValveWidget(parent=self)
        self.valve.setFixedSize(50, 50)
        self.valve.move(325, 455)

    def build_tanks(self):
        self.tank1 = TankWidgetSquare(self)
        self.tank2 = TankWidgetSquare(self)
        self.tank3 = TankWidget(self)
        self.tank4 = TankWidget(self)
        for tank in (self.tank1, self.tank2, self.tank3, self.tank4):
            tank.setStyleSheet("background-color: #222;")
            tank.setFixedSize(tank.minimumSize())

        tank_positions = {
            self.tank1: (200, 20),
            self.tank2: (1000, 20),
            self.tank3: (200, 500),
            self.tank4: (800, 500),
        }

        for tank, (x, y) in tank_positions.items():
            tank.move(x, y)

        self.tank2.setPoziom(1)

    def build_labels(self):
        self.label_1 = TanksLabels(parent=self)
        self.label_1.set_label_position(375, 350)
        self.label_2 = TanksLabels(parent=self)
        self.label_2.set_label_position(875, 5)






