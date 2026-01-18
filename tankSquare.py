from PyQt5.QtCore import QPointF, Qt, QRectF
from PyQt5.QtGui import QPainter, QPainterPath, QPen, QColor
from PyQt5.QtWidgets import QWidget


class TankWidgetSquare(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(400, 300)

        # Parametry geometryczne
        self.width = 400  # Szerokosc zbiornika
        self.height = 300  # Wysokosc zbiornika

        # Stan poczatkowy (0.0 - 1.0)
        self._poziom = 0.5

    def setPoziom(self, poziom: float):
        self._poziom = max(0.0, min(1.0, poziom))
        self.update()

    def getPoziom(self) -> float:
        return self._poziom

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        path = QPainterPath()
    
        # Punkty kluczowe
        p1_tl = QPointF(0, 0)
        p2_tr = QPointF(self.width, 0)
        p3_br = QPointF(self.width, self.height)
        p4_bl = QPointF(0, self.height)

        # Budowanie sciezki (laczenie punktow)
        path.moveTo(p1_tl)
        path.lineTo(p4_bl)
        path.lineTo(p3_br)
        path.lineTo(p2_tr)

        liquid_height_px = self.height * self._poziom

        rect_liquid = QRectF(
            0,
            self.height - liquid_height_px,
            self.width,
            liquid_height_px,
        )

        painter.fillRect(rect_liquid, QColor(0, 120, 255, 180))
        painter.restore()

        # 4. Rysowanie obrysu na wierzchu
        pen = QPen(Qt.gray, 4)
        painter.setPen(pen)
        painter.setBrush(Qt.NoBrush)
        painter.drawPath(path)
