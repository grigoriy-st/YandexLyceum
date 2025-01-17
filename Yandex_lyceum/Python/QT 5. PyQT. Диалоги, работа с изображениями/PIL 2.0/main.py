import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow,
    QPushButton, QLabel, QFileDialog
)
from PyQt6.QtGui import QPixmap, QImage, QColor, QTransform
from PyQt6.QtCore import Qt


class MyPillow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(500, 600)
        self.setupUI()

    def setupUI(self):
        self.label = QLabel('', self)
        self.label.setScaledContents(True)
        # self.label.setFixedSize(300)
        self.label.setGeometry(130, 0, 150, 150)
        self.curr_image = QImage()
        self.r_img = None
        self.g_img = None
        self.b_img = None
        fileName, _ = QFileDialog.getOpenFileName(self,
                                                   self.tr("Open Image"),
                                                   ".",
                                                   self.tr("Image Files (*.png *.jpg *.bmp)"))
        if fileName:
            self.curr_image.load(fileName)
            self.label.setPixmap(QPixmap.fromImage(self.curr_image))


        self.channelButtons = {}
        for i, color in enumerate(['R', 'G', 'B', 'ALL']):
            button = QPushButton(color, self)
            button.setGeometry(10, 40 + i * 40, 100, 30)
            button.clicked.connect(self.color_change)
            self.channelButtons[color] = button

        # Кнопки для поворота
        self.counterclockwise = QPushButton('Против часовой стрелки', self)
        self.counterclockwise.setGeometry(10, 340, 150, 30)
        self.counterclockwise.clicked.connect(self.rotate_counterclockwise)

        self.clockwise = QPushButton('По часовой стрелке', self)
        self.clockwise.setGeometry(300, 340, 150, 30)
        self.clockwise.clicked.connect(self.rotate_clockwise)

    def color_change(self):
        sender = self.sender()
        color = sender.text()

        if color == 'R':
            self.change_color(1, 0, 0)
        elif color == 'G':
            self.change_color(0, 1, 0)
        elif color == 'B':
            self.change_color(0, 0, 1)
        elif color == 'ALL':
            self.label.setPixmap(QPixmap.fromImage(self.curr_image))

    def change_color(self, r, g, b):
        new_image = QImage(self.curr_image.size(), QImage.Format.Format_RGB16)

        for y in range(self.curr_image.height()):
            for x in range(self.curr_image.width()):
                pixel = self.curr_image.pixel(x, y)
                red = QColor(pixel).red() if r else 0
                green = QColor(pixel).green() if g else 0
                blue = QColor(pixel).blue() if b else 0

                new_image.setPixel(x, y, QColor(red, green, blue).rgb())

        self.label.setPixmap(QPixmap.fromImage(new_image))

    def rotate_counterclockwise(self):
        transform = QTransform().rotate(-90)
        self.curr_image = self.curr_image.transformed(transform)
        self.label.setPixmap(QPixmap.fromImage(self.curr_image))

    def rotate_clockwise(self):
        transform = QTransform().rotate(90)
        self.curr_image = self.curr_image.transformed(transform)
        self.label.setPixmap(QPixmap.fromImage(self.curr_image))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MyPillow()
    ui.show()
    sys.exit(app.exec())