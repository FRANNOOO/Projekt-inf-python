import sys
from PyQt5.QtCore import QPointF, Qt, QRectF
from PyQt5.QtGui import QBrush, QColor, QPainter, QPen, QPainterPath
from PyQt5.QtWidgets import QApplication, QWidget


class HeaterWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(400, 400)

        self.state = False  # Heater is initially off
        
    def changeState(self, state: bool):
        self.state = state
        self.update()

    def getState(self) -> bool:
        return self.state

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        color = Qt.red if self.state else Qt.black

        outer = QRectF(8, 45, 30, 30)
        inner = QRectF(15, 53, 15, 15)

        path = QPainterPath()
        path.moveTo(37.5, 60)
        path.arcTo(outer, 0, 180)
        path.arcTo(inner, 180, -180)
        path.lineTo(38, 60)

        painter.setPen(QPen(color, 1))
        painter.setBrush(color)
        painter.drawPath(path)

        painter.setBrush(color)
        painter.setPen(Qt.NoPen)

        painter.drawRect(
            0,
            278,
            45,
            23,
        )

        painter.drawRect(
            8,
            60,
            8,
            218,
        )

        painter.drawRect(
            30,
            60,
            8,
            218,
        )



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = HeaterWidget()
    w.setWindowTitle("Grzalka")
    w.resize(300, 300)
    w.show()
    sys.exit(app.exec_())