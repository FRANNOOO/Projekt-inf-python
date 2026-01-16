from PyQt5.QtCore import QPointF, Qt, QRectF
from PyQt5.QtGui import QPainter, QPainterPath, QPen, QColor
from PyQt5.QtWidgets import QWidget


class TankWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(300, 400)

        # Parametry geometryczne
        self.top_trapez_h = 60  # Wysokosc gornego trapezu
        self.rect_h = 200       # Wysokosc srodka
        self.bot_trapez_h = 60  # Wysokosc dolnego trapezu

        self.width_top = 200  # Szerokosc wlotu
        self.width_mid = 140  # Szerokosc srodka
        self.width_bot = 40   # Szerokosc wylotu

        # Calkowita wysokosc "uzyteczna" zbiornika
        self.total_tank_height = self.top_trapez_h + self.rect_h + self.bot_trapez_h

        # Stan poczatkowy (0.0 - 1.0)
        self._poziom = 0.5

        # Pozycja rysowania wewnatrz widgetu
        self.draw_x = 50
        self.draw_y = 50

    def setPoziom(self, poziom: float):
        self._poziom = max(0.0, min(1.0, poziom))
        self.update()

    def setPolozenie(self, x: float, y: float):
        self.draw_x = x
        self.draw_y = y
        self.update()

    def getPoziom(self) -> float:
        return self._poziom

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # 1. Obliczamy punkty wzgledem draw_x i draw_y
        cx = self.draw_x + (self.width_top / 2)
        start_y = self.draw_y

        # 2. Definiujemy ksztalt zbiornika (sciezka)
        path = QPainterPath()

        # Punkty kluczowe
        p1_tl = QPointF(cx - self.width_top / 2, start_y)
        p1_tr = QPointF(cx + self.width_top / 2, start_y)
        p2_ml = QPointF(cx - self.width_mid / 2, start_y + self.top_trapez_h)
        p2_mr = QPointF(cx + self.width_mid / 2, start_y + self.top_trapez_h)
        p3_bl = QPointF(cx - self.width_mid / 2, start_y + self.top_trapez_h + self.rect_h)
        p3_br = QPointF(cx + self.width_mid / 2, start_y + self.top_trapez_h + self.rect_h)
        p4_bl = QPointF(cx - self.width_bot / 2, start_y + self.total_tank_height)
        p4_br = QPointF(cx + self.width_bot / 2, start_y + self.total_tank_height)

        # Budowanie sciezki (laczenie punktow)
        path.moveTo(p1_tl)
        path.lineTo(p1_tr)
        path.lineTo(p2_mr)
        path.lineTo(p3_br)
        path.lineTo(p4_br)
        path.lineTo(p4_bl)
        path.lineTo(p3_bl)
        path.lineTo(p2_ml)
        path.lineTo(p1_tl)
        path.closeSubpath()

        # 3. Rysowanie cieczy (z maskowaniem)
        painter.save()
        painter.setClipPath(path)

        liquid_height_px = self.total_tank_height * self._poziom

        rect_liquid = QRectF(
            cx - self.width_top / 2,
            start_y + self.total_tank_height - liquid_height_px,
            self.width_top,
            liquid_height_px,
        )

        painter.fillRect(rect_liquid, QColor(0, 120, 255, 180))
        painter.restore()

        # 4. Rysowanie obrysu na wierzchu
        pen = QPen(Qt.gray, 4)
        painter.setPen(pen)
        painter.setBrush(Qt.NoBrush)
        painter.drawPath(path)
