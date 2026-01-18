import sys
from PyQt5.QtCore import QPointF, Qt, QRectF
from PyQt5.QtGui import QBrush, QColor, QPainter, QPen, QPainterPath
from PyQt5.QtWidgets import QApplication, QWidget


class ValveWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(400, 400)

        self.state = False  # Valve is initially closed
        
    def changeState(self, state: bool):
        self.state = state
        self.update()

    def getState(self) -> bool:
        return self.state

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)

        color = Qt.green if self.state else Qt.red
        angle = 90 if self.state else 0

        cx = 25
        cy = 25

        painter.save()
        painter.translate(cx, cy)
        painter.rotate(angle)
        painter.translate(-cx, -cy)

        painter.setPen(Qt.NoPen)
        painter.setBrush(color)
        painter.drawEllipse(20, 20, 10, 10)

        path = QPainterPath()
        path.moveTo(QPointF(10, 15))
        path.lineTo(QPointF(40, 35))
        path.lineTo(QPointF(40, 15))
        path.lineTo(QPointF(10, 35))
        path.closeSubpath()

        painter.drawPath(path)

        painter.restore()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = ValveWidget()
    w.setWindowTitle("Zawór")
    w.resize(50, 50)
    w.show()
    sys.exit(app.exec_())