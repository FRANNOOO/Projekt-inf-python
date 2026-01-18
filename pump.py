import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QBrush, QColor, QPainter, QPen
from PyQt5.QtWidgets import QApplication, QWidget


class PumpWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(30, 30)

        self._angle = 0.0
        self._rpm = 40.0
        self._timer = QTimer(self)
        self._timer.timeout.connect(self._tick)
        self._timer.start(30)

    def setRpm(self, rpm: float):
        self._rpm = max(0.0, float(rpm))

    def start(self):
        if not self._timer.isActive():
            self._timer.start(30)

    def stop(self):
        self._timer.stop()

    def isRunning(self) -> bool:
        return self._timer.isActive()

    def _tick(self):
        degrees_per_sec = self._rpm * 6.0
        self._angle = (self._angle + degrees_per_sec * 0.03) % 360.0
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        side = min(self.width(), self.height())
        cx = self.width() / 2.0
        cy = self.height() / 2.0
        radius = side * 0.42

        # Housing
        pen = QPen(Qt.gray, 6)
        painter.setPen(pen)
        painter.setBrush(QBrush(QColor(255, 255, 255)))
        painter.drawEllipse(int(cx - radius), int(cy - radius), int(radius * 2), int(radius * 2))

        # Impeller
        painter.save()
        painter.translate(cx, cy)
        painter.rotate(self._angle)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(QColor(150, 150, 150)))

        blade_w = radius * 0.4
        blade_h = radius * 1.8
        for i in range(4):
            painter.drawRoundedRect(
                int(-blade_w / 2),
                int(-blade_h / 2),
                int(blade_w),
                int(blade_h),
                4,
                4,
            )
            painter.rotate(90)

        # Hub
        painter.setBrush(QBrush(QColor(120, 120, 120)))
        hub_r = radius * 0.18
        painter.drawEllipse(int(-hub_r), int(-hub_r), int(hub_r * 2), int(hub_r * 2))
        painter.restore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = PumpWidget()
    w.setWindowTitle("Pompa obiegowa")
    w.resize(300, 300)
    w.show()
    sys.exit(app.exec_())