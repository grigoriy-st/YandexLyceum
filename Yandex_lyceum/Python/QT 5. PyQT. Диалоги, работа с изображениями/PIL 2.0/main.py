import os
import sys

from PyQt6.QtWidgets import (
    QApplication, QMainWindow,
    QPushButton, QLabel, QFileDialog
)
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt

class MyPillow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(500, 600)
        self.setupUI()

    def setupUI(self):
        self.label = QLabel('', self)
        self.label.setScaledContents(True)
        self.label.setGeometry(130, 0, 400, 300)
        self.curr_image = QImage()


        fileName, _ = QFileDialog.getOpenFileName(self,
                                               self.tr("Open Image"),
                                               ".",
                                               self.tr("Image Files (*.png *.jpg *.bmp)"))
        if fileName:
            self.curr_image.load(fileName)
            self.label.setPixmap(QPixmap.fromImage(self.curr_image))

        self.btn_r = QPushButton('R', self)
        self.btn_r.setGeometry(10, 40, 100, 30)

        self.btn_g = QPushButton('G', self)
        self.btn_g.setGeometry(10, 80, 100, 30)

        self.btn_b = QPushButton('B', self)
        self.btn_b.setGeometry(10, 120, 100, 30)

        self.btn_all = QPushButton('ALL', self)
        self.btn_all.setGeometry(10, 160, 100, 30)

        self.channelButtons = [self.btn_r, self.btn_g, self.btn_b, self.btn_all]


        self.counterclockwise = QPushButton('Против часовой стрелки', self)
        self.counterclockwise.setGeometry(10, 340, 150, 30)
        self.clockwise = QPushButton('По часовой стрелке', self)
        self.clockwise.setGeometry(300, 340, 150, 30)

        self.rotateButtons = [self.counterclockwise, self.clockwise]

    def color_change(self, color):
        color = self.butto

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MyPillow()
    ui.show()
    sys.exit(app.exec())
