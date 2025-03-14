import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import Qt, QPointF
from PyQt6.QtGui import QPixmap


class Car(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 300, 300)
        self.lbl = QLabel(self)
        self.lbl.setGeometry(0, 0, 50, 50)
        self.setMouseTracking(True)

        self.cur_img_point = 0
        self.imgs = [
            QPixmap("car1.png"),
            QPixmap("car2.png"),
            QPixmap("car3.png")
        ]
        self.pixmap = self.imgs[0]
        self.image_position = QPointF(0, 0)
        self.update_image()

    def update_image(self):
        """ Обновление изображения. """
        self.pixmap = self.imgs[self.cur_img_point]
        self.pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio)
        self.lbl.setPixmap(self.pixmap)

    def mouseMoveEvent(self, event):
        """ Отслеживание курсора. """
        pos = event.position()
        x = max(0, min(pos.x(), 250))
        y = max(0, min(pos.y(), 250))
        self.image_position = QPointF(x, y)
        self.lbl.move(self.image_position.toPoint())

    def keyPressEvent(self, event):
        """ Обработка нажатия пробела. Реакция на пробел. """
        if event.key() == Qt.Key.Key_Space:
            self.cur_img_point = (self.cur_img_point + 1) % 3
            self.update_image()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Car()
    window.show()
    sys.exit(app.exec())
