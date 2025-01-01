import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QPixmap


class UfoControl(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Управление НЛО")
        self.setGeometry(0, 0, 300, 300)
        self.ufo = QLabel(self)
        self.img = QPixmap("ufo.png")
        self.ufo.setPixmap(self.img)

    def keyPressEvent(self, event):
        x, y = self.ufo.x(), self.ufo.y()
        if event.key() == Qt.Key.Key_Up:
            y -= 10
        elif event.key() == Qt.Key.Key_Down:
            y += 10
        elif event.key() == Qt.Key.Key_Left:
            x -= 10
        elif event.key() == Qt.Key.Key_Right:
            x += 10

        x = x % 250
        y = y % 250
        self.ufo.move(x, y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UfoControl()
    window.show()
    sys.exit(app.exec())