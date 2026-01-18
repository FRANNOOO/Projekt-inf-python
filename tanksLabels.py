import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class TanksLabels(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.temp_label = QLabel("Temp: 20 C", self)
        self.temp_label.setStyleSheet("color: #000; border: 3px solid #000; padding: 4px;")
        self.temp_label.adjustSize()
        self.temp_label.move(0, 0)
        self.setFixedSize(self.temp_label.size())


    def set_temperature(self, value):
        self.temp_label.setText(f"Temp: {value:.1f} C")
        self.temp_label.adjustSize()
        self.setFixedSize(self.temp_label.size())

    def set_label_position(self, x, y):
        self.move(x, y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = TanksLabels()
    w.setWindowTitle("Pompa obiegowa")
    w.resize(300, 300)
    w.show()
    sys.exit(app.exec_())
